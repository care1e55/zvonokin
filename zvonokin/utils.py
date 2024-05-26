import sys
import wave
from pathlib import Path
from typing import Dict

import deepspeech
import json

import numpy as np
from pydub import AudioSegment
from pydub.effects import speedup
from deepspeech.client import convert_samplerate


def modify_audio(audio: AudioSegment, speed: float, volume: int) -> AudioSegment:
    audio = speedup(audio, playback_speed=speed)
    audio = audio + volume
    return audio


def stt_audio(audio_path: str, model: deepspeech.Model) -> Dict[str, str]:
    audio: wave.Wave_read = wave.open(audio_path, 'rb')
    desired_sample_rate = model.sampleRate()
    orig_sample_rate = audio.getframerate()
    if orig_sample_rate != desired_sample_rate:
        print(
            'Warning: original sample rate ({}) is different than {}hz.'
            'Resampling might produce erratic speech recognition.'
            .format(orig_sample_rate, desired_sample_rate), file=sys.stderr
        )
        fs_new, audio = convert_samplerate(audio_path, desired_sample_rate)
    else:
        audio = np.frombuffer(audio.readframes(audio.getnframes()), np.int16)
    audio = np.frombuffer(audio.readframes(audio.getnframes()), np.int16)
    text = model.stt(audio)
    return {"text": text}


def write_json(stt_json: Dict, path: Path):
    with open(path, 'w') as f:
        return json.dump(stt_json, f)
