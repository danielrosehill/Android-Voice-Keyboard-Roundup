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
  The differentiation between these apps is therefore almost never recognition
  quality — it is the input surface and the post-processing.
- **Moonshine appears nowhere.** Despite being the obvious small-footprint
  candidate, no project in the list uses it as of 2026-09-22. That is a gap, not
  an oversight in the data.
