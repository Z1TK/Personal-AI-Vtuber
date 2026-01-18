import numpy as np
import pyaudio
from TTS.api import TTS


class AudioStreamTTS:
    def __init__(self, model: str, device: str = "cpu"):
        self.tts = TTS(model).to(device)
        self.p = pyaudio.PyAudio()
        self.stream = None

    def start(self, chunk_size: int) -> None:
        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            rate=self.tts.synthesizer.output_sample_rate,
            channels=1,
            frames_per_buffer=chunk_size,
            output=True,
        )

    # def set_voice_cash(self, wav: list[str]) -> None:
    #     self.gpt_cond_latent, self.speaker_embedding = self.tts.get_conditioning_latents(wav)

    def synthesizing(
        self,
        text: str,
        wav: list[str],
        lang: str,
        speed: float | None = None,
        temperature: float | None = None,
    ) -> None:
        audio = self.tts.tts(
            text=text,
            language=lang,
            speed=speed,
            temperature=temperature,
            speaker_wav=wav,
            # gpt_cond_latent=self.gpt_cond_latent,
            # speaker_embedding=self.speaker_embedding,
        )
        audio32 = np.asarray(audio, np.float32)
        self.stream.write(audio32.tobytes())

    def close(self) -> None:
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()
