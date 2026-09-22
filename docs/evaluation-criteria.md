# Evaluation criteria

Definitions for every field in `data/projects.json`. Read this before annotating a
new project, so the same word means the same thing across rows.

Verified against project READMEs on **2026-09-22**.

## Value vocabulary

Every boolean-shaped field takes one of four strings. Never use `true`/`false`.

| Value | Meaning |
| --- | --- |
| `yes` | The project's own documentation or source states it plainly. |
| `no` | The documentation states it does not, or the architecture rules it out. |
| `partial` | It does a restricted version of the thing — always explain in `notes`. |
| `unknown` | Not stated anywhere read so far. Not the same as `no`. |

`unknown` is the correct answer far more often than it feels like. Do not infer
`no` from silence, and do not infer `yes` from a marketing line — see
`voxboard` in `data/projects.json` for a case where the catalogue description
claimed on-device voice input and the source turned out to delegate to Android's
`SpeechRecognizer`.

## `category`

What kind of thing this is. Only `keyboard` rows appear in the main matrix.

| Value | Meaning |
| --- | --- |
| `keyboard` | Ships an Android IME, or a floating-overlay dictation app. In the matrix. |
| `service` | Ships no IME — only a `RecognitionService` and/or a `RECOGNIZE_SPEECH` handler, supplying recognition to whatever keyboard you already use. |
| `app` | A dictation/transcription app with no text-injection path into other apps. |
| `library` | An SDK for building one of the above. |
| `resource` | A list, index or reference. Not software you install. |

## `form` — how you reach the microphone

Three independent capabilities. A project can have all three.

### `form.voice_ime`

Registers an `InputMethodService` that is **voice-only** — a mic panel with no
alphabet, reached from the keyboard switcher. Android's `voice` IME subtype also
makes it the target of the mic key on keyboards that delegate (HeliBoard,
FlorisBoard, OpenBoard, Fossify, AnySoftKeyboard, the AOSP keyboard).

`no` when voice is a mic button *inside* a full keyboard — that is
`form.full_keyboard`, not this.

### `form.full_keyboard`

Can replace your everyday keyboard: letters, symbols, autocorrect, glide typing.
In practice every `yes` here is a fork of HeliBoard, FlorisBoard or AOSP LatinIME.

### `form.floating_button`

A draggable on-screen mic overlay that works in any app, inserting text through
the Android Accessibility API rather than through an IME. Requires
`SYSTEM_ALERT_WINDOW` plus an accessibility-service grant.

`no` for a floating window that Android itself opens in response to a
`RECOGNIZE_SPEECH` intent — that is a system dialog, not a persistent button, and
it needs no accessibility grant. Also `no` for a "floating keyboard" that merely
undocks the IME panel.

## `engine` — where recognition runs

### `engine.local`

Speech-to-text runs on the device. A one-time model download over the network
still counts as `yes`; what matters is that no audio leaves the phone at
dictation time.

`no` when the app calls Android's `SpeechRecognizer` and lets the system decide —
that is delegation, not on-device recognition, and on a stock device it resolves
to Google's cloud. Record it as `engine.system_delegated: yes` instead.

### `engine.cloud`

Sends audio to a remote STT API. BYOK counts. LLM post-processing in the cloud
does **not** count here — that is `llm_postprocess.cloud`.

### `engine.fallback`

**Automatic** degradation from cloud STT to local STT when the network or the
provider fails. The user must not have to change a setting.

`no` for a manual mode switch, and `no` for an offline queue that stores audio
and retries the same cloud endpoint later — that is durability, not fallback.
Where a project chains fallbacks for text cleanup but not for transcription,
mark `partial` and say so in `notes`.

## `models` — which ASR model

Recorded per the three families asked for, plus a free list.

| Field | Counts when |
| --- | --- |
| `whisper` | OpenAI Whisper in any packaging — whisper.cpp, TFLite, Groq/OpenAI/Mistral `whisper-*` endpoints. |
| `moonshine` | Useful Sensors Moonshine. |
| `nvidia` | An NVIDIA NeMo model: Parakeet TDT (any size/version), Canary, Nemotron streaming. |
| `other` | Free-text list — `Deepgram Nova-3`, `SenseVoice`, `FunASR`, `Qwen3-ASR`, `FireRedASR`, `gpt-4o-transcribe`, `Gemini`, … |

`runtime` names the inference stack where stated: `sherpa-onnx`, `whisper.cpp`,
`onnxruntime`, `transcribe.cpp`, `TFLite`.

## `llm_postprocess`

Whether dictated text is passed through a language model to strip fillers, fix
punctuation, translate or restyle. `local` and `cloud` are tracked separately
because several projects do local STT and cloud cleanup, or the reverse.

## Metadata

`stars`, `updated`, `license`, `lang` are snapshots from the GitHub API, stamped
with `snapshot_date` at the top of `data/projects.json`. They go stale; the
annotations do not, unless the project changes.

`evidence` lists the URLs actually read to reach the annotation. If a field was
settled by reading source rather than the README, the file path belongs there
too.
