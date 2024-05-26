from pathlib import Path
from pydub import AudioSegment

import typer as typer

from zvonokin.utils import modify_audio, write_json, stt
import wave
import deepspeech
from pydantic_settings import BaseSettings


class AudioSettings(BaseSettings):
    stt_model_path: Path
    modify_result_path: Path
    stt_result_path: Path

    class Config:
        env_prefix = 'AUDIO_'


settings = AudioSettings()
app = typer.Typer()


@app.command()
def _modify(
    path: Path = typer.Option(...),
    speed: float = typer.Option(...),
    volume: int = typer.Option(...),
) -> None:
    audio = AudioSegment.from_file(path, format="wav")
    audio = modify_audio(audio, speed, volume)
    audio.export(settings.modify_result_path, format="wav")


@app.command()
def _stt(
    path: Path = typer.Option(...),
) -> None:
    audio: wave.Wave_read = wave.open(path, 'rb')
    model = deepspeech.Model(settings.stt_model_path)
    result_json = stt(audio, model)
    write_json(result_json, settings.stt_result_path)


if __name__ == '__main__':
    app()
