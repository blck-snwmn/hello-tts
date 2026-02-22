import glob
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from voicevox_core.blocking import Onnxruntime, OpenJtalk, Synthesizer, VoiceModelFile

from speaker_config import ALLOWED_SPEAKERS, EXCLUDED_VVMS

onnxruntime = Onnxruntime.load_once(
    filename=f"./voicevox_core/onnxruntime/lib/{Onnxruntime.LIB_VERSIONED_FILENAME}"
)
synthesizer = Synthesizer(onnxruntime, OpenJtalk("./voicevox_core/dict/open_jtalk_dic_utf_8-1.11"))

for vvm_path in sorted(glob.glob("./voicevox_core/models/vvms/*.vvm")):
    if Path(vvm_path).name in EXCLUDED_VVMS:
        continue
    with VoiceModelFile.open(vvm_path) as model:
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

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

styles = [
    (meta.name, style.name, style.id)
    for meta in synthesizer.metas()
    if meta.name in ALLOWED_SPEAKERS
    for style in meta.styles
]


def generate(speaker_name: str, style_name: str, style_id: int) -> str:
    filename = f"{speaker_name}_{style_name}_{style_id}.wav"
    output_path = output_dir / filename

    wav = synthesizer.tts(text, style_id=style_id)
    with open(output_path, "wb") as f:
        f.write(wav)

    return str(output_path)


with ThreadPoolExecutor() as executor:
    futures = {
        executor.submit(generate, name, sname, sid): (name, sname)
        for name, sname, sid in styles
    }

    for future in as_completed(futures):
        name, sname = futures[future]
        try:
            path = future.result()
            print(f"  {path}")
        except Exception as e:
            print(f"  [ERROR] {name}({sname}): {e}")

print("Generation complete")
