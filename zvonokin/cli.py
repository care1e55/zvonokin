from pydub import AudioSegment

import typer as typer

from zvonokin.utils import modify_audio, write_json, stt_audio
import deepspeech
from pydantic_settings import BaseSettings


class AudioSettings(BaseSettings):
    stt_model_path: str = "resources/deepspeech-0.9.3-models.pbmm"
    modify_result_path: str = "resources/modify_result.wav"
    stt_result_path: str = "resources/stt_result.json"

    class Config:
        env_prefix = 'AUDIO_'


app = typer.Typer()
settings = AudioSettings()


@app.command()
def modify(
    path: str = typer.Option(...),
    speed: float = typer.Option(...),
    volume: int = typer.Option(...),
) -> None:
    audio = AudioSegment.from_file(path, format="wav")
    audio = modify_audio(audio, speed, volume)
    audio.export(settings.modify_result_path, format="wav")


@app.command()
def stt(
    path: str = typer.Option(...),
) -> None:
    model = deepspeech.Model(settings.stt_model_path)
    result_json = stt_audio(path, model)
    write_json(result_json, settings.stt_result_path)
