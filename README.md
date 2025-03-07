# DirectorsCut V2

## Overview
DirectorsCut V2 is a Python script that automates the extraction of metadata from movie files in a specified directory. It utilizes FFmpeg's `ffprobe` to gather video codec, audio codec, resolution, and audio channel information. The script also offers an option to generate a structured report in CSV format.

## Features
- Recursively scans a movie directory to locate main movie files
- Extracts metadata including:
  - Video codec
  - Audio codec
  - Resolution
  - Audio channels
- Supports multiple video formats (`.mkv`, `.mp4`, `.avi`, `.m4v`, `.webm`, `.mov`, `.wmv`, `.flv`)
- Provides an option to generate a report (CSV) of all processed movie files
- Saves the report to a user-specified location (defaults to the `Movies/` directory)

## Prerequisites
Ensure you have the following installed before running the script:

- **Python 3.7+**
- **FFmpeg** (with `ffprobe` accessible from the command line)
  - [Download FFmpeg](https://ffmpeg.org/download.html)
  - Ensure it's added to your system `PATH`

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/directorscut-v2.git
   cd directorscut-v2
   ```
2. Install dependencies (if any required in the future):
   ```sh
   pip install -r requirements.txt  # Currently, no external dependencies
   ```

## Usage
Run the script with:
```sh
python directorscut_v2.py
```

### Steps:
1. Enter the path to your movie directory.
2. The script will automatically detect and analyze movie files.
3. You will be prompted whether to generate a metadata report (`Y/N`).
4. If `Y`, specify the save location (defaults to `Movies/report.csv`).
5. The script processes each movie file, displaying extracted metadata.
6. If a report is generated, it is saved in the specified location.

## Example Output
```plaintext
Enter the path to your movie directory: V:\Downloads\New Vids\Movies
📂 Selected main movie file: V:\Downloads\New Vids\Movies\Big Daddy (1999) [1080p] [x264] [DTS]\Big Daddy (1999).mkv
Extracted metadata for Big Daddy (1999).mkv:
  - Video Codec: [H.264]
  - Audio Codec: [DTS]
  - Resolution: [1920x1040]
  - Audio Channels: [6.1]
Do you want to generate a report? (Y/N): Y
Enter the path to save the report (default: Movies/report.csv):
✅ Report saved to Movies/report.csv
```

## Future Enhancements
- Support for additional metadata fields (e.g., bitrate, framerate)
- JSON report option
- GUI version for easier interaction
- Multi-threaded processing for large directories

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit pull requests or open issues for any bugs, feature requests, or improvements!
