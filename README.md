# Android Voice Keyboard Roundup

Open-source voice input for Android, evaluated against a fixed set of questions
rather than summarised from each project's own pitch.

Seeded from the GitHub stars list
[**android-voice-keyboards**](https://github.com/stars/danielrosehill/lists/android-voice-keyboards),
which stays the intake queue: star a project there, run `scripts/refresh_list.py`,
annotate the stub it creates.

<!-- BEGIN snapshot -->
Data snapshot: **2026-09-22** · 19 keyboards, 3 other entries.
<!-- END snapshot -->

- **`data/projects.json`** is the source of truth. The tables below are generated
  from it — do not hand-edit inside the `<!-- BEGIN … -->` markers.
- **`docs/evaluation-criteria.md`** defines every field. Read it before adding a
  row; the distinctions it draws are the point of this repo.
- **`docs/model-sources.md`** covers where the weights come from, including the
  Hugging Face searches and the working collection.

Legend: ✅ yes · — no · ◐ partial · ? unknown · · not applicable.
**`?` means not stated anywhere I read, not "no".**

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
| [Fluence](https://github.com/raviumeshkulkarni-web/Fluence-Android) | — | — | ✅ |
| [FUTO Keyboard](https://github.com/futo-org/android-keyboard) | — | ✅ | — |
| [FUTO Voice Input](https://github.com/futo-org/voice-input) | ✅ | — | — |
| [Offline Voice Input](https://github.com/notune/android_transcribe_app) | ✅ | — | — |
| [Outspoke](https://github.com/minburg/outspoke) | ✅ | — | — |
| [Parakeeb](https://github.com/surma/parakeeb) | ✅ | — | — |
| [Parakeet Voice](https://github.com/mpnikhil/parakeet-voice-android) | ✅ | — | — |
| [Polished Recognition](https://github.com/georgernstgraf/polished-recognition) | ✅ | — | — |
| [Ramblr](https://github.com/trevornk/ramblr) | ✅ | — | ✅ |
| [SonderKey](https://github.com/Verisonder/SonderKey) | — | ✅ | — |
| [TobiBoard](https://github.com/leinss/TobiBoard) | — | ✅ | — |
| [Transcribro](https://github.com/soupslurpr/Transcribro) | ✅ | — | — |
| [TranSlander](https://github.com/hatsch/TranSlander) | ✅ | — | ✅ |
| [Voice Keyboard](https://github.com/rustemar/voice-keyboard) | ✅ | — | — |
| [VoxBoard](https://github.com/Predator04/VoxBoard) | — | ✅ | — |
| [VoxPen (語墨)](https://github.com/soanseng/voxpen-android) | ✅ | — | — |
| [WhisperBoard](https://github.com/david-digitis/WhisperBoard) | — | ✅ | — |
| [Whisper Voice Keyboard](https://github.com/MichaelMcCulloch/WhisperVoiceKeyboard) | ✅ | — | — |
<!-- END capability -->

## Recognition

`Auto fallback` is strictly **automatic** cloud-to-local degradation. A manual
mode switch is not fallback, and neither is an offline queue that retries the
same cloud endpoint later.

<!-- BEGIN recognition -->
| Project | Local | Cloud | Auto fallback | Whisper | NVIDIA | Moonshine | Other ASR |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| [说点啥 (BiBi Keyboard)](https://github.com/BryceWG/BiBi-Keyboard) | ✅ | ✅ | ✅ | ? | ✅ | — | SenseVoice, FunASR Nano, Qwen3-ASR, FireRedASR, X-ASR |
| [Fluence](https://github.com/raviumeshkulkarni-web/Fluence-Android) | ✅ | ✅ | — | ✅ | — | — | SenseVoice-Small (offline), Groq whisper-large-v3 (cloud) |
| [FUTO Keyboard](https://github.com/futo-org/android-keyboard) | ✅ | — | — | ✅ | — | — | — |
| [FUTO Voice Input](https://github.com/futo-org/voice-input) | ✅ | — | — | ✅ | — | — | — |
| [Offline Voice Input](https://github.com/notune/android_transcribe_app) | ✅ | — | — | ? | ✅ | — | — |
| [Outspoke](https://github.com/minburg/outspoke) | ✅ | — | — | — | ✅ | — | Silero VAD v4 |
| [Parakeeb](https://github.com/surma/parakeeb) | ✅ | — | — | — | ✅ | — | — |
| [Parakeet Voice](https://github.com/mpnikhil/parakeet-voice-android) | ✅ | — | — | — | ✅ | — | Silero VAD |
| [Polished Recognition](https://github.com/georgernstgraf/polished-recognition) | — | ✅ | — | ✅ | — | — | — |
| [Ramblr](https://github.com/trevornk/ramblr) | ✅ | ✅ | ◐ | ✅ | ✅ | — | Parakeet TDT 0.6B v3, Parakeet Unified 0.6B, Canary 180M Flash, Parakeet 110M, gpt-4o-transcribe, Gemini |
| [SonderKey](https://github.com/Verisonder/SonderKey) | ✅ | — | — | — | ✅ | — | — |
| [TobiBoard](https://github.com/leinss/TobiBoard) | ✅ | ✅ | ? | ? | ✅ | — | OpenRouter and PayPerQ cloud models |
| [Transcribro](https://github.com/soupslurpr/Transcribro) | ✅ | — | — | ✅ | — | — | Silero VAD |
| [TranSlander](https://github.com/hatsch/TranSlander) | ✅ | — | — | — | ✅ | — | — |
| [Voice Keyboard](https://github.com/rustemar/voice-keyboard) | — | ✅ | — | ✅ | — | — | Groq whisper-large-v3-turbo (default), Mistral voxtral-mini |
| [VoxBoard](https://github.com/Predator04/VoxBoard) | — | — | — | — | — | — | — |
| [VoxPen (語墨)](https://github.com/soanseng/voxpen-android) | — | ✅ | — | ✅ | — | — | gpt-4o-transcribe |
| [WhisperBoard](https://github.com/david-digitis/WhisperBoard) | ✅ | ✅ | ✅ | ✅ | — | — | Deepgram Nova-3 (cloud) |
| [Whisper Voice Keyboard](https://github.com/MichaelMcCulloch/WhisperVoiceKeyboard) | ✅ | — | — | ✅ | — | — | — |
<!-- END recognition -->

## Post-processing and metadata

<!-- BEGIN postprocess -->
| Project | LLM cleanup (local) | LLM cleanup (cloud) | Runtime | Licence | ★ | Updated |
| --- | :---: | :---: | --- | --- | ---: | --- |
| [说点啥 (BiBi Keyboard)](https://github.com/BryceWG/BiBi-Keyboard) | ? | ✅ | unknown | Apache-2.0 | 803 | 2026-09-20 |
| [Fluence](https://github.com/raviumeshkulkarni-web/Fluence-Android) | — | ✅ | sherpa-onnx | AGPL-3.0 | 15 | 2026-09-21 |
| [FUTO Keyboard](https://github.com/futo-org/android-keyboard) | — | — | whisper.cpp | FUTO Source First 1.1 (not OSI-approved) | 3238 | 2026-09-14 |
| [FUTO Voice Input](https://github.com/futo-org/voice-input) | — | — | whisper.cpp | FUTO Source First 1.0 (not OSI-approved) | 327 | 2025-09-16 |
| [Offline Voice Input](https://github.com/notune/android_transcribe_app) | — | — | transcribe.cpp (ggml) via a Rust core | MIT | 302 | 2026-07-19 |
| [Outspoke](https://github.com/minburg/outspoke) | — | — | onnxruntime | GPL-3.0 | 85 | 2026-08-29 |
| [Parakeeb](https://github.com/surma/parakeeb) | — | — | transcribe-rs / onnxruntime | MIT | 6 | 2026-07-18 |
| [Parakeet Voice](https://github.com/mpnikhil/parakeet-voice-android) | — | — | sherpa-onnx | NOASSERTION | 4 | 2026-04-20 |
| [Polished Recognition](https://github.com/georgernstgraf/polished-recognition) | ✅ | ✅ | n/a (cloud) | MIT | 7 | 2026-09-21 |
| [Ramblr](https://github.com/trevornk/ramblr) | ✅ | ✅ | sherpa-onnx + llama.cpp | GPL-3.0 | 51 | 2026-09-22 |
| [SonderKey](https://github.com/Verisonder/SonderKey) | — | ✅ | sherpa-onnx | GPL-3.0 | 8 | 2026-08-30 |
| [TobiBoard](https://github.com/leinss/TobiBoard) | ✅ | ✅ | sherpa-onnx | GPL-3.0 | 3 | 2026-09-14 |
| [Transcribro](https://github.com/soupslurpr/Transcribro) | — | — | whisper.cpp | ISC | 750 | 2025-08-29 |
| [TranSlander](https://github.com/hatsch/TranSlander) | — | — | sherpa-onnx | Apache-2.0 | 11 | 2026-02-08 |
| [Voice Keyboard](https://github.com/rustemar/voice-keyboard) | — | ✅ | n/a (cloud) | MIT | 14 | 2026-09-22 |
| [VoxBoard](https://github.com/Predator04/VoxBoard) | — | — | n/a (delegated) | Apache-2.0 | 4 | 2026-07-08 |
| [VoxPen (語墨)](https://github.com/soanseng/voxpen-android) | — | ✅ | n/a (cloud) | Apache-2.0 | 8 | 2026-09-10 |
| [WhisperBoard](https://github.com/david-digitis/WhisperBoard) | — | — | whisper.cpp v1.8.3 | GPL-3.0 | 3 | 2026-05-15 |
| [Whisper Voice Keyboard](https://github.com/MichaelMcCulloch/WhisperVoiceKeyboard) | — | — | TFLite + Rust/FFmpeg | MIT | 52 | 2023-06-10 |
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
- **Automatic cloud-to-local fallback is rare** — `whisperboard` states it
  plainly, `bibi-keyboard` implements it as a resident local engine behind a
  primary/backup pair, and `tobiboard` has both halves but does not say whether
  it bridges them. Everything else makes you choose a mode up front.
- **Whisper is losing to NVIDIA Parakeet on-device.** Whisper still dominates
  the cloud rows because that is what Groq and OpenAI serve; the local rows are
  overwhelmingly Parakeet TDT 0.6B v3 via sherpa-onnx. Note that v3 is the
  *default*, not the best choice for English dictation — v2 is, in practice —
  and only `ramblr` and `parakeet-voice-android` give you the option. See
  [`docs/model-sources.md`](docs/model-sources.md), where the decisive variable
  turns out to be decoder architecture and context-buffer behaviour rather than
  model family.
- **Moonshine appears nowhere.** Not in any project in the list, as of
  2026-09-22.
- **Gboard cannot be redirected.** Three separate projects document it
  independently: Gboard's mic is hardcoded to Google's voice typing and will not
  delegate to a third-party voice IME. Samsung's keyboard is the same. Any
  project promising to replace Gboard's mic means either a `RecognitionService`
  (which Gboard also ignores) or switching keyboards.

## Per-project notes

<!-- BEGIN notes -->
### 说点啥 (BiBi Keyboard)

`bibi-keyboard` · <https://github.com/BryceWG/BiBi-Keyboard> · Apache-2.0 · 803★ · last commit 2026-09-20

The most feature-complete of the set. 18 ASR providers, 12 cloud and 6 local, with an explicit primary/backup arrangement and a resident local engine as the last resort (主备与本地兜底) — the clearest automatic cloud-to-local fallback in the list. The floating ball (悬浮球) is the accessibility-overlay kind and works over any other IME. full_keyboard is partial: the layout is a configurable key pool and AI edit panel, not a general alphabet keyboard. Also exposes itself to third-party apps over SpeechRecognizer and AIDL, and can drive Fcitx/Rime forks. Has a paid Pro tier on Play; the repo is the free app.

### Fluence

`fluence` · <https://github.com/raviumeshkulkarni-web/Fluence-Android> · AGPL-3.0 · 15★ · last commit 2026-09-21

Deliberately not an IME at all — the pitch is that you keep your own keyboard and a glassmorphic bubble follows the cursor. Cloud and offline are a toggle, not a fallback chain. Agent Mode (Llama 3.3 70B via Groq) takes spoken commands like 'delete the last two sentences' and edits in place, which nothing else here does.

### FUTO Keyboard

`futo-keyboard` · <https://github.com/futo-org/android-keyboard> · FUTO Source First 1.1 (not OSI-approved) · 3238★ · last commit 2026-09-14

By far the most-starred and the most mature keyboard here — a LatinIME fork with FUTO Voice Input built in. Voice is a mode inside the keyboard rather than a separate voice IME, so it consumes the voice-IME slot rather than filling it; you can force it to delegate to the standalone app by disabling built-in voice input. Source-available, not open source: the licence is FUTO Source First 1.1 and PRs need a CLA. This repo is a mirror of an internal GitLab.

### FUTO Voice Input

`futo-voice-input` · <https://github.com/futo-org/voice-input> · FUTO Source First 1.0 (not OSI-approved) · 327★ · last commit 2025-09-16

The reference implementation of the voice-IME pattern, and the source of the keyboard-compatibility table everyone else repeats. Registers both as a voice-subtype IME and as a RECOGNIZE_SPEECH intent handler; the intent path opens a centred floating window, which is a system dialog and not an accessibility overlay. Does NOT implement SpeechRecognizer. Development has largely moved to FUTO Keyboard — last touched 2025-09-16, the only stale entry besides whispervoicekeyboard. 17 languages, capped at Whisper languages with >1000 training hours.

### Offline Voice Input

`offline-voice-input` · <https://github.com/notune/android_transcribe_app> · MIT · 302★ · last commit 2026-07-19

The best-integrated of the pure on-device ones: it plugs into Android speech in all three ways at once — RECOGNIZE_SPEECH popup, RecognitionService, and a voice IME — so it works from SwiftKey's mic, from website voice search, and from the keyboard switcher. The README's keyboard-by-keyboard notes were verified against each keyboard's source by the author. Also does live subtitles over screen capture. On Play as well as GitHub. Supports loading custom speech models.

### Outspoke

`outspoke` · <https://github.com/minburg/outspoke> · GPL-3.0 · 85★ · last commit 2026-08-29

The cleanest single-purpose voice IME: Parakeet only, offline only, no LLM, no cloud path to misconfigure. Progressive partial results while you speak, hold-to-talk or tap-to-toggle, and a microphone-calibration screen that ranks every mic on the device by capture fidelity and picks the best — nothing else in the list does that. Architecture is built around a swappable SpeechEngine interface, so a second model backend is one class away. Needs Android 11+, 4 GB RAM, ~750 MB storage.

### Parakeeb

`parakeeb` · <https://github.com/surma/parakeeb> · MIT · 6★ · last commit 2026-07-18

A fork of offline-voice-input carrying a mostly unedited upstream README — the badges and package name still point at notune's app, so read it as inheriting that project's behaviour rather than describing its own. Its actual contribution is ONNX Runtime execution-provider tuning: the EP list and graph-optimisation level are settable at runtime over adb setprop without a rebuild, and the author measured that NNAPI/Darwinn on a Pixel 8a is slower than XNNPACK for the int8 Parakeet model. Worth reading for that finding even if you run something else.

### Parakeet Voice

`parakeet-voice-android` · <https://github.com/mpnikhil/parakeet-voice-android> · NOASSERTION · 4★ · last commit 2026-04-20

Small and direct. Its selling point is the RecognitionService implementation: set it as the system default voice input and Gboard's own mic button transcribes locally, keeping Gboard for typing. English only — it ships Parakeet TDT v2, and the README names the one-line change to swap in multilingual v3 at ~3% WER cost on English. Do not take that as an upgrade: v2 is the better English model in practice (see docs/model-sources.md), so shipping it is a point in this project's favour rather than a limitation. arm64-v8a only. Offers the best verification trick in the list: turn on airplane mode and dictate.

### Polished Recognition

`polished-recognition` · <https://github.com/georgernstgraf/polished-recognition> · MIT · 7★ · last commit 2026-09-21

Cloud STT only — the local option is for the polish step (Ollama or LM Studio over the OpenAI contract), not for recognition, so a claim of 'or run a local model' should not be read as on-device ASR. 18 provider presets and dynamic model lists off each provider's /v1/models. Recording starts the instant you switch to the keyboard, and survives switching away to your typing keyboard and back. Raw mode skips the LLM. On F-Droid; the Play build is closed testing and needs 12 continuously opted-in testers.

### Ramblr

`ramblr` · <https://github.com/trevornk/ramblr> · GPL-3.0 · 51★ · last commit 2026-09-22

The most thoroughly engineered project in the list and the only one shipping ADRs and field latency data. Five independent ways to trigger dictation (floating ring, voice IME, accessibility button / volume-hold, QS tile, text-selection menu), of which the IME and the selection menu need no accessibility grant. Transcription and cleanup are chosen independently, so local STT plus cloud cleanup is a normal setup. fallback is 'partial' on purpose: the ordered waterfall with on-device as the floor applies to CLEANUP only — transcription is a single configured provider with no automatic degradation. Chain capped at 8 s, tuned from 34 days of p99 data. Four local ASR models and two local cleanup models, all downloaded on demand, none bundled.

### SonderKey

`sonderkey` · <https://github.com/Verisonder/SonderKey> · GPL-3.0 · 8★ · last commit 2026-08-30

HeliBoard/LeanType lineage, so a genuine full keyboard with glide typing, clipboard history and a text expander, plus on-device Parakeet dictation you can type alongside — pause mode leaves the keys usable mid-turn, and spacing/capitalisation can be switched off for code and shell commands. Cloud is LLM-only (Gemini by default, Groq, any OpenAI-compatible) for proofread and translate; STT never goes to the cloud. Ships an Offline build variant with no INTERNET permission in the manifest at all. Its 'floating keyboard' is a draggable IME panel, not an accessibility mic overlay. English-only voice for now.

### TobiBoard

`tobiboard` · <https://github.com/leinss/TobiBoard> · GPL-3.0 · 3★ · last commit 2026-09-14

HeliBoard fork whose distinguishing move is on-device text rewriting as well as on-device dictation — a local LLM (547 MB to 1.6 GB depending on choice) fixes selected text with no API key, which nothing else here does locally. Installs side by side with HeliBoard. Both features ship OFF; enabling them means a 670 MB speech download plus the text model. Cloud providers are opt-in for larger models, and a custom transcription prompt is available on cloud only — the on-device model takes no prompt. Has its own F-Droid repo at leinss.xyz/TobiBoard/repo. Whether it degrades cloud-to-local automatically is not stated.

### Transcribro

`transcribro` · <https://github.com/soupslurpr/Transcribro> · ISC · 750★ · last commit 2025-08-29

The security-hardened option: distributed through Accrescent, with the signing-certificate SHA-256 published in the README and cross-posted to Bluesky so the website alone does not have to be trusted. Voice IME plus a speech-to-text service other apps can select. English only, with multi-language tracked in issue #18. Second-most-starred after FUTO Keyboard. Last commit 2025-08-29 — quiet for about a year, so check it is still moving before committing to it.

### TranSlander

`translander` · <https://github.com/hatsch/TranSlander> · Apache-2.0 · 11★ · last commit 2026-02-08

The only project that is offline-only AND offers all four input surfaces: voice IME, RecognitionService, RECOGNIZE_SPEECH intent, accessibility floating mic, plus the system navigation-bar accessibility button. Falls back to the clipboard when no text field has focus. Uniquely, it also transcribes voice messages from files — share/open-with, or folder monitoring that watches e.g. Music/Signal and pops a transcription when a new voice note lands. Custom word-correction dictionary for recurring recognition errors. 25 languages with auto-detect. Author states it was largely built with Claude Code.

### Voice Keyboard

`voice-keyboard` · <https://github.com/rustemar/voice-keyboard> · MIT · 14★ · last commit 2026-09-22

Cloud-only, any OpenAI-compatible Whisper endpoint, Groq free tier by default. Its offline story is durability rather than fallback and the distinction matters: recordings that cannot be transcribed are persisted to disk and resent to the SAME cloud endpoint when a validated connection returns, surviving reboots and app rebuilds. That is engine.fallback = no. Strong keyboard ergonomics for a voice IME — punctuation keys that swallow the preceding space, accelerating backspace, smart spacing, per-recording post-processing toggles, custom vocabulary biasing, multi-language cycling. The panel has no letter keys by design.

### VoxBoard

`voxboard` · <https://github.com/Predator04/VoxBoard> · Apache-2.0 · 4★ · last commit 2026-07-08

CAUTION — the catalogue description advertises 'on-device voice input', and that is not what the code does. The README never mentions voice at all, and app/src/main/kotlin/com/voxboard/ime/voice/VoiceInputHandler.kt calls Android's SpeechRecognizer, whose own comment says it 'works offline if the user has downloaded offline speech recognition data' and that replacing it with whisper.cpp is future work. On a stock device that resolves to Google's cloud. Treat it as a FlorisBoard v0.5.2 fork with a normal mic key. The keyboard itself is fine — glide typing, Material You, no INTERNET permission — the voice claim is the problem.

### VoxPen (語墨)

`voxpen` · <https://github.com/soanseng/voxpen-android> · Apache-2.0 · 8★ · last commit 2026-09-10

Cloud BYOK, Whisper via Groq/OpenAI or any compatible endpoint. Shows the raw transcription and the LLM-refined version side by side in the candidate bar and lets you pick — the only project that surfaces both. Auto Tone detects the foreground app and switches register (casual for messaging, formal for email) on customisable per-app rules. Speak-to-edit rewrites a selection in place. Ten voice commands run locally with no API call. Only two permissions, INTERNET and RECORD_AUDIO. UI is zh-TW/en/ja.

### WhisperBoard

`whisperboard` · <https://github.com/david-digitis/WhisperBoard> · GPL-3.0 · 3★ · last commit 2026-05-15

The clearest statement of automatic fallback in the list: an Auto mode that 'uses cloud when available, falls back to local offline'. Cloud is Deepgram Nova-3 over a WebSocket at roughly 300 ms; local Whisper takes 2-5 s. Full HeliBoard underneath, so a real keyboard. Three local models, base/small/small-FR, downloaded in-app; French, English, Dutch, German. No LLM step. The most direct answer if what you want is one keyboard that is fast online and still works on a plane.

### Whisper Voice Keyboard

`whispervoicekeyboard` · <https://github.com/MichaelMcCulloch/WhisperVoiceKeyboard> · MIT · 52★ · last commit 2023-06-10

ABANDONED — last commit 2023-06-10 and the README opens with the author's own TODO saying it predates whisper.cpp and needs rewriting on it. Historical interest only: it is the earliest attempt in this list, Whisper TFLite with a Rust/FFmpeg pipeline, and it explains why every later project uses whisper.cpp or sherpa-onnx instead. Do not install.

### awesome-voice-typing

`awesome-voice-typing` · <https://github.com/primaprashant/awesome-voice-typing> · MIT · 193★ · last commit 2026-09-22

Not software — a cross-platform curated index of open-source voice-typing tools covering desktop, mobile and CLI, with an auto-updated 30-day trending table and links to the relevant HN threads. Useful as an upstream feed for this roundup: watch its Android section for projects worth adding here. Its own top picks are desktop-first (Handy, VoiceInk, FluidVoice), so it does not answer the Android question directly.

### Local Transcribe

`local-transcribe` · <https://github.com/mtib/android-local-transcribe> · NOASSERTION · 2★ · last commit 2026-07-09

Not a keyboard and not an IME — a recorder with live transcription and a share-sheet export. Included because it is the strictest privacy position in the list: the model is bundled inside the APK and the app holds no INTERNET permission at all, so egress is impossible at the OS level. Expect ~1.4 GB installed. Kept out of the matrix; use it as the reference for what bundling costs.

### Speech Android (soniqo)

`speech-android` · <https://github.com/soniqo/speech-android> · Apache-2.0 · 159★ · last commit 2026-09-15

An SDK, not an app — the piece you would build a keyboard on rather than install. Covers the whole local pipeline: VAD, streaming STT, TTS and noise cancellation, all ONNX, no cloud. Interesting for the small end: Parakeet-EOU 120M at 153 MB does streaming STT with end-of-utterance detection, which is the shape a low-latency IME wants, and the demo runs VAD to STT to a small LM to TTS in 1.2 GB of RAM. Has an Apple counterpart (speech-swift) and a Linux/embedded build.

<!-- END notes -->

## Not keyboards

<!-- BEGIN other -->
| Project | Kind | What it is |
| --- | --- | --- |
| [awesome-voice-typing](https://github.com/primaprashant/awesome-voice-typing) | resource | Not software |
| [Local Transcribe](https://github.com/mtib/android-local-transcribe) | app | Not a keyboard and not an IME |
| [Speech Android (soniqo)](https://github.com/soniqo/speech-android) | library | An SDK, not an app |
<!-- END other -->

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
