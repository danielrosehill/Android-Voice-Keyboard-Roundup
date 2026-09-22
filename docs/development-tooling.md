# Development tooling

The inference engines, SDKs and platform APIs the projects in
`data/projects.json` actually build on. Compiled from their READMEs and credits
sections, 2026-09-22.

The useful thing about reading it this way: **there are only about five real
choices here**, and picking one determines most of what the resulting keyboard
can do. Forty-odd projects, five engines.

## Inference engines

Where the ASR model actually runs.

| Engine | Repo | Models it can run | Used by |
| --- | --- | --- | --- |
| **sherpa-onnx** | [k2-fsa/sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) (~14.9k★) | Parakeet TDT, Canary, Nemotron, SenseVoice, Zipformer, Paraformer, Silero VAD, plus TTS and diarisation | `outspoke`, `tobiboard`, `sonderkey`, `translander`, `parakeet-voice-android`, `orbie`, `ramblr`, `local-transcribe`, `fluence`, `dictus`, `feelime`, `voiceflow-keyboard`, `whispr-ai` (Windows half) |
| **whisper.cpp** | [ggerganov/whisper.cpp](https://github.com/ggerganov/whisper.cpp) | Whisper (ggml) | `transcribro`, `whisperboard`, `futo-voice-input`, `futo-keyboard`, `kaiboard`, `whisperinput`, `dictus`, `whisper-speech-to-text` |
| **ONNX Runtime** | [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime), Rust bindings [pykeio/ort](https://github.com/pykeio/ort) | anything exported to ONNX | `outspoke` (direct), `whisperimeplus`, `nemotron-voice-keyboard`, and underneath sherpa-onnx everywhere |
| **transcribe.cpp / transcribe-rs** | [handy-computer/transcribe.cpp](https://github.com/handy-computer/transcribe.cpp), [cjpais/transcribe-rs](https://github.com/cjpais/transcribe-rs) | Parakeet, Whisper (GGUF) | `offline-voice-input`, `parakeeb` |
| **TensorFlow Lite / LiteRT** | — | Whisper TFLite | `whisperime`, `whispervoicekeyboard` (abandoned) |
| **Vosk** | [alphacephei/vosk-api](https://github.com/alphacephei/vosk-api) | Kaldi models, tens of MB, streaming | `sayboard`, `localstt`, `voiceflow-keyboard` (compact fallback tier) |
| **llama.cpp** | [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) | on-device LLM for transcript cleanup, not ASR | `ramblr`, `tobiboard` |
| **librime** | [rime/librime](https://github.com/rime/librime) | not ASR — Chinese input engine alongside it | `feelime`, `vertick-ime` |

**sherpa-onnx has effectively won.** It is the default answer for anything
NVIDIA-shaped, whisper.cpp holds the Whisper-shaped work, and everything else is
either legacy (TFLite), niche (Vosk, where tiny models and rare languages still
matter), or a different problem (llama.cpp for cleanup).

Consequences worth knowing before you pick:

- sherpa-onnx ships as a prebuilt AAR (~54 MB) that projects fetch rather than
  vendor — `tobiboard` has `make fetch-native-libs`, `orbie` has
  `fetch-sherpa-aar.sh`, `feelime` has `setup-assets.sh`, all SHA-256 verified.
  A clone alone will not build.
- ONNX Runtime execution providers are tunable and the defaults are not obviously
  right. `parakeeb` exposes the EP list over `adb setprop` and found that
  NNAPI/Darwinn on a Pixel 8a is *slower* than XNNPACK for int8 Parakeet. Start
  at `xnnpack,cpu`.
- Two engines resident at once will get you killed by the OS.
  `whisper-speech-to-text` documents evicting the idle engine on switch and
  dropping idle models on `onTrimMemory`.
- 16 KB page alignment (NDK 28) is now required; older native libs fail on newer
  devices. Same source.

## SDKs and helper libraries

| Library | Repo | What it gives you |
| --- | --- | --- |
| **Silero VAD** | [snakers4/silero-vad](https://github.com/snakers4/silero-vad) | ~2 MB voice-activity detection; endpointing and auto-stop. Near-universal here. |
| **android-vad** | [gkonovalov/android-vad](https://github.com/gkonovalov/android-vad) | WebRTC + Silero VAD packaged for Android. `futo-voice-input`, `whisperime`. |
| **speechutils** | [Kaljurand/speechutils](https://github.com/Kaljurand/speechutils) | Kõnele's audio-capture and recognition plumbing. Reused by `whisperinput`, `localstt`. Its permission model predates recent Android and is a known source of record failures. |
| **soniqo/speech-core** | [soniqo/speech-core](https://github.com/soniqo/speech-core) | C++17 VAD + streaming STT + TTS + DeepFilterNet3 denoise pipeline; the engine under `speech-android`. |
| **soniqo/speech-android** | [soniqo/speech-android](https://github.com/soniqo/speech-android) | The Android SDK wrapper. In `data/projects.json` as a `library`. |
| **whisper_android** | [vilassn/whisper_android](https://github.com/vilassn/whisper_android) (~692★) | Whisper + TFLite reference implementation for Android. `whisperime` is built on it. |
| **RTranslator** | [niedev/RTranslator](https://github.com/niedev/RTranslator) (~10.4k★) | A translation app, but its Whisper ONNX implementation is lifted by `whisperimeplus`. |
| **parakeet-rs** | [altunenes/parakeet-rs](https://github.com/altunenes/parakeet-rs) | Rust Parakeet/Nemotron inference. `nemotron-voice-keyboard`. |
| **cactus** | [cactus-compute/cactus](https://github.com/cactus-compute/cactus) (~6k★) | General mobile/edge inference runtime. Not used by anything here yet — a plausible future base. |
| **Opencc4j** | [houbb/opencc4j](https://github.com/houbb/opencc4j) | Simplified/traditional Chinese conversion. Both woheller69 apps. |

## The Android platform APIs

The part that decides form factor. Four integration points, and most projects
implement one or two when they could implement all four.

| API | What it gets you | Accessibility grant? |
| --- | --- | --- |
| `InputMethodService` | Your own keyboard or voice panel, inserting via `InputConnection`. The only path that works in password fields and in apps that block accessibility. | No |
| `RecognitionService` | Other apps' `SpeechRecognizer` calls route to you. Set as system default voice input. **Needs `QUERY_ALL_PACKAGES` to work properly** — an Android bug, documented in `sayboard` via [K6nele-service#9](https://github.com/Kaljurand/K6nele-service/issues/9). | No |
| `RECOGNIZE_SPEECH` intent | Apps and some keyboards (SwiftKey, web voice search) open your panel as a system dialog. | No |
| Accessibility API | A floating mic over any app, inserting at the cursor in any text field. The only keyboard-independent path. | Yes |

Three projects implement all of the first three at once — `offline-voice-input`,
`whisperime`, `whisperimeplus` — and `translander` adds the fourth. That is the
completeness bar; most of the list clears one hurdle.

Two operational notes that cost people time:

- **If your app does not appear in the system voice-input list**, Android is
  showing a hardcoded list. `whisperime` publishes the fix:
  `adb shell settings put secure voice_recognition_service <pkg>/<service>`.
- **`WRITE_SECURE_SETTINGS` via adb** lets an app rebind accessibility shortcuts
  in-app, sidestepping the `INVISIBLE_TOGGLE` trap where turning off the last
  bound shortcut disables the service itself. Documented by `ramblr`.

## Base keyboards people fork

Nobody writing a full keyboard starts from nothing.

| Base | Forked by |
| --- | --- |
| [HeliBoard](https://github.com/Helium314/HeliBoard) | `sonderkey` (via LeanType), `tobiboard`, `whisperboard`, `deskdrop` |
| [FlorisBoard](https://github.com/florisboard/florisboard) | `voxboard`, `dictate-keyboard` |
| AOSP LatinIME | `futo-keyboard`, and HeliBoard/OpenBoard upstream of the rest |
| Gboard (patched binary) | `pixelboard` — not a source fork |

Choosing the base is choosing the licence: HeliBoard forks are GPL-3.0,
FlorisBoard forks Apache-2.0, and `futo-keyboard` is source-available under a
non-OSI licence with a CLA.

## One ecosystem risk worth flagging

Both woheller69 apps carry this notice, and it applies to every sideloaded and
F-Droid app in this roundup, not just theirs:

> Google has announced that, starting in 2026/2027, all apps on certified
> Android devices will require the developer to submit personal identity details
> directly to Google. Since the developers of this app do not agree to this
> requirement, this app will no longer work on certified Android devices after
> that time.

Recorded as a quoted claim from the project, not as verified policy analysis.
Most of what is evaluated here is distributed outside Play, so if it holds as
described it affects the majority of the list at once.
