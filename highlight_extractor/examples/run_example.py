# examples/run_example.py

import os
from highlight_extractor import extract_highlight
from pydub import AudioSegment
from pydub.playback import play

# 예제 파일 경로
AUDIO_FILE = "example_audio.mp3"  # 같은 디렉토리에 있는 MP3 예시 파일

def main():
    if not os.path.exists(AUDIO_FILE):
        print(f"Cannot find audio file: {AUDIO_FILE}")
        return

    # Extract Highlight
    print("🔍 Extracting Highlight...")
    start, end = extract_highlight(AUDIO_FILE, target_duration=15)
    print(f"🎧 Extracted Highlight Segments: {start:.2f} ~ {end:.2f}")

    # Load and Play
    print("▶️ Playing...")
    audio = AudioSegment.from_file(AUDIO_FILE)
    segment = audio[start * 1000:end * 1000].fade_in(1000).fade_out(1000)
    play(segment)

if __name__ == "__main__":
    main()
