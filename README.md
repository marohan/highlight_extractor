# highlight_extractor

🎧 A Python package to extract highlight segments from songs using chroma repetition and energy analysis.

## Features

- Detects repeated musical segments via chroma similarity
- Combines with energy-based peak detection
- Filters out intro/outro noise and fade-outs
- Outputs the most suitable highlight section (default 15s)

## Installation

### From GitHub

```bash
pip install git+https://github.com/marohan/highlight_extractor.git
```

### From PyPi

```bash
pip install highlight-extractor
```

## 🧱 Project Structure

```
highlight_extractor/
├── highlight_extractor/
│   ├── __init__.py
│   └── core.py
├── examples/
│   └── run_example.py
├── setup.py
├── pyproject.toml
├── requirements.txt
├── README.md
└── LICENSE
```

## ⚙️ Dependencies

- librosa
- numpy
- scipy
- pydub

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Usage

from highlight_extractor import extract_highlight

start, end = extract_highlight("your_audio.mp3", target_duration=15)
print(f"Highlight from {start:.2f}s to {end:.2f}s")

## Example

```bash
python examples/run_example.py
```

Make sure to place an MP3 file (e.g., example_audio.mp3) in the root folder.

## ✨ Author

- Developed by **Marohan Min**
- GitHub: [@marohan](https://github.com/marohan)
- email : fragrantmaro@naver.com
