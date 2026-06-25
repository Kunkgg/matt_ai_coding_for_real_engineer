import re
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
SUBS_DIR = BASE_DIR / "subs"


def clean_subtitle_content(content: str) -> str:
    # Remove time ticks and any unwanted characters from the subtitle content
    cleaned_content = re.sub(
        r"\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n", "", content
    )
    cleaned_content = re.sub(
        r"[^\w\s.,!?]", "", cleaned_content
    )  # Remove unwanted characters
    return cleaned_content.strip()


def merge_subs(subs_dir: pathlib.Path) -> str:
    merged_subs = []
    for sub_file in sorted(subs_dir.glob("*.srt")):
        with open(sub_file, "r", encoding="utf-8") as f:
            content = f.read()
            title = sub_file.stem
            merged_subs.append(f"### {title}\n{clean_subtitle_content(content)}\n")
    return "\n".join(merged_subs)


if __name__ == "__main__":
    merged_content = merge_subs(SUBS_DIR)
    output_file = BASE_DIR / "merged_subs.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(merged_content)
    print(f"Merged subtitles saved to {output_file}")
