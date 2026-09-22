# Android Voice Keyboard Roundup

Open-source voice input for Android, evaluated against a fixed set of questions
rather than summarised from each project's own pitch.

Seeded from the GitHub stars list
[**android-voice-keyboards**](https://github.com/stars/danielrosehill/lists/android-voice-keyboards),
which stays the intake queue: star a project there, run `scripts/refresh_list.py`,
annotate the stub it creates.

<!-- BEGIN snapshot -->
Data snapshot: **2026-09-22** · 40 keyboards, 4 other entries.
<!-- END snapshot -->

### Contents

1. **The apps** — the matrix, below, generated from `data/projects.json`.
2. **The models** — [`docs/model-sources.md`](docs/model-sources.md): NVIDIA's
   Parakeet roster, which weights each project fetches, and why decoder
   architecture decides on-device usability.
3. **Hugging Face links** — saved ASR searches and the working collection, in
   the same file.
4. **Development tooling** —
   [`docs/development-tooling.md`](docs/development-tooling.md): the inference
   engines, SDKs and Android platform APIs these projects are built on.

Plus [`docs/evaluation-criteria.md`](docs/evaluation-criteria.md), which defines
every field — read it before adding a row; the distinctions it draws are the
point of this repo.

`data/projects.json` is the source of truth. The tables below are generated from
it — do not hand-edit inside the `<!-- BEGIN … -->` markers.

Legend: ✅ yes · — no · ◐ partial · ? unknown · · not applicable.
**`?` means not stated anywhere I read, not "no".**
⭐ marks the one Daniel actually uses.

Each project in [Per-project notes](#per-project-notes) carries badges:

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square)
![Moonshine](https://img.shields.io/badge/Moonshine-F5A623?style=flat-square)
![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square)
![other](https://img.shields.io/badge/other_ASR-6B7280?style=flat-square)
— model family, then
![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)
![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square)
![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)
![Auto fallback](https://img.shields.io/badge/Auto_fallback-00897B?style=flat-square)
![Partial fallback](https://img.shields.io/badge/Partial_fallback-80CBC4?style=flat-square)
![Delegated](https://img.shields.io/badge/Delegated_STT-9E9E9E?style=flat-square)
— where inference runs.

**BYOK** means the cloud path needs your own API key or endpoint. Its absence
next to a Cloud badge means someone else is paying — which in this list is
either a vendor's own service (`pixelboard` uses Google's) or a free tier, and
is the thing most likely to change without notice.

## The three questions that actually separate these

Everything else is detail:

1. **How do you reach the microphone** — a voice-only IME, a full keyboard with
   a mic key, or a floating accessibility button over whatever keyboard you
   already use? This decides whether you have to give something up.
2. **Where does recognition run** — on the device, in the cloud, or on-device
   with a cloud escalation that happens automatically?
3. **Is the transcript cleaned up by a language model**, and if so, where does
   *that* run? Increasingly a separate question from recognition, with its own
   models.

## Form factor

Can it act as a voice IME, as a conventional full keyboard, and as a floating
button? These are independent; several projects do two, one does all three.

<!-- BEGIN capability -->
| Project | Voice IME | Full keyboard | Floating button |
| --- | :---: | :---: | :---: |
| [说点啥 (BiBi Keyboard)](https://github.com/BryceWG/BiBi-Keyboard) | ✅ | ◐ | ✅ |
| [Deskdrop](https://github.com/SvReenen/Deskdrop) | — | ✅ | — |
| [Dictate Keyboard](https://github.com/DevEmperor/DictateKeyboard) | — | ✅ | ✅ |
| [Dictus](https://github.com/getdictus/dictus-android) | — | ✅ | — |
| [Feelime](https://github.com/feelime/feelime) | — | ✅ | — |
| [Fluence](https://github.com/raviumeshkulkarni-web/Fluence-Android) | — | — | ✅ |
| [FUTO Keyboard](https://github.com/futo-org/android-keyboard) | — | ✅ | — |
| [FUTO Voice Input](https://github.com/futo-org/voice-input) | ✅ | — | — |
| [Kaiboard](https://github.com/kaisoapbox/kaiboard) | ✅ | — | — |
| [Kõnele](https://github.com/Kaljurand/K6nele) | ✅ | — | — |
| [Nemotron Voice Keyboard](https://github.com/catfewd/nemotron-voice-keyboard) | ✅ | — | — |
| [Offline Voice Input](https://github.com/notune/android_transcribe_app) | ✅ | — | — |
| [Orbie](https://github.com/MaxGoh/Orbie) | ✅ | — | — |
| [Outspoke](https://github.com/minburg/outspoke) | ✅ | — | — |
| [Parakeeb](https://github.com/surma/parakeeb) | ✅ | — | — |
| [Parakeet Voice](https://github.com/mpnikhil/parakeet-voice-android) | ✅ | — | — |
| [PixelBoard](https://github.com/Akshayykadam/PixelBoard) | — | ✅ | — |
| [Polished Recognition](https://github.com/georgernstgraf/polished-recognition) | ✅ | — | — |
| [Ramblr](https://github.com/trevornk/ramblr) | ✅ | — | ✅ |
| [Voice Keyboard (sahilchouksey)](https://github.com/sahilchouksey/voice-keyboard) | — | ✅ | — |
| [Sayboard](https://github.com/ElishaAz/Sayboard) | ✅ | — | — |
| [SonderKey](https://github.com/Verisonder/SonderKey) | — | ✅ | — |
| [TobiBoard](https://github.com/leinss/TobiBoard) | — | ✅ | — |
| [Transcribro](https://github.com/soupslurpr/Transcribro) | ✅ | — | — |
| [TranSlander](https://github.com/hatsch/TranSlander) | ✅ | — | ✅ |
| [Vertick IME](https://github.com/BurgerK1ng16/Vertick-IME) | — | ✅ | — |
| [Voice Keyboard](https://github.com/rustemar/voice-keyboard) | ✅ | — | — |
| [VoiceBoard](https://github.com/jagajaga/voiceboard) | ✅ | — | — |
| [VoiceFlow Keyboard](https://github.com/yutungh/voiceflow-keyboard-android) | — | ✅ | — |
| [VoxBoard](https://github.com/Predator04/VoxBoard) | — | ✅ | — |
| [VoxPen (語墨)](https://github.com/soanseng/voxpen-android) | ✅ | — | — |
| [Speech to Text (WhisperSpeechToText)](https://github.com/Jackfood2/WhisperSpeechToText) | ✅ | — | ✅ |
| [Whisper To Input](https://github.com/j3soon/whisper-to-input) | ✅ | — | — |
| [WhisperBoard](https://github.com/david-digitis/WhisperBoard) | — | ✅ | — |
| ⭐ [Whisperian](https://whisperian.app) | ✅ | — | ✅ |
| [whisperIME](https://github.com/woheller69/whisperIME) | ✅ | — | — |
| [whisperIME+](https://github.com/woheller69/whisperIMEplus) | ✅ | — | — |
| [WhisperInput](https://github.com/alex-vt/WhisperInput) | ✅ | — | — |
| [Whisper Voice Keyboard](https://github.com/MichaelMcCulloch/WhisperVoiceKeyboard) | ✅ | — | — |
| [Whispr AI](https://github.com/lam3y35/whispr-ai) | ✅ | — | — |
<!-- END capability -->

## Recognition

`Auto fallback` is strictly **automatic** cloud-to-local degradation. A manual
mode switch is not fallback, and neither is an offline queue that retries the
same cloud endpoint later.

<!-- BEGIN recognition -->
| Project | Local | Cloud | BYOK | Auto fallback | Whisper | NVIDIA | Moonshine | Other ASR |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| [说点啥 (BiBi Keyboard)](https://github.com/BryceWG/BiBi-Keyboard) | ✅ | ✅ | ✅ | ✅ | ? | ✅ | — | SenseVoice, FunASR Nano, Qwen3-ASR, FireRedASR, X-ASR |
| [Deskdrop](https://github.com/SvReenen/Deskdrop) | — | ✅ | ✅ | — | ✅ | — | — | Google Speech Recognition (delegated), self-hosted Whisper |
| [Dictate Keyboard](https://github.com/DevEmperor/DictateKeyboard) | ✅ | ✅ | ✅ | ◐ | ✅ | ✅ | — | Canary, Dolphin (40 Eastern languages), Deepgram Flux, Soniox, AssemblyAI, ElevenLabs, Gemini |
| [Dictus](https://github.com/getdictus/dictus-android) | ✅ | — | — | — | ✅ | ✅ | — | — |
| [Feelime](https://github.com/feelime/feelime) | ✅ | — | — | — | — | — | — | Zipformer (streaming), Paraformer (segment correction) |
| [Fluence](https://github.com/raviumeshkulkarni-web/Fluence-Android) | ✅ | ✅ | ✅ | — | ✅ | — | — | SenseVoice-Small (offline), Groq whisper-large-v3 (cloud) |
| [FUTO Keyboard](https://github.com/futo-org/android-keyboard) | ✅ | — | — | — | ✅ | — | — | — |
| [FUTO Voice Input](https://github.com/futo-org/voice-input) | ✅ | — | — | — | ✅ | — | — | — |
| [Kaiboard](https://github.com/kaisoapbox/kaiboard) | ✅ | — | — | — | ✅ | — | — | — |
| [Kõnele](https://github.com/Kaljurand/K6nele) | — | ✅ | ✅ | — | — | — | — | Kaldi (kaldi-gstreamer-server), PocketSphinx (unmaintained) |
| [Nemotron Voice Keyboard](https://github.com/catfewd/nemotron-voice-keyboard) | ✅ | — | — | — | — | ✅ | — | Nemotron-3 0.6B streaming INT8 |
| [Offline Voice Input](https://github.com/notune/android_transcribe_app) | ✅ | — | — | — | ? | ✅ | — | — |
| [Orbie](https://github.com/MaxGoh/Orbie) | ✅ | — | — | — | — | ✅ | — | Silero VAD |
| [Outspoke](https://github.com/minburg/outspoke) | ✅ | — | — | — | — | ✅ | — | Silero VAD v4 |
| [Parakeeb](https://github.com/surma/parakeeb) | ✅ | — | — | — | — | ✅ | — | — |
| [Parakeet Voice](https://github.com/mpnikhil/parakeet-voice-android) | ✅ | — | — | — | — | ✅ | — | Silero VAD |
| [PixelBoard](https://github.com/Akshayykadam/PixelBoard) | — | ✅ | — | — | — | — | — | Google Rambler (Gemini) |
| [Polished Recognition](https://github.com/georgernstgraf/polished-recognition) | — | ✅ | ✅ | — | ✅ | — | — | — |
| [Ramblr](https://github.com/trevornk/ramblr) | ✅ | ✅ | ✅ | ◐ | ✅ | ✅ | — | Parakeet TDT 0.6B v3, Parakeet Unified 0.6B, Canary 180M Flash, Parakeet 110M, gpt-4o-transcribe, Gemini |
| [Voice Keyboard (sahilchouksey)](https://github.com/sahilchouksey/voice-keyboard) | — | ✅ | ✅ | — | ? | — | — | — |
| [Sayboard](https://github.com/ElishaAz/Sayboard) | ✅ | — | — | — | — | — | — | Vosk (Kaldi) |
| [SonderKey](https://github.com/Verisonder/SonderKey) | ✅ | — | ✅ | — | — | ✅ | — | — |
| [TobiBoard](https://github.com/leinss/TobiBoard) | ✅ | ✅ | ✅ | ? | ? | ✅ | — | OpenRouter and PayPerQ cloud models |
| [Transcribro](https://github.com/soupslurpr/Transcribro) | ✅ | — | — | — | ✅ | — | — | Silero VAD |
| [TranSlander](https://github.com/hatsch/TranSlander) | ✅ | — | — | — | — | ✅ | — | — |
| [Vertick IME](https://github.com/BurgerK1ng16/Vertick-IME) | — | ✅ | ✅ | — | — | — | — | MiMo-V2.5-ASR |
| [Voice Keyboard](https://github.com/rustemar/voice-keyboard) | — | ✅ | ✅ | — | ✅ | — | — | Groq whisper-large-v3-turbo (default), Mistral voxtral-mini |
| [VoiceBoard](https://github.com/jagajaga/voiceboard) | — | ✅ | ✅ | — | — | — | — | gpt-4o-transcribe |
| [VoiceFlow Keyboard](https://github.com/yutungh/voiceflow-keyboard-android) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | Vosk (compact fallback), GPT Transcribe, Grok |
| [VoxBoard](https://github.com/Predator04/VoxBoard) | — | — | — | — | — | — | — | — |
| [VoxPen (語墨)](https://github.com/soanseng/voxpen-android) | — | ✅ | ✅ | — | ✅ | — | — | gpt-4o-transcribe |
| [Speech to Text (WhisperSpeechToText)](https://github.com/Jackfood2/WhisperSpeechToText) | ✅ | — | — | — | ✅ | — | ✅ | — |
| [Whisper To Input](https://github.com/j3soon/whisper-to-input) | — | ✅ | ✅ | — | ✅ | — | — | NVIDIA NIM / Riva whisper-large-v3, self-hosted Whisper ASR Webservice |
| [WhisperBoard](https://github.com/david-digitis/WhisperBoard) | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | Deepgram Nova-3 (cloud) |
| ⭐ [Whisperian](https://whisperian.app) | ✅ | ✅ | ✅ | ? | ✅ | ✅ | — | Deepgram, Groq (built-in free tier), custom OpenAI-compatible providers |
| [whisperIME](https://github.com/woheller69/whisperIME) | ✅ | — | — | — | ✅ | — | — | Android VAD |
| [whisperIME+](https://github.com/woheller69/whisperIMEplus) | ✅ | — | — | — | ✅ | — | — | Android VAD |
| [WhisperInput](https://github.com/alex-vt/WhisperInput) | ✅ | — | — | — | ✅ | — | — | — |
| [Whisper Voice Keyboard](https://github.com/MichaelMcCulloch/WhisperVoiceKeyboard) | ✅ | — | — | — | ✅ | — | — | — |
| [Whispr AI](https://github.com/lam3y35/whispr-ai) | — | — | — | — | — | — | — | — |
<!-- END recognition -->

## Post-processing and metadata

<!-- BEGIN postprocess -->
| Project | LLM cleanup (local) | LLM cleanup (cloud) | Runtime | Licence | ★ | Updated |
| --- | :---: | :---: | --- | --- | ---: | --- |
| [说点啥 (BiBi Keyboard)](https://github.com/BryceWG/BiBi-Keyboard) | ? | ✅ | unknown | Apache-2.0 | 803 | 2026-09-20 |
| [Deskdrop](https://github.com/SvReenen/Deskdrop) | ✅ | ✅ | n/a (delegated or self-hosted) | GPL-3.0 | 52 | 2026-09-22 |
| [Dictate Keyboard](https://github.com/DevEmperor/DictateKeyboard) | — | ✅ | unknown | Apache-2.0 | 284 | 2026-09-22 |
| [Dictus](https://github.com/getdictus/dictus-android) | — | — | whisper.cpp + sherpa-onnx | MIT | 20 | 2026-09-01 |
| [Feelime](https://github.com/feelime/feelime) | — | — | sherpa-onnx + librime | GPL-3.0 | 36 | 2026-09-21 |
| [Fluence](https://github.com/raviumeshkulkarni-web/Fluence-Android) | — | ✅ | sherpa-onnx | AGPL-3.0 | 15 | 2026-09-21 |
| [FUTO Keyboard](https://github.com/futo-org/android-keyboard) | — | — | whisper.cpp | FUTO Source First 1.1 (not OSI-approved) | 3238 | 2026-09-14 |
| [FUTO Voice Input](https://github.com/futo-org/voice-input) | — | — | whisper.cpp | FUTO Source First 1.0 (not OSI-approved) | 327 | 2025-09-16 |
| [Kaiboard](https://github.com/kaisoapbox/kaiboard) | — | — | whisper.cpp | BSD-3-Clause | 21 | 2025-02-22 |
| [Kõnele](https://github.com/Kaljurand/K6nele) | — | — | n/a (server) | Apache-2.0 | 291 | 2026-08-29 |
| [Nemotron Voice Keyboard](https://github.com/catfewd/nemotron-voice-keyboard) | — | — | parakeet-rs + ONNX Runtime (ort) | MIT | 3 | 2026-05-07 |
| [Offline Voice Input](https://github.com/notune/android_transcribe_app) | — | — | transcribe.cpp (ggml) via a Rust core | MIT | 302 | 2026-07-19 |
| [Orbie](https://github.com/MaxGoh/Orbie) | — | — | sherpa-onnx | MIT | 0 | 2026-07-06 |
| [Outspoke](https://github.com/minburg/outspoke) | — | — | onnxruntime | GPL-3.0 | 85 | 2026-08-29 |
| [Parakeeb](https://github.com/surma/parakeeb) | — | — | transcribe-rs / onnxruntime | MIT | 6 | 2026-07-18 |
| [Parakeet Voice](https://github.com/mpnikhil/parakeet-voice-android) | — | — | sherpa-onnx | NOASSERTION | 4 | 2026-04-20 |
| [PixelBoard](https://github.com/Akshayykadam/PixelBoard) | — | ✅ | n/a (Google cloud) | GPL-3.0 | 78 | 2026-09-18 |
| [Polished Recognition](https://github.com/georgernstgraf/polished-recognition) | ✅ | ✅ | n/a (cloud) | MIT | 7 | 2026-09-21 |
| [Ramblr](https://github.com/trevornk/ramblr) | ✅ | ✅ | sherpa-onnx + llama.cpp | GPL-3.0 | 51 | 2026-09-22 |
| [Voice Keyboard (sahilchouksey)](https://github.com/sahilchouksey/voice-keyboard) | — | — | n/a (self-hosted Bun server) | MIT | 0 | 2026-01-11 |
| [Sayboard](https://github.com/ElishaAz/Sayboard) | — | — | Vosk Android | GPL-3.0 | 583 | 2025-07-01 |
| [SonderKey](https://github.com/Verisonder/SonderKey) | — | ✅ | sherpa-onnx | GPL-3.0 | 8 | 2026-08-30 |
| [TobiBoard](https://github.com/leinss/TobiBoard) | ✅ | ✅ | sherpa-onnx | GPL-3.0 | 3 | 2026-09-14 |
| [Transcribro](https://github.com/soupslurpr/Transcribro) | — | — | whisper.cpp | ISC | 750 | 2025-08-29 |
| [TranSlander](https://github.com/hatsch/TranSlander) | — | — | sherpa-onnx | Apache-2.0 | 11 | 2026-02-08 |
| [Vertick IME](https://github.com/BurgerK1ng16/Vertick-IME) | — | ✅ | n/a (cloud) | GPL-3.0 | 35 | 2026-09-01 |
| [Voice Keyboard](https://github.com/rustemar/voice-keyboard) | — | ✅ | n/a (cloud) | MIT | 14 | 2026-09-22 |
| [VoiceBoard](https://github.com/jagajaga/voiceboard) | — | ✅ | n/a (cloud) | NOASSERTION | 0 | 2026-09-02 |
| [VoiceFlow Keyboard](https://github.com/yutungh/voiceflow-keyboard-android) | — | ✅ | sherpa-onnx + Vosk | MIT | 1 | 2026-08-30 |
| [VoxBoard](https://github.com/Predator04/VoxBoard) | — | — | n/a (delegated) | Apache-2.0 | 4 | 2026-07-08 |
| [VoxPen (語墨)](https://github.com/soanseng/voxpen-android) | — | ✅ | n/a (cloud) | Apache-2.0 | 8 | 2026-09-10 |
| [Speech to Text (WhisperSpeechToText)](https://github.com/Jackfood2/WhisperSpeechToText) | — | — | whisper.cpp JNI + Moonshine native | MIT | 0 | 2026-09-22 |
| [Whisper To Input](https://github.com/j3soon/whisper-to-input) | — | — | n/a (cloud or self-hosted) | GPL-3.0 | 138 | 2025-12-21 |
| [WhisperBoard](https://github.com/david-digitis/WhisperBoard) | — | — | whisper.cpp v1.8.3 | GPL-3.0 | 3 | 2026-05-15 |
| ⭐ [Whisperian](https://whisperian.app) | ? | ✅ | unknown | Proprietary (closed source) | — | 2026-09-22 |
| [whisperIME](https://github.com/woheller69/whisperIME) | — | — | TensorFlow Lite | MIT | 641 | 2026-08-30 |
| [whisperIME+](https://github.com/woheller69/whisperIMEplus) | — | — | ONNX Runtime (RTranslator models) | GPL-3.0 | 416 | 2026-09-01 |
| [WhisperInput](https://github.com/alex-vt/WhisperInput) | — | — | whisper.cpp | MIT | 114 | 2024-06-01 |
| [Whisper Voice Keyboard](https://github.com/MichaelMcCulloch/WhisperVoiceKeyboard) | — | — | TFLite + Rust/FFmpeg | MIT | 52 | 2023-06-10 |
| [Whispr AI](https://github.com/lam3y35/whispr-ai) | — | — | n/a on Android (delegated); sherpa-onnx on Windows | NOASSERTION | 0 | 2026-09-07 |
<!-- END postprocess -->

## What the matrix says

Reading down the columns rather than across the rows:

- **Nobody offers all three form factors with on-device recognition and
  automatic fallback.** The closest are `bibi-keyboard` (all three form factors,
  local + cloud + fallback, but Chinese-first and only a partial full keyboard)
  and `ramblr` (five trigger surfaces, local + cloud, but the fallback chain
  covers cleanup rather than transcription).
- **Full keyboard and voice IME are near-mutually-exclusive** and for a
  structural reason: the full keyboards are HeliBoard/FlorisBoard/LatinIME forks
  that *consume* the voice-IME slot, while the voice IMEs *fill* it. If you want
  a real keyboard plus dictation you are choosing a fork; if you want dictation
  layered onto the keyboard you already like, you want a voice IME or a floating
  button.
- **Automatic cloud-to-local fallback is rare** — three of thirty-nine.
  `whisperboard` states it plainly, `bibi-keyboard` implements it as a resident
  local engine behind a primary/backup pair, and `voiceflow-keyboard` degrades
  to a pre-downloaded offline model when there is no validated connection.
  `tobiboard` has both halves but does not say whether it bridges them.
  Everything else makes you choose a mode up front.
- **Whisper is losing to NVIDIA Parakeet on-device.** Whisper still dominates
  the cloud rows because that is what Groq and OpenAI serve; the local rows are
  overwhelmingly Parakeet TDT 0.6B v3 via sherpa-onnx. Note that v3 is the
  *default*, not the best choice for English dictation — v2 is, in practice —
  and only `ramblr` and `parakeet-voice-android` give you the option. See
  [`docs/model-sources.md`](docs/model-sources.md), where the decisive variable
  turns out to be decoder architecture and context-buffer behaviour rather than
  model family.
- **Moonshine has exactly one implementation** — `whisper-speech-to-text`,
  which offers it as a second engine beside Whisper (English-only, claimed
  5-40x faster). It has zero stars and was not in the original stars list; it
  took a GitHub sweep to find. Every other project here is Whisper or Parakeet.
- **Gboard cannot be redirected.** Three separate projects document it
  independently: Gboard's mic is hardcoded to Google's voice typing and will not
  delegate to a third-party voice IME. Samsung's keyboard is the same. Any
  project promising to replace Gboard's mic means either a `RecognitionService`
  (which Gboard also ignores) or switching keyboards. `pixelboard` is the
  exception that proves it — it does not redirect Gboard, it ships a patched
  Gboard.
- **Two projects advertise on-device recognition and delegate to
  `SpeechRecognizer` instead** — `voxboard` and `whispr-ai` (Android half; its
  Windows half really does run Parakeet). Neither is lying exactly; both say so
  somewhere below the headline. It is the single most common way the catalogue
  description and the code disagree, so check it first on any new entry.
- **Most projects implement one integration point when four exist.** Only
  `offline-voice-input`, `whisperime` and `whisperimeplus` cover IME +
  `RecognitionService` + `RECOGNIZE_SPEECH`; only `translander` adds the
  accessibility overlay on top. See
  [`docs/development-tooling.md`](docs/development-tooling.md).

## Per-project notes

<!-- BEGIN notes -->
### 说点啥 (BiBi Keyboard)

![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![SenseVoice](https://img.shields.io/badge/SenseVoice-6B7280?style=flat-square) ![FunASR Nano](https://img.shields.io/badge/FunASR_Nano-6B7280?style=flat-square) ![Qwen3-ASR](https://img.shields.io/badge/Qwen3--ASR-6B7280?style=flat-square) ![FireRedASR](https://img.shields.io/badge/FireRedASR-6B7280?style=flat-square) ![X-ASR](https://img.shields.io/badge/X--ASR-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square) ![Auto fallback](https://img.shields.io/badge/Auto_fallback-00897B?style=flat-square) ![Delegated STT](https://img.shields.io/badge/Delegated_STT-9E9E9E?style=flat-square)

`bibi-keyboard` · <https://github.com/BryceWG/BiBi-Keyboard> · Apache-2.0 · 803★ · last updated 2026-09-20

The most feature-complete of the set. 18 ASR providers, 12 cloud and 6 local, with an explicit primary/backup arrangement and a resident local engine as the last resort (主备与本地兜底) — the clearest automatic cloud-to-local fallback in the list. The floating ball (悬浮球) is the accessibility-overlay kind and works over any other IME. full_keyboard is partial: the layout is a configurable key pool and AI edit panel, not a general alphabet keyboard. Also exposes itself to third-party apps over SpeechRecognizer and AIDL, and can drive Fcitx/Rime forks. Has a paid Pro tier on Play; the repo is the free app.

### Deskdrop

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Google Speech Recognition](https://img.shields.io/badge/Google_Speech_Recognition-6B7280?style=flat-square) ![self-hosted Whisper](https://img.shields.io/badge/self--hosted_Whisper-6B7280?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square) ![Delegated STT](https://img.shields.io/badge/Delegated_STT-9E9E9E?style=flat-square)

`deskdrop` · <https://github.com/SvReenen/Deskdrop> · GPL-3.0 · 52★ · last updated 2026-09-22

A HeliBoard fork built for self-hosted LLM setups rather than for dictation — Ollama, LM Studio, vLLM, llama.cpp or KoboldCpp, with MCP support for Home Assistant and a primary-plus-LAN/Tailscale fallback URL. Its LLM layer has the automatic cloud fallback that its speech layer does not: when your local server goes down, shortcuts switch to a cloud model and revert when it returns. Voice itself is thin — Google Speech Recognition (so delegated, not on-device) or a self-hosted Whisper endpoint. Included because it is the clearest example in the list of the keyboard becoming an LLM surface with dictation as a side feature, and for the local-first fallback design worth copying.

### Dictate Keyboard

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Canary](https://img.shields.io/badge/Canary-6B7280?style=flat-square) ![Dolphin](https://img.shields.io/badge/Dolphin-6B7280?style=flat-square) ![Deepgram Flux](https://img.shields.io/badge/Deepgram_Flux-6B7280?style=flat-square) ![Soniox](https://img.shields.io/badge/Soniox-6B7280?style=flat-square) ![AssemblyAI](https://img.shields.io/badge/AssemblyAI-6B7280?style=flat-square) ![ElevenLabs](https://img.shields.io/badge/ElevenLabs-6B7280?style=flat-square) ![Gemini](https://img.shields.io/badge/Gemini-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square) ![Partial fallback](https://img.shields.io/badge/Partial_fallback-80CBC4?style=flat-square)

`dictate-keyboard` · <https://github.com/DevEmperor/DictateKeyboard> · Apache-2.0 · 284★ · last updated 2026-09-22

The biggest omission from the original list and arguably the most complete project in the roundup. A full FlorisBoard-based keyboard (glide typing, next-word prediction, autocorrect) with dictation on top, a floating button, AND registration as a system-wide voice input — so other keyboards' mic keys transcribe through it with no accessibility permission, which means it works in apps that block accessibility. Both engines: cloud streaming from six providers (Deepgram Flux decides turn-end itself rather than waiting out a silence timer) and on-device Whisper, Parakeet, Canary and Dolphin. Dolphin is notable — 40 Eastern languages in 105 MB, and the README states Whisper answers Hindi in the wrong script. Hold the send button to run a single dictation locally without switching providers. fallback is partial: you can force one local dictation by hand, but automatic cloud-to-local degradation is not claimed. Paid on Play, free if you build it.

### Dictus

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`dictus` · <https://github.com/getdictus/dictus-android> · MIT · 20★ · last updated 2026-09-01

One of only two projects running both engines side by side — Whisper via whisper.cpp for multilingual, Parakeet via sherpa-onnx for fast English — and it is a full system IME with AZERTY/QWERTY layouts and FR+EN prediction dictionaries rather than a voice-only panel. No cloud path at all. Part of a three-platform family (dictus-ios, dictus-desktop) sharing a brand repo. Smallest Whisper model is ~150 MB, so the cheapest entry point to on-device dictation here. On-device LLM reformulation is roadmap, not shipped.

### Feelime

![Zipformer](https://img.shields.io/badge/Zipformer-6B7280?style=flat-square) ![Paraformer](https://img.shields.io/badge/Paraformer-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`feelime` · <https://github.com/feelime/feelime> · GPL-3.0 · 36★ · last updated 2026-09-21

Architecturally the odd one out and worth reading for that alone: the keyboard UI is plain HTML/CSS/JS rendered in a WebView that calls Android's InputConnection over a controlled JS bridge, so you can restyle or re-lay-out the keyboard without repacking the APK (debug builds even support hot-pushed keyboard updates). Dual-channel speech — streaming Zipformer for provisional text, Paraformer re-correcting the whole segment at each pause, then local punctuation and English casing restoration. Fully offline: WebView has network and file access disabled and a CSP blocking external links. Chinese-first (full/double Pinyin, T9, stroke input via librime) with English, French, Russian and Japanese romaji dictionaries.

### Fluence

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![SenseVoice-Small](https://img.shields.io/badge/SenseVoice--Small-6B7280?style=flat-square) ![Groq whisper-large-v3](https://img.shields.io/badge/Groq_whisper--large--v3-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)

`fluence` · <https://github.com/raviumeshkulkarni-web/Fluence-Android> · AGPL-3.0 · 15★ · last updated 2026-09-21

Deliberately not an IME at all — the pitch is that you keep your own keyboard and a glassmorphic bubble follows the cursor. Cloud and offline are a toggle, not a fallback chain. Agent Mode (Llama 3.3 70B via Groq) takes spoken commands like 'delete the last two sentences' and edits in place, which nothing else here does.

### FUTO Keyboard

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`futo-keyboard` · <https://github.com/futo-org/android-keyboard> · FUTO Source First 1.1 (not OSI-approved) · 3238★ · last updated 2026-09-14

By far the most-starred and the most mature keyboard here — a LatinIME fork with FUTO Voice Input built in. Voice is a mode inside the keyboard rather than a separate voice IME, so it consumes the voice-IME slot rather than filling it; you can force it to delegate to the standalone app by disabling built-in voice input. Source-available, not open source: the licence is FUTO Source First 1.1 and PRs need a CLA. This repo is a mirror of an internal GitLab.

### FUTO Voice Input

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`futo-voice-input` · <https://github.com/futo-org/voice-input> · FUTO Source First 1.0 (not OSI-approved) · 327★ · last updated 2025-09-16

The reference implementation of the voice-IME pattern, and the source of the keyboard-compatibility table everyone else repeats. Registers both as a voice-subtype IME and as a RECOGNIZE_SPEECH intent handler; the intent path opens a centred floating window, which is a system dialog and not an accessibility overlay. Does NOT implement SpeechRecognizer. Development has largely moved to FUTO Keyboard — last touched 2025-09-16, the only stale entry besides whispervoicekeyboard. 17 languages, capped at Whisper languages with >1000 training hours.

### Kaiboard

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`kaiboard` · <https://github.com/kaisoapbox/kaiboard> · BSD-3-Clause · 21★ · last updated 2025-02-22

The direct successor to whispervoicekeyboard — the author credits MichaelMcCulloch's abandoned version and rebuilt it on whisper.cpp, which is exactly the rewrite that project's README said it needed. WhisperBoard in turn credits kaiboard as its JNI reference, so this is the middle link in a three-project chain. Model is added to assets at build time; there is no in-app model picker (it is on the roadmap along with realtime transcription, marked partial success). Last commit 2025-02-22.

### Kõnele

![Kaldi](https://img.shields.io/badge/Kaldi-6B7280?style=flat-square) ![PocketSphinx](https://img.shields.io/badge/PocketSphinx-6B7280?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)

`konele` · <https://github.com/Kaljurand/K6nele> · Apache-2.0 · 291★ · last updated 2026-08-29

The ancestor of this whole category — a voice IME, a RecognizerIntent panel and two SpeechRecognizer implementations, predating Whisper entirely. Recognition runs on a kaldi-gstreamer-server you point it at, so `local` is no in the sense used here even though you can self-host. The in-app SpeechRecognizer implementations are deprecated in favour of the separate Kõnele service app. Built for Estonian and for grammar-based voice commands. Its `speechutils` library is reused by WhisperInput and LocalSTT, so several newer projects inherit its permission model — and, per WhisperInput's own README, its permission bugs.

### Nemotron Voice Keyboard

![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Nemotron-3 0.6B streaming INT8](https://img.shields.io/badge/Nemotron--3_0.6B_streaming_INT8-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`nemotron-voice-keyboard` · <https://github.com/catfewd/nemotron-voice-keyboard> · MIT · 3★ · last updated 2026-05-07

The only project running NVIDIA Nemotron rather than Parakeet or Whisper, and one of only two doing real streaming recognition on-device. Another fork of notune's architecture, in Rust via parakeet-rs and the ort bindings. Reverts to your previous keyboard automatically the moment you stop speaking, which is the right behaviour for a voice-only IME and which almost nothing else does. Registers as a system voice input provider and also does live subtitles. Author states plainly that they are not a programmer; model quantisation is lokkju's. Interesting for the model choice, not for maturity — 3 stars, last commit 2026-05-07.

### Offline Voice Input

![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`offline-voice-input` · <https://github.com/notune/android_transcribe_app> · MIT · 302★ · last updated 2026-07-19

The best-integrated of the pure on-device ones: it plugs into Android speech in all three ways at once — RECOGNIZE_SPEECH popup, RecognitionService, and a voice IME — so it works from SwiftKey's mic, from website voice search, and from the keyboard switcher. The README's keyboard-by-keyboard notes were verified against each keyboard's source by the author. Also does live subtitles over screen capture. On Play as well as GitHub. Supports loading custom speech models.

### Orbie

![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`orbie` · <https://github.com/MaxGoh/Orbie> · MIT · 0★ · last updated 2026-07-06

Radically minimal: one orb, no keys — hold, speak, release. Built explicitly for dictating long prompts to AI agents from a phone, which is a different design target from messaging and shows in the UI. Parakeet on-device via a vendored sherpa-onnx AAR. Notable for its README: it has a section addressed to AI agents setting the app up on someone's behalf, with a condensed checklist — the only project here that assumes an agent reader. Needs ~1.5 GB free and 4 GB+ RAM; the model alone is ~661 MB and loads ~1.2 GB resident.

### Outspoke

![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`outspoke` · <https://github.com/minburg/outspoke> · GPL-3.0 · 85★ · last updated 2026-08-29

The cleanest single-purpose voice IME: Parakeet only, offline only, no LLM, no cloud path to misconfigure. Progressive partial results while you speak, hold-to-talk or tap-to-toggle, and a microphone-calibration screen that ranks every mic on the device by capture fidelity and picks the best — nothing else in the list does that. Architecture is built around a swappable SpeechEngine interface, so a second model backend is one class away. Needs Android 11+, 4 GB RAM, ~750 MB storage.

### Parakeeb

![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`parakeeb` · <https://github.com/surma/parakeeb> · MIT · 6★ · last updated 2026-07-18

A fork of offline-voice-input carrying a mostly unedited upstream README — the badges and package name still point at notune's app, so read it as inheriting that project's behaviour rather than describing its own. Its actual contribution is ONNX Runtime execution-provider tuning: the EP list and graph-optimisation level are settable at runtime over adb setprop without a rebuild, and the author measured that NNAPI/Darwinn on a Pixel 8a is slower than XNNPACK for the int8 Parakeet model. Worth reading for that finding even if you run something else.

### Parakeet Voice

![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`parakeet-voice-android` · <https://github.com/mpnikhil/parakeet-voice-android> · NOASSERTION · 4★ · last updated 2026-04-20

Small and direct. Its selling point is the RecognitionService implementation: set it as the system default voice input and Gboard's own mic button transcribes locally, keeping Gboard for typing. English only — it ships Parakeet TDT v2, and the README names the one-line change to swap in multilingual v3 at ~3% WER cost on English. Do not take that as an upgrade: v2 is the better English model in practice (see docs/model-sources.md), so shipping it is a point in this project's favour rather than a limitation. arm64-v8a only. Offers the best verification trick in the list: turn on airplane mode and dictate.

### PixelBoard

![Google Rambler](https://img.shields.io/badge/Google_Rambler-6B7280?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square)

`pixelboard` · <https://github.com/Akshayykadam/PixelBoard> · GPL-3.0 · 78★ · last updated 2026-09-18

Not open-source software in the sense the rest of this list is — a patched Gboard APK with an independent package id, pre-patched to bypass Play signature and integrity checks, so it installs alongside stock Gboard. It exists to unlock Google's Rambler voice typing (filler-word removal, self-correction repair, context-aware punctuation, mid-sentence language mixing) and the Gemini writing tools on non-Pixel phones. Recognition is Google's cloud. Included because it is the only route in this roundup to Rambler-class cleanup quality, and because it is the direct counterexample to the Gboard-cannot-be-redirected rule: you do not redirect Gboard's mic, you replace Gboard. Judge the redistribution and signature-bypass question yourself.

### Polished Recognition

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)

`polished-recognition` · <https://github.com/georgernstgraf/polished-recognition> · MIT · 7★ · last updated 2026-09-21

Cloud STT only — the local option is for the polish step (Ollama or LM Studio over the OpenAI contract), not for recognition, so a claim of 'or run a local model' should not be read as on-device ASR. 18 provider presets and dynamic model lists off each provider's /v1/models. Recording starts the instant you switch to the keyboard, and survives switching away to your typing keyboard and back. Raw mode skips the LLM. On F-Droid; the Play build is closed testing and needs 12 continuously opted-in testers.

### Ramblr

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Parakeet TDT 0.6B v3](https://img.shields.io/badge/Parakeet_TDT_0.6B_v3-6B7280?style=flat-square) ![Parakeet Unified 0.6B](https://img.shields.io/badge/Parakeet_Unified_0.6B-6B7280?style=flat-square) ![Canary 180M Flash](https://img.shields.io/badge/Canary_180M_Flash-6B7280?style=flat-square) ![Parakeet 110M](https://img.shields.io/badge/Parakeet_110M-6B7280?style=flat-square) ![gpt-4o-transcribe](https://img.shields.io/badge/gpt--4o--transcribe-6B7280?style=flat-square) ![Gemini](https://img.shields.io/badge/Gemini-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square) ![Partial fallback](https://img.shields.io/badge/Partial_fallback-80CBC4?style=flat-square)

`ramblr` · <https://github.com/trevornk/ramblr> · GPL-3.0 · 51★ · last updated 2026-09-22

The most thoroughly engineered project in the list and the only one shipping ADRs and field latency data. Five independent ways to trigger dictation (floating ring, voice IME, accessibility button / volume-hold, QS tile, text-selection menu), of which the IME and the selection menu need no accessibility grant. Transcription and cleanup are chosen independently, so local STT plus cloud cleanup is a normal setup. fallback is 'partial' on purpose: the ordered waterfall with on-device as the floor applies to CLEANUP only — transcription is a single configured provider with no automatic degradation. Chain capped at 8 s, tuned from 34 days of p99 data. Four local ASR models and two local cleanup models, all downloaded on demand, none bundled.

### Voice Keyboard (sahilchouksey)

![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)

`sahilchouksey-voice-keyboard` · <https://github.com/sahilchouksey/voice-keyboard> · MIT · 0★ · last updated 2026-01-11

Full QWERTY IME with voice on top, transcribing against a Bun.js server you run yourself, with a React Native settings app. Two ergonomics worth stealing: swipe the space bar as a cursor joystick, and hold backspace then swipe to select and delete by word. Explicitly supports terminal and TUI apps, which nothing else here mentions. Last commit 2026-01-11.

### Sayboard

![Vosk](https://img.shields.io/badge/Vosk-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`sayboard` · <https://github.com/ElishaAz/Sayboard> · GPL-3.0 · 583★ · last updated 2025-07-01

The only Vosk project in the roundup, and the counterexample to the Whisper/Parakeet duopoly: Vosk models are tiny (tens of MB against hundreds), stream natively, and cover languages the others do not — at lower accuracy. Voice IME plus a RecognitionService. INTERNET is only for the model downloader and can be revoked on ROMs that allow it. Documents a real Android bug: a speech RecognitionService needs QUERY_ALL_PACKAGES to work properly (K6nele-service issue #9). Last commit 2025-07-01. Based on Felicis/vosk-android-demo.

### SonderKey

![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)

`sonderkey` · <https://github.com/Verisonder/SonderKey> · GPL-3.0 · 8★ · last updated 2026-08-30

HeliBoard/LeanType lineage, so a genuine full keyboard with glide typing, clipboard history and a text expander, plus on-device Parakeet dictation you can type alongside — pause mode leaves the keys usable mid-turn, and spacing/capitalisation can be switched off for code and shell commands. Cloud is LLM-only (Gemini by default, Groq, any OpenAI-compatible) for proofread and translate; STT never goes to the cloud. Ships an Offline build variant with no INTERNET permission in the manifest at all. Its 'floating keyboard' is a draggable IME panel, not an accessibility mic overlay. English-only voice for now.

### TobiBoard

![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![OpenRouter and PayPerQ cloud models](https://img.shields.io/badge/OpenRouter_and_PayPerQ_cloud_models-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)

`tobiboard` · <https://github.com/leinss/TobiBoard> · GPL-3.0 · 3★ · last updated 2026-09-14

HeliBoard fork whose distinguishing move is on-device text rewriting as well as on-device dictation — a local LLM (547 MB to 1.6 GB depending on choice) fixes selected text with no API key, which nothing else here does locally. Installs side by side with HeliBoard. Both features ship OFF; enabling them means a 670 MB speech download plus the text model. Cloud providers are opt-in for larger models, and a custom transcription prompt is available on cloud only — the on-device model takes no prompt. Has its own F-Droid repo at leinss.xyz/TobiBoard/repo. Whether it degrades cloud-to-local automatically is not stated.

### Transcribro

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`transcribro` · <https://github.com/soupslurpr/Transcribro> · ISC · 750★ · last updated 2025-08-29

The security-hardened option: distributed through Accrescent, with the signing-certificate SHA-256 published in the README and cross-posted to Bluesky so the website alone does not have to be trusted. Voice IME plus a speech-to-text service other apps can select. English only, with multi-language tracked in issue #18. Second-most-starred after FUTO Keyboard. Last commit 2025-08-29 — quiet for about a year, so check it is still moving before committing to it.

### TranSlander

![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`translander` · <https://github.com/hatsch/TranSlander> · Apache-2.0 · 11★ · last updated 2026-02-08

The only project that is offline-only AND offers all four input surfaces: voice IME, RecognitionService, RECOGNIZE_SPEECH intent, accessibility floating mic, plus the system navigation-bar accessibility button. Falls back to the clipboard when no text field has focus. Uniquely, it also transcribes voice messages from files — share/open-with, or folder monitoring that watches e.g. Music/Signal and pops a transcription when a new voice note lands. Custom word-correction dictionary for recurring recognition errors. 25 languages with auto-detect. Author states it was largely built with Claude Code.

### Vertick IME

![MiMo-V2.5-ASR](https://img.shields.io/badge/MiMo--V2.5--ASR-6B7280?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)

`vertick-ime` · <https://github.com/BurgerK1ng16/Vertick-IME> · GPL-3.0 · 35★ · last updated 2026-09-01

ANDROID DEVELOPMENT HAS STOPPED — the README's own banner says the developer switched devices, has no Android hardware to test on, and is moving to iOS. Recorded for completeness and as a design reference, not as something to install. Offline Pinyin via Rime-Ice with a precompiled dictionary package so first use does not compile a table on the phone, but ASR is cloud (MiMo-V2.5-ASR) with local punctuation cleanup applied afterwards. Android 15+. Good privacy documentation: dictation and clipboard history both off by default, clipboard capped at 20 items for 24 hours.

### Voice Keyboard

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Groq whisper-large-v3-turbo](https://img.shields.io/badge/Groq_whisper--large--v3--turbo-6B7280?style=flat-square) ![Mistral voxtral-mini](https://img.shields.io/badge/Mistral_voxtral--mini-6B7280?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)

`voice-keyboard` · <https://github.com/rustemar/voice-keyboard> · MIT · 14★ · last updated 2026-09-22

Cloud-only, any OpenAI-compatible Whisper endpoint, Groq free tier by default. Its offline story is durability rather than fallback and the distinction matters: recordings that cannot be transcribed are persisted to disk and resent to the SAME cloud endpoint when a validated connection returns, surviving reboots and app rebuilds. That is engine.fallback = no. Strong keyboard ergonomics for a voice IME — punctuation keys that swallow the preceding space, accelerating backspace, smart spacing, per-recording post-processing toggles, custom vocabulary biasing, multi-language cycling. The panel has no letter keys by design.

### VoiceBoard

![gpt-4o-transcribe](https://img.shields.io/badge/gpt--4o--transcribe-6B7280?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)

`voiceboard` · <https://github.com/jagajaga/voiceboard> · NOASSERTION · 0★ · last updated 2026-09-02

Minimal cloud voice IME — record, stop, insert, powered by gpt-4o-transcribe with gpt-5.5 behind a rephrase button that takes a spoken instruction against a text selection. No local option, no licence file. Included for completeness; `voice-keyboard` (rustemar) does the same job with far more keyboard ergonomics.

### VoiceFlow Keyboard

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Vosk](https://img.shields.io/badge/Vosk-6B7280?style=flat-square) ![GPT Transcribe](https://img.shields.io/badge/GPT_Transcribe-6B7280?style=flat-square) ![Grok](https://img.shields.io/badge/Grok-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square) ![Auto fallback](https://img.shields.io/badge/Auto_fallback-00897B?style=flat-square)

`voiceflow-keyboard` · <https://github.com/yutungh/voiceflow-keyboard-android> · MIT · 1★ · last updated 2026-08-30

Despite one star, this has the cleanest fallback design in the roundup and it is the third project with genuine automatic degradation: pick a cloud provider, and if the phone has no validated internet connection it transcribes offline instead, with a settings control to pre-download the compact fallback model before you need it. Two local tiers — compact Vosk or high-accuracy Parakeet. Captures a full recording rather than live-inserting partials, then optionally cleans it with an LLM. Has a provider-independent local correction layer that guarantees spellings like `npm run signoff` from dictated letters. Debug-signed prototype builds only.

### VoxBoard

![Delegated STT](https://img.shields.io/badge/Delegated_STT-9E9E9E?style=flat-square)

`voxboard` · <https://github.com/Predator04/VoxBoard> · Apache-2.0 · 4★ · last updated 2026-07-08

CAUTION — the catalogue description advertises 'on-device voice input', and that is not what the code does. The README never mentions voice at all, and app/src/main/kotlin/com/voxboard/ime/voice/VoiceInputHandler.kt calls Android's SpeechRecognizer, whose own comment says it 'works offline if the user has downloaded offline speech recognition data' and that replacing it with whisper.cpp is future work. On a stock device that resolves to Google's cloud. Treat it as a FlorisBoard v0.5.2 fork with a normal mic key. The keyboard itself is fine — glide typing, Material You, no INTERNET permission — the voice claim is the problem.

### VoxPen (語墨)

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![gpt-4o-transcribe](https://img.shields.io/badge/gpt--4o--transcribe-6B7280?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)

`voxpen` · <https://github.com/soanseng/voxpen-android> · Apache-2.0 · 8★ · last updated 2026-09-10

Cloud BYOK, Whisper via Groq/OpenAI or any compatible endpoint. Shows the raw transcription and the LLM-refined version side by side in the candidate bar and lets you pick — the only project that surfaces both. Auto Tone detects the foreground app and switches register (casual for messaging, formal for email) on customisable per-app rules. Speak-to-edit rewrites a selection in place. Ten voice commands run locally with no API call. Only two permissions, INTERNET and RECORD_AUDIO. UI is zh-TW/en/ja.

### Speech to Text (WhisperSpeechToText)

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Moonshine](https://img.shields.io/badge/Moonshine-F5A623?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`whisper-speech-to-text` · <https://github.com/Jackfood2/WhisperSpeechToText> · MIT · 0★ · last updated 2026-09-22

THE ONLY MOONSHINE IMPLEMENTATION FOUND ON ANDROID, which alone earns it a place: Settings picks Whisper (multilingual, ~100 languages) or Moonshine v2 (English-only, stated 5-40x faster), each in tiny/base/small/medium. Voice IME plus an accessibility typing bridge and a floating bubble, plus a meeting recorder with a job queue and lock-screen recording. Zero stars but an unusually candid changelog that is the most useful on-device engineering record in the list: a Moonshine activity leak pinned to app context, the model download holding the engine lock and stalling transcription for minutes, engine switching evicting the idle model so two giants are never resident, `onTrimMemory` dropping idle models, and native libs rebuilt with NDK 28 for 16 KB page alignment. Read the changelog before building anything dual-engine.

### Whisper To Input

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![NVIDIA NIM / Riva whisper-large-v3](https://img.shields.io/badge/NVIDIA_NIM_/_Riva_whisper--large--v3-6B7280?style=flat-square) ![self-hosted Whisper ASR Webservice](https://img.shields.io/badge/self--hosted_Whisper_ASR_Webservice-6B7280?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)

`whisper-to-input` · <https://github.com/j3soon/whisper-to-input> · GPL-3.0 · 138★ · last updated 2025-12-21

Voice IME aimed at mixed-language input — English, Chinese, Japanese and Taiwanese, including code-switching mid-sentence. Three interchangeable backends: the OpenAI API, a self-hosted Whisper ASR Webservice, or NVIDIA NIM. The self-hosted option is the interesting one: it is the only project here whose cloud path can point at a box on your own LAN with a documented endpoint shape. No on-device model. Last commit 2025-12-21.

### WhisperBoard

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Deepgram Nova-3](https://img.shields.io/badge/Deepgram_Nova--3-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square) ![Auto fallback](https://img.shields.io/badge/Auto_fallback-00897B?style=flat-square)

`whisperboard` · <https://github.com/david-digitis/WhisperBoard> · GPL-3.0 · 3★ · last updated 2026-05-15

The clearest statement of automatic fallback in the list: an Auto mode that 'uses cloud when available, falls back to local offline'. Cloud is Deepgram Nova-3 over a WebSocket at roughly 300 ms; local Whisper takes 2-5 s. Full HeliBoard underneath, so a real keyboard. Three local models, base/small/small-FR, downloaded in-app; French, English, Dutch, German. No LLM step. The most direct answer if what you want is one keyboard that is fast online and still works on a plane.

### ⭐ Whisperian

![favourite](https://img.shields.io/badge/%E2%98%85_Daniel%27s_pick-E4B400?style=flat-square) ![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Deepgram](https://img.shields.io/badge/Deepgram-6B7280?style=flat-square) ![Groq](https://img.shields.io/badge/Groq-6B7280?style=flat-square) ![custom OpenAI-compatible providers](https://img.shields.io/badge/custom_OpenAI--compatible_providers-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square) ![Cloud](https://img.shields.io/badge/Cloud-0277BD?style=flat-square) ![BYOK](https://img.shields.io/badge/BYOK-6A1B9A?style=flat-square)

`whisperian` · <https://whisperian.app> · Proprietary (closed source) · last updated 2026-09-22

DANIEL'S PICK — the one he actually uses on Android, added 2026-09-22 on his recommendation rather than from the stars list. The only closed-source entry in the roundup: Play Store only, no public repository, so nothing below was read from source and it cannot be starred on GitHub. Free during early access with no sign-up. Covers both form factors at once — a voice IME and an accessibility-driven system-wide floating toolbar that reads the focused field and cursor position, and suppresses itself in password and number fields. Three power options in one app: a built-in free dictation service (Groq) so it works before you configure anything, your own keys for OpenAI, Deepgram and custom OpenAI-compatible providers, or downloadable local models including Parakeet v2 and v3. Configuration is profile-based — each profile pins transcription provider, post-processing provider, model, language, custom prompt and text-replacement rules — which is the 'building blocks, not fixed configurations' design its authors describe, and is closer to Superwhisper's model than to anything else here. Crash-tolerant: audio survives the app being force-killed mid-dictation. Quick Settings tile. Whether it degrades from cloud to local automatically is not documented.

### whisperIME

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`whisperime` · <https://github.com/woheller69/whisperIME> · MIT · 641★ · last updated 2026-08-30

The most-starred voice IME here after Transcribro, and it fills all three Android speech slots at once: IME, RecognitionService, and RECOGNIZE_SPEECH intent. Works as the mic key behind HeliBoard. Two models — a fast English-only one and a slower multilingual one — ~435 MB downloaded from Hugging Face at first run, the only time INTERNET is used. Also translates any supported language to English as a standalone app. Hard 30 s cap per recording. Ships the adb incantation for when the system voice-input list shows only Google/Samsung: `settings put secure voice_recognition_service org.woheller69.whisper/com.whispertflite.WhisperRecognitionService`. Built on vilassn/whisper_android, so TFLite rather than whisper.cpp.

### whisperIME+

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`whisperimeplus` · <https://github.com/woheller69/whisperIMEplus> · GPL-3.0 · 416★ · last updated 2026-09-01

Same author and same three integration points as whisperIME, rebuilt on RTranslator's Whisper ONNX implementation instead of TFLite — the whole point of the fork is speed. Adds two predefinable languages with quick switching. Same 30 s cap, but you can release and re-press to continue while transcription runs. Models come from DocWolle/whisperOnnx. Licence changes to GPL-3.0 because of the RTranslator code. Pick this over whisperIME unless you need the TFLite build.

### WhisperInput

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`whisperinput` · <https://github.com/alex-vt/WhisperInput> · MIT · 114★ · last updated 2024-06-01

Voice IME, voice input panel, and assistant app — the assistant registration is unusual and means long-pressing Home opens dictation. Ships `ggml-tiny.en.bin` bundled in assets rather than downloading, so it works offline from first launch at the cost of accuracy; swapping in a larger or multilingual model means editing assets and rebuilding. Marked experimental by its author. Built from Kõnele components plus whisper.cpp, and the README warns the inherited permission model lags newer Android versions and may fail to record until permissions are set by hand. Last commit 2024-06-01, the second-oldest live entry.

### Whisper Voice Keyboard

![Whisper](https://img.shields.io/badge/Whisper-5436DA?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`whispervoicekeyboard` · <https://github.com/MichaelMcCulloch/WhisperVoiceKeyboard> · MIT · 52★ · last updated 2023-06-10

ABANDONED — last commit 2023-06-10 and the README opens with the author's own TODO saying it predates whisper.cpp and needs rewriting on it. Historical interest only: it is the earliest attempt in this list, Whisper TFLite with a Rust/FFmpeg pipeline, and it explains why every later project uses whisper.cpp or sherpa-onnx instead. Do not install.

### Whispr AI

![Delegated STT](https://img.shields.io/badge/Delegated_STT-9E9E9E?style=flat-square)

`whispr-ai` · <https://github.com/lam3y35/whispr-ai> · NOASSERTION · 0★ · last updated 2026-09-07

CAUTION, same trap as voxboard: the headline says on-device push-to-talk dictation, and that is true of the WINDOWS half (Parakeet TDT 0.6B v2 via sherpa-onnx) but not the Android half. The README states it plainly further down — 'the Android app's speech recognition uses the device's Android speech service (SpeechRecognizer, on-device when available)' — so on a stock phone it is Google's cloud. What Android does get is the shared dictionary correction contract, tested against the same 19 vectors as the desktop build. Worth watching rather than installing: if the Parakeet path is ported to the IME it becomes interesting.

### awesome-voice-typing

`awesome-voice-typing` · <https://github.com/primaprashant/awesome-voice-typing> · MIT · 193★ · last updated 2026-09-22

Not software — a cross-platform curated index of open-source voice-typing tools covering desktop, mobile and CLI, with an auto-updated 30-day trending table and links to the relevant HN threads. Useful as an upstream feed for this roundup: watch its Android section for projects worth adding here. Its own top picks are desktop-first (Handy, VoiceInk, FluidVoice), so it does not answer the Android question directly.

### Local Transcribe

![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`local-transcribe` · <https://github.com/mtib/android-local-transcribe> · NOASSERTION · 2★ · last updated 2026-07-09

Not a keyboard and not an IME — a recorder with live transcription and a share-sheet export. Included because it is the strictest privacy position in the list: the model is bundled inside the APK and the app holds no INTERNET permission at all, so egress is impossible at the OS level. Expect ~1.4 GB installed. Kept out of the matrix; use it as the reference for what bundling costs.

### LocalSTT

![Vosk](https://img.shields.io/badge/Vosk-6B7280?style=flat-square) ![Mozilla DeepSpeech](https://img.shields.io/badge/Mozilla_DeepSpeech-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`localstt` · <https://github.com/ccoreilly/LocalSTT> · GPL-3.0 · 111★ · last updated 2022-01-19

PROOF OF CONCEPT, last commit 2022-01-19, and the reason the `service` category exists: it ships no IME at all, only two RecognitionService implementations and a RECOGNIZE_SPEECH activity, so it supplies on-device recognition to whatever keyboard you already use. Tested against AnySoftKeyboard, Kõnele and SwiftKey. Built for Catalan, with a prebuilt APK carrying Catalan Vosk and DeepSpeech models; swapping languages means replacing the models in assets and rebuilding. Historically important as the pre-Whisper answer to the same problem, and still the cleanest illustration of the service-only pattern.

### Speech Android (soniqo)

![NVIDIA](https://img.shields.io/badge/NVIDIA-76B900?style=flat-square) ![Parakeet-EOU 120M](https://img.shields.io/badge/Parakeet--EOU_120M-6B7280?style=flat-square) ![DeepFilterNet3](https://img.shields.io/badge/DeepFilterNet3-6B7280?style=flat-square) ![Local](https://img.shields.io/badge/Local-2E7D32?style=flat-square)

`speech-android` · <https://github.com/soniqo/speech-android> · Apache-2.0 · 159★ · last updated 2026-09-15

An SDK, not an app — the piece you would build a keyboard on rather than install. Covers the whole local pipeline: VAD, streaming STT, TTS and noise cancellation, all ONNX, no cloud. Interesting for the small end: Parakeet-EOU 120M at 153 MB does streaming STT with end-of-utterance detection, which is the shape a low-latency IME wants, and the demo runs VAD to STT to a small LM to TTS in 1.2 GB of RAM. Has an Apple counterpart (speech-swift) and a Linux/embedded build.

<!-- END notes -->

## Not keyboards

<!-- BEGIN other -->
| Project | Kind | What it is |
| --- | --- | --- |
| [awesome-voice-typing](https://github.com/primaprashant/awesome-voice-typing) | resource | Not software |
| [Local Transcribe](https://github.com/mtib/android-local-transcribe) | app | Not a keyboard and not an IME |
| [LocalSTT](https://github.com/ccoreilly/LocalSTT) | service | PROOF OF CONCEPT, last commit 2022-01-19, and the reason the `service` category exists: it ships no IME at all, only two RecognitionService implementations and a RECOGNIZE_SPEECH activity, so it supplies on-device recognition to whatever keyboard you already use |
| [Speech Android (soniqo)](https://github.com/soniqo/speech-android) | library | An SDK, not an app |
<!-- END other -->

## Where these came from

`whisperian` came in a third way — Daniel's own recommendation. It is the only
closed-source entry and the only one with no GitHub repository, so it cannot be
starred and `refresh_list.py` ignores it. Its `slug` is `null`; the annotation
comes from the Play listing and whisperian.app rather than from source.

The stars list seeded 22 entries. A GitHub sweep on 2026-09-22 — 18 keyword
queries plus six topic queries, 423 unique repositories scanned — found 21 more,
including four with more stars than most of the original list (`whisperime` 641,
`sayboard` 583, `whisperimeplus` 416, `dictate-keyboard` 284).

Rejected after reading, so nobody re-checks them:

| Repo | Why not |
| --- | --- |
| [GravityPoet/ChordVox](https://github.com/GravityPoet/ChordVox) | Calls itself an IME and is genuinely good, but it is Electron for macOS/Windows/Linux. Not Android. |
| [lrq3000/futo-voiceinput-whisper](https://github.com/lrq3000/futo-voiceinput-whisper) | Mirror of `futo-voice-input`, already listed. |
| [maraxman/uttero-legal](https://github.com/maraxman/uttero-legal) | Privacy policy and legal documents only; the app itself is not open source. |
| [niedev/RTranslator](https://github.com/niedev/RTranslator) | Translation app, not an input method — but its Whisper ONNX code is upstream of `whisperimeplus`, so it is in the tooling doc. |
| [vilassn/whisper_android](https://github.com/vilassn/whisper_android) | Reference implementation, not an app. In the tooling doc. |
| Desktop-first dictation tools (Handy, VoiceInk, amical, OmniDictate, …) | Out of scope; `awesome-voice-typing` already indexes them. |

Searches that found nothing new are worth repeating rather than re-inventing:
the productive queries were `android voice keyboard`, `android dictation
keyboard`, `android ime speech`, and the topic pairs `android`+`speech-to-text`
and `whisper`+`android`. Note that `gh search repos` quotes a multi-word string
into a phrase match — pass the words as separate arguments to get an AND, and
keep the search API's 30-requests-per-minute limit in mind, because exceeding it
returns empty result sets rather than an error.

## Maintaining this

```bash
python3 scripts/refresh_list.py           # diff the stars list against the data
python3 scripts/refresh_list.py --write   # refresh ★/dates, stub any new entries
python3 scripts/render_readme.py          # regenerate the tables above
```

`--write` never invents an annotation. A new project lands as a stub with every
judgement set to `unknown` and a `NOT YET ANNOTATED` note; filling it in means
reading the README, and sometimes the source — `voxboard` is in here because its
catalogue description claimed on-device voice input that the code does not do.
