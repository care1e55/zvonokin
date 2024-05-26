import wave
from pathlib import Path
from typing import Dict

import deepspeech
import json

import numpy as np
from pydub import AudioSegment
from pydub.effects import speedup


def modify_audio(audio: AudioSegment, speed: float, volume: int) -> AudioSegment:
    audio = speedup(audio, playback_speed=speed)
    audio = audio + volume
    return audio


def stt(audio: wave.Wave_read, model: deepspeech.Model, *args, **kwargs) -> Dict[str, str]:
    audio = np.frombuffer(audio.readframes(audio.getnframes()), np.int16)
    text = model.stt(audio)
    return {"text": text}


def write_json(stt_json: Dict, path: Path):
    with open(path, 'w') as f:
        return json.dump(stt_json, f)
