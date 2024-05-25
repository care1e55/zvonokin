# zvonokin

STT and modify audio

### Installation:

Packages can be installed via `poetry`: 
```bash
poetry shell
poetry install
```
or `requirements.txt`:
```bash
pip install -e requirements.txt
```

### Usage
Command line arguments can be viewed with `--help` option:
```bash
python zvonokin/cli.py --help
```

### Examples

#### Modify audio

```bash
python zvonokin/cli.py modify --path 'resources/data.wav' --velocity 1.25 --volume 10
```

#### STT

```bash
python zvonokin/cli.py stt --path 'resources/data.wav'
```
