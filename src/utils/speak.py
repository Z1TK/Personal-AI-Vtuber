import time

import keyboard

from src.stt import AudioStreamSTT
from src.tts import AudioStreamTTS


def speak(stt: AudioStreamSTT, tts: AudioStreamTTS, rate: int, chunk: int) -> None:
    stt.start(rate, chunk)
    tts.start(chunk)

    while True:
        keyboard.wait("alt")
        print("Запись...")

        command = []

        while keyboard.is_pressed("alt"):
            command.append(stt.record())
            time.sleep(chunk / rate)

        record = stt.bytes_to_array(command)

        audio = stt.transcribe(record, "ru")

        if audio == "":
            print("Пользователь ничего не сказал")
            continue

        if audio.strip(" .,!?\n").lower() == "выход":
            break

        print("Приступаю к озвучиванию")

        reply_array = tts.synthesizing(
            text=audio,
            lang="ru",
            temperature=0.7,
            speed=1.0,
            wav=[
                "samples/sample_1.wav",
                "samples/sample_2.wav",
            ],
        )

        reply = tts.array_to_bytes(reply_array)
        tts.voice(reply)

    tts.close()
    stt.close()
