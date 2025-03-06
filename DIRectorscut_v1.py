import os
import re
from pathlib import Path

# Define the movie directory path
movie_directory = r"V:\Downloads\New Vids\Movies"

# Regex patterns
year_pattern = r"\b(19|20)\d{2}\b"

# Categorizing allowed tags
video_codecs = {
    "x265": "x265", "x264": "x264", "hevc": "HEVC", "h.264": "H.264", "h.265": "H.265", "avc": "AVC"
}
audio_encodings = {
    "dts": "DTS", "aac": "AAC", "ac3": "AC3", "dts-hd": "DTS-HD", "truehd": "TrueHD", "5.1": "5.1", "7.1": "7.1"
}
movie_versions = {
    "unrated": "Unrated", "extended": "Extended", "redux": "Redux", 
    "director['’]s cut": "Director’s Cut", "final cut": "Final Cut", "remastered": "Remastered"
}

def normalize_movie_name(original_name):
    # Extract year
    year_match = re.search(year_pattern, original_name)
    year = year_match.group(0) if year_match else ""

    # Extract video codec
    video_codec = next((f"[{video_codecs[tag]}]" for tag in video_codecs if re.search(rf"\b{tag}\b", original_name, re.IGNORECASE)), "")

    # Extract audio encoding
    audio_encoding = next((f"[{audio_encodings[tag]}]" for tag in audio_encodings if re.search(rf"\b{tag}\b", original_name, re.IGNORECASE)), "")

    # Extract movie version (prioritizing common ones)
    version_tags = [f"[{movie_versions[tag]}]" for tag in movie_versions if re.search(rf"\b{tag}\b", original_name, re.IGNORECASE)]
    movie_version = " ".join(version_tags)

    # Remove unnecessary parts and reformat the name
    clean_name = re.sub(r"[\.\-_]", " ", original_name)  # Replace dots, underscores, dashes with spaces
    clean_name = re.sub(rf"{year_pattern}.*", "", clean_name).strip()  # Remove everything after the year
    clean_name = re.sub(r"\s+", " ", clean_name)  # Normalize spaces

    # Construct new directory name
    new_name = f"{clean_name} ({year}) {video_codec} {audio_encoding} {movie_version}".strip()
    return re.sub(r"\s+", " ", new_name)  # Remove extra spaces

# Process directories with user approval
for dir_name in os.listdir(movie_directory):
    dir_path = Path(movie_directory) / dir_name
    if dir_path.is_dir():
        new_name = normalize_movie_name(dir_name)
        new_path = dir_path.parent / new_name

        if dir_path != new_path:
            # Prompt user for confirmation
            while True:
                user_input = input(f"\nRename: {dir_name}\n   → {new_name}\nApprove? (Y/N/Q to quit): ").strip().lower()
                
                if user_input == "y":  # Rename if approved
                    try:
                        os.rename(dir_path, new_path)
                        print(f"✅ Renamed: {dir_name} → {new_name}")
                    except Exception as e:
                        print(f"❌ Error renaming {dir_name}: {e}")
                    break
                
                elif user_input == "n":  # Skip renaming
                    print(f"⏩ Skipped: {dir_name}")
                    break
                
                elif user_input == "q":  # Quit script
                    print("🚪 Exiting script.")
                    exit()
                
                else:
                    print("Invalid input. Please enter 'Y' to approve, 'N' to skip, or 'Q' to quit.")
