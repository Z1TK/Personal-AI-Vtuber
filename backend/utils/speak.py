import time

import keyboard

from backend.service.stt import AudioStreamSTT
from backend.service.tts import AudioStreamTTS


def listen_commands(stt_engine: AudioStreamSTT, rate: int, chunk: int) -> str:
    print("Нажми и удерживай ALT, чтобы начать разговор")
    keyboard.wait("alt")
    print("Запись...")
    command = []

    try:
        while keyboard.is_pressed("alt"):
            command.append(stt_engine.record())
            time.sleep(chunk / rate)
        print("Прекращение записи")

        record = stt_engine.bytes_to_array(command)
        audio = stt_engine.transcribe(record, "ru")
    except (OSError, IOError) as e:
        print(f"Ошибка аудиоустройства: {e}")
    except (ValueError, RuntimeError) as e:
        print(f"Ошибка распознования речи: {e}")
    except Exception as e:
        print(f"Ошибка STT: {e}")

    print(f"Пользователь: {audio}")
    return audio


def speak_assistant(tts_engine: AudioStreamTTS, audio: str) -> None:
    print("начинаю обработку")

    try:
        reply_array = tts_engine.synthesizing(
            text=audio,
            lang="ru",
            temperature=0.7,
            speed=1.0,
            wav=[
                "backend/samples/sample_1.wav",
                "backend/samples/sample_2.wav",
            ],
        )

        reply = tts_engine.array_to_bytes(reply_array)
        tts_engine.voice(reply)
    except (OSError, IOError) as e:
        print(f"Ошибка аудиовыхода: {e}")
    except (ValueError, RuntimeError) as e:
        print(f"Ошибка синтеза речи: {e}")
    except Exception as e:
        print(f"Ошибка TTS: {e}")
