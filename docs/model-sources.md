# Where the models come from

Every on-device project in `data/projects.json` pulls its ASR weights from
Hugging Face at first run — none of them bundle the model in the APK except
`local-transcribe`. So the model catalogue is the upstream of this whole roundup:
a new small multilingual ASR model landing on the Hub is what makes the next
keyboard possible.

## The working collection

**<https://huggingface.co/collections/danielrosehill/asr-models-0926>** — *"ASR
Models 0926: a composite of models I've been trying and using across different
devices in September 2026. Both ASR post-processing small models and
multimodal."*

That collection is the curated end of this; the searches below are the raw feed.
Contents as of 2026-09-22, with the overlap against this roundup marked:

| Model | Note |
| --- | --- |
| `handy-computer/parakeet-tdt-0.6b-v3-gguf` | GGUF build of the model seven projects here already ship as ONNX |
| `handy-computer/parakeet-unified-en-0.6b-gguf` | the "best quality, non-free NVIDIA licence" option `ramblr` gates behind consent |
| `handy-computer/parakeet-tdt-0.6b-v2-gguf` | English-only v2, what `parakeet-voice-android` ships |
| `handy-computer/parakeet-tdt_ctc-1.1b-gguf`, `nvidia/parakeet-ctc-1.1b` | above the ~1B handset ceiling |
| `handy-computer/Qwen3-ASR-1.7B-gguf` | Qwen3-ASR, one of `bibi-keyboard`'s six local engines |
| `handy-computer/Voxtral-Mini-4B-Realtime-2602-gguf` | Mistral Voxtral; `voice-keyboard` uses the hosted `voxtral-mini` endpoint, not this |
| `trevornk/mumble-cleanup-2stage-GGUF` | `ramblr`'s own on-device cleanup model, published by its author |
| `mlx-community/parakeet-tdt-0.6b-v3` | Apple-silicon build — desktop, not Android |
| `oruk/orukeet`, `fishaudio/s1-mini`, `pyannote/speaker-diarization-3.1` | adjacent: post-processing, TTS, diarisation |

Two readings worth keeping. The `handy-computer` GGUF line is the same upstream
as `transcribe.cpp`, which is what `offline-voice-input` runs — so the GGUF and
ONNX camps are converging on identical weights and differ only in runtime. And
`trevornk` publishing a cleanup model to the Hub is the strongest signal in the
list that transcript cleanup is now a separate model problem from transcription,
which is exactly the split `ramblr` and `tobiboard` build around.

## NVIDIA Parakeet — the authoritative list

**<https://huggingface.co/collections/nvidia/parakeet-asr-659711f49d1469e51546e021>**
(short form `nvidia/parakeet-asr`) is NVIDIA's own collection and the canonical
roster of Parakeet models — 16 entries, last updated 2026-08-11. Go there first;
the third-party GGUF and ONNX conversions everyone ships are downstream of it and
lag it.

### Field experience, not benchmarks

Daniel's own results across devices, September 2026. These disagree with the
leaderboard ordering, and the field result wins:

- **`parakeet-tdt-0.6b-v2` outperforms `v3` in practice.** v2 is English-only;
  v3 buys 25 languages and gives back English accuracy for it. If you dictate in
  English, v2 is the better model despite being the older and less-starred one.
  Most Android projects default to v3 — `parakeet-voice-android` is the one that
  ships v2, and `ramblr` lets you pick.
- **`nvidia/parakeet-ctc-1.1b` is the step up when 0.6B is not accurate enough.**
  Second choice overall. ~600k downloads, the most-used 1.1B in the collection.
  Too large for most phones today, which is exactly why it matters as the
  reference point: it tells you how much accuracy you are leaving on the table
  by fitting into a handset.

### Architecture matters more than family

The bigger determinant of whether a model works on a phone is not which Parakeet
it is, but how it decodes. From the collection, four shapes:

| Suffix | Decoder | On-device consequence |
| --- | --- | --- |
| `ctc` | frame-independent, no decoder state | Cheapest and most streaming-friendly. No autoregressive state to carry, so memory is flat. Weakest at long-range context and formatting. |
| `rnnt` | RNN-Transducer, prediction network carries state | Naturally streaming and more accurate than CTC, but every step pays for the decoder state and joint network. |
| `tdt` | Token-and-Duration Transducer — predicts token *and* duration, skipping frames | Far fewer decoder steps than RNN-T at equal or better accuracy. Why `tdt-0.6b` is the on-device default everywhere. Still a transducer, so still stateful. |
| `tdt_ctc` | hybrid: one encoder, both heads | Lets you trade decode speed against accuracy from the same weights, at runtime. Underused in the Android projects here — nobody exposes the choice. |

**The real constraint is the context buffer.** The offline models
(`tdt-0.6b-v2`/`v3`) attend over a whole utterance, so working memory scales with
how much audio you hold. On a handset that forces a choice: chunk the audio and
lose context at the boundaries, or hold a long buffer and pay in RAM — which is
what makes the *slightly-less-than-real-time* operating point the sweet spot in
practice, and also what makes it hard to hit. Daniel's finding is that this
buffer behaviour, rather than the model family, is what decides whether a given
model is usable on a device.

