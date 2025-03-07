# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
- Planned improvements and feature enhancements.

## [1.0.0] - 2025-03-06
### Added
- Initial release of the movie metadata extraction script.
- Directory traversal to find the main movie file in each folder.
- Extraction of video codec, audio codec, resolution, and audio channels using `ffprobe`.
- Standardization of extracted metadata for consistency.
- Support for multiple video formats: `.mkv`, `.mp4`, `.avi`, `.m4v`, `.webm`, `.mov`, `.wmv`, `.flv`.
- Option to generate a report in CSV format containing extracted metadata.
- User-defined report save location with a default to the `Movies` directory.

### Fixed
- Addressed FFmpeg installation issues to ensure smooth metadata extraction.
- Improved error handling for missing files and invalid directories.

### Changed
- Optimized the method for identifying the primary movie file in each directory.

## [0.9.0] - 2025-03-05
### Added
- Initial implementation of the script with basic directory traversal and FFmpeg metadata extraction.

### Fixed
- Debugging and validation of extracted metadata.

---

**Note:** Version numbers follow [Semantic Versioning](https://semver.org/).