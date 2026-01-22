import numpy as np
import pyaudio
from faster_whisper import WhisperModel


class AudioStreamSTT:
    def __init__(self, model: str, device: str, type: str) -> None:
        self.whisper = WhisperModel(
            model_size_or_path=model, device=device, compute_type=type
        )
        self.p = pyaudio.PyAudio()

        self.stream = None
        self.rate = None
        self.chunk = None

    def start(self, rate_size: int, chunk_size: int) -> None:
        self.rate = rate_size
        self.chunk = chunk_size

        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            rate=rate_size,
            channels=1,
            frames_per_buffer=chunk_size,
            input=True,
        )

    def record(self) -> bytes:
        return self.stream.read(self.chunk, exception_on_overflow=False)

    def bytes_to_array(self, frames: list[bytes]) -> np.ndarray:
        audio = np.frombuffer(b"".join(frames), dtype=np.float32)
        return audio

    def transcribe(self, audio: np.ndarray, lang: str) -> str:
        segment, _ = self.whisper.transcribe(
            audio=audio,
            language=lang,
            condition_on_previous_text=False,
            vad_filter=True,
        )
        return " ".join(seg.text for seg in segment).strip()

    def close(self) -> None:
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()
