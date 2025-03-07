import os
import re
import subprocess
import json
import csv
from pathlib import Path

# Ask the user for the movie directory
while True:
    movie_directory = input("Enter the path to your movie directory: ").strip()
    if os.path.isdir(movie_directory):
        break
    print("❌ Invalid directory. Please enter a valid path.")

# Ask the user if they want to generate a report
generate_report = input("Do you want to generate a report? (Y/N): ").strip().lower()
report_data = []

# Regex patterns
year_pattern = r"\b(19|20)\d{2}\b"
website_pattern = r"(?:www\.|http[s]?://)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"  # Detects website patterns

# Allowed video file extensions
video_extensions = {".mkv", ".mp4", ".avi", ".m4v", ".webm", ".mov", ".wmv", ".flv"}

# Standardization mappings
video_codec_map = {
    "hevc": "[H.265]", "h265": "[H.265]", "h264": "[H.264]", "x264": "[H.264]", "vp9": "[VP9]", "av1": "[AV1]", "mpeg4": "[MPEG4]", "vc1": "[VC-1]"
}
audio_codec_map = {
    "aac": "[AAC]", "ac3": "[AC3]", "dts": "[DTS]", "dts-hd": "[DTS-HD]", "truehd": "[TrueHD]", "eac3": "[EAC3]"
}

def format_resolution(width, height):
    if width == 1920 and height == 1080:
        return "[1080p]"
    elif width == 1280 and height == 720:
        return "[720p]"
    elif width == 3840 and height == 2160:
        return "[4K]"
    elif width == 7680 and height == 4320:
        return "[8K]"
    elif width == 2048 and height == 1080:
        return "[2K]"
    elif width == 5120 and height == 2880:
        return "[5K]"
    elif width == 720 and height == 480:
        return "[480p]"
    else:
        return f"[{width}x{height}]"

def find_main_movie_file(directory):
    """Finds the largest video file in the directory, assuming it's the main movie file."""
    video_files = [f for f in Path(directory).rglob("*.*") if f.suffix.lower() in video_extensions]
    
    if not video_files:
        print(f"❌ No valid video files found in: {directory}")
        return None
    
    largest_file = max(video_files, key=lambda f: f.stat().st_size)
    print(f"📂 Selected main movie file: {largest_file}")  # Debugging
    return largest_file

def extract_metadata(video_file):
    """Extracts resolution, video codec, and audio codec from the given video file using FFmpeg."""
    if not video_file.exists():
        print(f"❌ File not found: {video_file}")
        return None, None, None, None

    try:
        cmd = [
            "ffprobe", "-v", "quiet", "-print_format", "json",
            "-show_streams", str(video_file)
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        metadata = json.loads(result.stdout)

        video_codec, audio_codec, resolution, audio_channels = None, None, None, None

        for stream in metadata.get("streams", []):
            if stream["codec_type"] == "video":
                raw_codec = stream["codec_name"].lower()
                video_codec = video_codec_map.get(raw_codec, f"[{raw_codec.upper()}]")
                width, height = stream.get("width", 0), stream.get("height", 0)
                resolution = format_resolution(width, height)
            elif stream["codec_type"] == "audio" and not audio_codec:
                raw_audio = stream["codec_name"].lower()
                audio_codec = audio_codec_map.get(raw_audio, f"[{raw_audio.upper()}]")
                audio_channels = f"[{stream.get('channels', 'Unknown')}.1]" if stream.get('channels', 0) > 2 else "[Stereo]"

        return video_codec, audio_codec, resolution, audio_channels

    except Exception as e:
        print(f"❌ FFmpeg error on {video_file}: {e}")
        return None, None, None, None

# Process directories with user approval
for root, dirs, files in os.walk(movie_directory):
    for dir_name in dirs:
        dir_path = Path(root) / dir_name
        
        main_movie = find_main_movie_file(dir_path)
        if main_movie:
            video_codec, audio_codec, resolution, audio_channels = extract_metadata(main_movie)
            print(f"Extracted metadata for {main_movie}:")
            print(f"  - Video Codec: {video_codec}")
            print(f"  - Audio Codec: {audio_codec}")
            print(f"  - Resolution: {resolution}")
            print(f"  - Audio Channels: {audio_channels}")
            
            if generate_report == "y":
                report_data.append([main_movie.name, video_codec, audio_codec, resolution, audio_channels])

# Save report if needed
if generate_report == "y" and report_data:
    report_path = input("Enter the path to save the report (default: Movies/report.csv): ").strip()
    if not report_path:
        report_path = os.path.join(movie_directory, "report.csv")
    
    with open(report_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Movie File", "Video Codec", "Audio Codec", "Resolution", "Audio Channels"])
        writer.writerows(report_data)
    
    print(f"✅ Report saved to {report_path}")
