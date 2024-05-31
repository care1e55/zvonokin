# zvonokin

STT and modify audio

### Installation:

Packages can be installed via `poetry`: 
```bash
poetry shell
poetry install
```

Download STT model:
```bash
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
```

### Usage
Command line arguments can be viewed with `--help` option:
```bash
python zvonokin/cli.py --help
```

Set up arguments:
```bash
export PYTHONPATH=$PWD
export AUDIO_STT_MODEL_PATH="resources/deepspeech-0.9.3-models.pbmm"
export AUDIO_MODIFY_RESULT_PATH="resources/modify_result.wav"
export AUDIO_STT_RESULT_PATH="resources/stt_result.json"
```


### Examples

#### Modify audio

```bash
zvonokin modify audio --path 'resources/data.wav' --velocity 1.25 --volume 10
```

#### STT

```bash
zvonokin stt --path 'resources/data.wav'
```
