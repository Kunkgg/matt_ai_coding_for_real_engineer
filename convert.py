import pathlib
import time

from faster_whisper import WhisperModel

BASE_DIR = pathlib.Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio"
CONVERTED_HISTORY = BASE_DIR / "converted_history.txt"

model = WhisperModel("medium", device="cpu", compute_type="int8", cpu_threads=16)


def load_converted_history(history_file: pathlib.Path) -> set:
    if history_file.exists():
        with open(history_file, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f)
    return set()


def save_converted_history(history_file: pathlib.Path, converted_files: set):
    with open(history_file, "w", encoding="utf-8") as f:
        for file in sorted(converted_files):
            f.write(f"{file}\n")


def convert_audio_folder(audio_folder: pathlib.Path, language: str = "en"):
    start_time = time.perf_counter()
    audio_files = sorted(audio_folder.glob("*.m4a"))
    converted_files = load_converted_history(CONVERTED_HISTORY)
    for idx, audio_file in enumerate(audio_files, start=1):
        if audio_file.name in converted_files:
            print(f"Skipping {audio_file.name}...")
            continue
        print(f"Processing {idx}/{len(audio_files)}: {audio_file.name}...")
        each_start_time = time.perf_counter()
        segments, _ = model.transcribe(audio_file, language=language, beam_size=1)
        srt_file = audio_file.with_suffix(".srt")
        with open(srt_file, "w", encoding="utf-8") as f:
            for i, segment in enumerate(segments, start=1):
                f.write(f"{i}\n")
                f.write(f"{segment.start:.3f} --> {segment.end:.3f}\n")
                f.write(segment.text + "\n\n")
        each_end_time = time.perf_counter()
        print(
            f"Converted {audio_file.name} to {srt_file.name} in {each_end_time - each_start_time:.2f} seconds"
        )
        converted_files.add(audio_file.name)
        save_converted_history(CONVERTED_HISTORY, converted_files)

    end_time = time.perf_counter()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    convert_audio_folder(AUDIO_DIR, language="en")
