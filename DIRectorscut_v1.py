import os
import re
from pathlib import Path

# Ask the user for the movie directory
while True:
    movie_directory = input("Enter the path to your movie directory: ").strip()
    if os.path.isdir(movie_directory):
        break
    print("❌ Invalid directory. Please enter a valid path.")

# Regex patterns
year_pattern = r"\b(19|20)\d{2}\b"
website_pattern = r"(?:www\.|http[s]?://)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"  # Detects website patterns

# Allowed video file extensions
video_extensions = {".mkv", ".mp4", ".avi", ".m4v", ".webm", ".mov", ".wmv", ".flv"}

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

def check_for_executables(directory):
    """Checks for .exe files and prompts the user to delete them."""
    exe_files = list(Path(directory).rglob("*.exe"))
    if exe_files:
        print("\n⚠️ WARNING: Executable files detected in your movie folders!\n")
        for exe in exe_files:
            while True:
                user_input = input(f"Found: {exe}\nDelete this file? (Y/N/Q to quit): ").strip().lower()
                if user_input == "y":
                    try:
                        os.remove(exe)
                        print(f"🗑️ Deleted: {exe}")
                    except Exception as e:
                        print(f"❌ Error deleting {exe}: {e}")
                    break
                elif user_input == "n":
                    print(f"⏩ Skipped: {exe}")
                    break
                elif user_input == "q":
                    print("🚪 Exiting script.")
                    exit()
                else:
                    print("Invalid input. Please enter 'Y' to delete, 'N' to keep, or 'Q' to quit.")

def normalize_movie_name(original_name):
    # Remove website references
    original_name = re.sub(website_pattern, "", original_name).strip()
    
    # Remove leading/trailing hyphens
    original_name = re.sub(r"^[- ]+|[- ]+$", "", original_name).strip()

    # Extract year
    year_match = re.search(year_pattern, original_name)
    year = year_match.group(0) if year_match else ""

    # Extract resolution
    resolution_match = re.search(r"(1080p|720p|2160p|480p)", original_name, re.IGNORECASE)
    resolution = f"[{resolution_match.group(0)}]" if resolution_match else ""

    # Extract video codec
    video_codec = next((f"[{video_codecs[tag]}]" for tag in video_codecs if re.search(rf"\b{tag}\b", original_name, re.IGNORECASE)), "")

    # Extract audio encoding
    audio_encoding = next((f"[{audio_encodings[tag]}]" for tag in audio_encodings if re.search(rf"\b{tag}\b", original_name, re.IGNORECASE)), "")

    # Extract movie version
    version_tags = [f"[{movie_versions[tag]}]" for tag in movie_versions if re.search(rf"\b{tag}\b", original_name, re.IGNORECASE)]
    movie_version = " ".join(version_tags)

    # Remove unnecessary characters (dots, underscores, dashes)
    clean_name = re.sub(r"[\._-]", " ", original_name).strip()

    # Ensure we don't delete part of the title after the year
    if year:
        clean_name = re.sub(rf"\s*\(?\b{year}\b.*", "", clean_name).strip()

    # Construct final directory name in the correct order
    new_name = f"{clean_name} ({year}) {movie_version} {resolution} {video_codec} {audio_encoding}".strip()
    
    # Ensure clean formatting (e.g., remove double spaces)
    new_name = re.sub(r"\s+", " ", new_name)

    return new_name

# Check for executable files before processing
check_for_executables(movie_directory)

# Process directories with user approval
for dir_name in os.listdir(movie_directory):
    dir_path = Path(movie_directory) / dir_name
    if dir_path.is_dir():
        new_name = normalize_movie_name(dir_name)
        new_path = dir_path.parent / new_name

        if dir_path != new_path:
            # Prompt user for confirmation
            while True:
                user_input = input(f"\nRename: {dir_name}\n   → {new_name}\nApprove? (Y/N/S/Q to quit): ").strip().lower()
                
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
                
                elif user_input == "s":  # Skip renaming without logging
                    break
                
                elif user_input == "q":  # Quit script
                    print("🚪 Exiting script.")
                    exit()
                
                # elif user_input == "a":  # Uncomment to add 'Approve All' functionality
                #     auto_approve = True
                #     break
                
                else:
                    print("Invalid input. Please enter 'Y' to approve, 'N' to skip, 'S' to silently skip, or 'Q' to quit.")
