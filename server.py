from src.stt import AudioStreamSTT
from src.tts import AudioStreamTTS
from src.utils.speak import speak


def run():
    tts = AudioStreamTTS("tts_models/multilingual/multi-dataset/xtts_v2", "cuda")
    stt = AudioStreamSTT("large-v2", "cpu", type="int8")

    print("Помщник готов к работе")
    speak(stt, tts, 16000, 1024)


if __name__ == "__main__":
    run()
