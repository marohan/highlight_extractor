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


## Overview

Purpose : To extract highlight sections of target duration (seconds) length from MP3 files. This logic basically starts from the premise that highlights in music are likely to be high energy sections with consistent chord repetitions.

First, it identifies repeat sections of at least 4 bars in length based on tempo through time-lag-similarity analysis of chromagram. (2)

If repeat sections are not identified, gradually reduce the number of bars to 2 and repeat the search.

Then it maps the STFT-based average energy value to the window of target duration length according to a certain step. (3)

Once mapping is done, it searches for items that are more than 75% identical to the repeat section obtained in (2) among the top items of energy values ​​obtained in (3), and select them as highlights if the conditions are satisfied. (4)

If no significant repeat sections are identified in (2) or no section satisfying the conditions is derived from the top 50% energy average value sections in (4), output the item with the highest average energy value as a highlight.


## Limitations & Improvement points

- In cases where it is difficult to secure tempo consistency or the energy clarity of the highlight is unclear, such as live sound sources, classical sound sources, or cases where repetitive chord patterns appear all the way through the song, the possibility of identification may be low.
  
- In sound sources where the pattern itself is unclear (such as sound sources with a narrative structure such as musicals), it is difficult to identify the repetitive pattern.

- In cases where the repetitive rhythm is emphasized and the pitch change is not large, such as some raps, there is a problem of excessively capturing the repetitive pattern.

- Since the analysis is based on 4/4 beat and the same tempo, there are issues when applying it to songs that deviate from the above criteria or have more complex forms (need to consider detailed parameters)


## ✨ Author

- Developed by **Marohan Min**
- GitHub: [@marohan](https://github.com/marohan)
- email : fragrantmaro@naver.com
