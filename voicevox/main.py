from pathlib import Path

from voicevox_core.blocking import Onnxruntime, OpenJtalk, Synthesizer, VoiceModelFile

onnxruntime = Onnxruntime.load_once(
    filename=f"./voicevox_core/onnxruntime/lib/{Onnxruntime.LIB_VERSIONED_FILENAME}"
)
synthesizer = Synthesizer(onnxruntime, OpenJtalk("./voicevox_core/dict/open_jtalk_dic_utf_8-1.11"))

with VoiceModelFile.open("./voicevox_core/models/vvms/0.vvm") as model:
    synthesizer.load_voice_model(model)

text = (
    "おはようございます。今日は2025年2月22日、土曜日です。"
    "天気予報によると、最高気温は12度、最低気温は3度だそうです。"
    "ところで、昨日の会議はどうでしたか？"
    "ええっ、まさか1時間半も延長したんですか！それは大変でしたね。"
    "さて、今日の予定を確認しましょう。"
    "まず午前中に資料を作成して、午後3時からお客様との打ち合わせがあります。"
    "あ、そうだ。お昼ご飯は何にしようかな……。"
    "カレーライスか、それともラーメンか。うーん、迷いますね。"
    "まあ、とりあえず頑張っていきましょう！"
)

wav = synthesizer.tts(text, style_id=3)

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)
output_path = output_dir / "output.wav"

with open(output_path, "wb") as f:
    f.write(wav)

print(f"{output_path} を生成しました (VOICEVOX:ずんだもん)")