Two entries in the collection address it directly and neither has been adopted by
any Android project in this roundup:

- [`nvidia/parakeet_realtime_eou_120m-v1`](https://huggingface.co/nvidia/parakeet_realtime_eou_120m-v1)
  — 120M streaming with end-of-utterance detection, bounded context. This is the
  shape a low-latency IME wants. `soniqo/speech-android` ships the nearest thing
  (Parakeet-EOU 120M at 153 MB), and it is an SDK rather than an app.
- [`nvidia/multitalker-parakeet-streaming-0.6b-v1`](https://huggingface.co/nvidia/multitalker-parakeet-streaming-0.6b-v1)
  — streaming 0.6B with speaker handling.

Also in the collection and worth knowing exist: `parakeet-tdt_ctc-0.6b-ja`
(Japanese), `parakeet-ctc-0.6b-Vietnamese`, `parakeet-rnnt-110m-da-dk` (Danish)
— per-language fine-tunes that beat multilingual v3 on their own language, and
`parakeet-tdt_ctc-110m` for the small end.

*Architecture descriptions above are from model documentation and general
knowledge of the NeMo decoders, not from measurements taken here. The two
comparative claims in "Field experience" are Daniel's, from use.*

## Hugging Face search links

Saved queries for the ASR task. Parameter-count filters matter here — an Android
handset realistically runs up to roughly 1B parameters quantised to int8, so the
1B and 2B views are the ones that map to shippable models.

| View | Link |
| --- | --- |
| ASR task, trending | <https://huggingface.co/models?pipeline_tag=automatic-speech-recognition&sort=trending> |
| ASR task, by downloads | <https://huggingface.co/models?pipeline_tag=automatic-speech-recognition&sort=downloads> |
| ASR ≤ 1B params | <https://huggingface.co/models?pipeline_tag=automatic-speech-recognition&num_parameters=min:0,max:1B&sort=downloads> |
| ASR ≤ 2B params | <https://huggingface.co/models?pipeline_tag=automatic-speech-recognition&num_parameters=min:0,max:2B&sort=downloads> |
| ASR ≤ 3B params | <https://huggingface.co/models?pipeline_tag=automatic-speech-recognition&num_parameters=min:0,max:3B&sort=downloads> |
| ASR ≤ 2B params, GGUF | <https://huggingface.co/models?pipeline_tag=automatic-speech-recognition&num_parameters=min:0,max:2B&library=gguf&sort=downloads> |

The `num_parameters` filter only applies to models whose config declares a
parameter count, so it silently drops repos that ship bare ONNX or GGUF without
one — the GGUF view in particular is narrower than the real GGUF population on
the Hub. Treat a short result list as a filter artefact, not as evidence that
few such models exist.

## The specific weights these projects fetch

Observed in the READMEs, 2026-09-22.

| Model | Size on device | Used by |
| --- | --- | --- |
| [`nvidia/parakeet-tdt-0.6b-v3`](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) (int8 ONNX, usually [istupakov's](https://huggingface.co/istupakov/parakeet-tdt-0.6b-v3-onnx) or [csukuangfj's](https://huggingface.co/csukuangfj/sherpa-onnx-nemo-parakeet-tdt-0.6b-v3-int8) conversion) | ~600–700 MB | `outspoke`, `tobiboard`, `translander`, `parakeeb`, `local-transcribe`, `sonderkey`, `ramblr` |
| `nvidia/parakeet-tdt-0.6b-v2` (English only) | ~600 MB | `parakeet-voice-android` |
| NVIDIA Canary 180M Flash | 153 MB | `ramblr` |
| Parakeet 110M | 104 MB | `ramblr` |
| Whisper base / small (ggml, via whisper.cpp) | 142 / 488 MB | `whisperboard`, `transcribro`, `futo-voice-input` |
| SenseVoice-Small (quantised ONNX) | ~230 MB | `fluence` |
| Silero VAD v4/v5 | ~2 MB | almost all of the on-device ones, for endpointing |

Two things follow from that table and are worth holding onto:

- **Parakeet TDT 0.6B v3 is the de facto default.** Seven of the eleven
  on-device projects ship the same int8 ONNX conversion behind `sherpa-onnx`.
  Differentiation between these apps is therefore mostly input surface and
  post-processing rather than recognition quality — with the caveat that v3 is
  the *default*, not the best English model (see the field notes above), and the
  projects that let you choose the weights are the ones that can be tuned.
- **Moonshine has exactly one implementation.** `whisper-speech-to-text` offers
  Moonshine v2 as a second engine beside Whisper — English-only, claimed 5-40x
  faster, in tiny/base/small/medium. Despite being the obvious small-footprint
  candidate it appears nowhere else, in a zero-star project that a GitHub sweep
  turned up rather than the stars list. Near-total absence, not total.
