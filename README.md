# hello-tts

## Setup

### VOICEVOX

Copy `voicevox/speaker_config.py.example` to `voicevox/speaker_config.py`.

```bash
cp voicevox/speaker_config.py.example voicevox/speaker_config.py
```

Set speaker names for TTS generation in `ALLOWED_SPEAKERS`, and VVM filenames to skip loading in `EXCLUDED_VVMS`.

#### Run

```bash
cd voicevox
uv run python main.py
```
