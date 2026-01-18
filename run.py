from src.service.tts import AudioStreamTTS


def run():
    tts_engine = AudioStreamTTS("tts_models/multilingual/multi-dataset/xtts_v2", "cuda")
    tts_engine.start(1024)

    print("Напишите сообщение: ")
    while True:
        text = input()
        tts_engine.synthesizing(
            text=text,
            lang="ru",
            temperature=0.7,
            speed=1.0,
            wav=[
                "samples/sample_1.wav",
                "samples/sample_2.wav",
            ],
        )
        if text == "exit":
            break

    tts_engine.close()


if __name__ == "__main__":
    run()
