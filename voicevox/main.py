from voicevox_core.blocking import Onnxruntime, OpenJtalk, Synthesizer, VoiceModelFile

onnxruntime = Onnxruntime.load_once(
    filename=f"./voicevox_core/onnxruntime/lib/{Onnxruntime.LIB_VERSIONED_FILENAME}"
)
synthesizer = Synthesizer(onnxruntime, OpenJtalk("./voicevox_core/dict/open_jtalk_dic_utf_8-1.11"))

with VoiceModelFile.open("./voicevox_core/models/vvms/0.vvm") as model:
    synthesizer.load_voice_model(model)

wav = synthesizer.tts("こんにちは、世界！", style_id=3)
with open("output.wav", "wb") as f:
    f.write(wav)

print("output.wav を生成しました (VOICEVOX:ずんだもん)")
