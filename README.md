# hello-tts

## Setup

### VOICEVOX

`voicevox/speaker_config.py.example` をコピーして `voicevox/speaker_config.py` を作成してください。

```bash
cp voicevox/speaker_config.py.example voicevox/speaker_config.py
```

`ALLOWED_SPEAKERS` に音声生成対象のスピーカー名を、`EXCLUDED_VVMS` にロードしないVVMファイル名を設定してください。

#### 実行

```bash
cd voicevox
uv run python main.py
```
