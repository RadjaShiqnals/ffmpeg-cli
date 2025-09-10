# FFmpeg CLI

A user-friendly command-line interface for FFmpeg on Linux-based systems. This tool provides simplified commands for common video and audio processing tasks using FFmpeg as the underlying engine.

## Prerequisites

- Linux-based operating system
- Python 3.6 or higher
- FFmpeg installed on your system

### Installing FFmpeg

On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

On CentOS/RHEL/Fedora:
```bash
# Fedora
sudo dnf install ffmpeg

# CentOS/RHEL (with EPEL repository)
sudo yum install epel-release
sudo yum install ffmpeg
```

## Installation

### Method 1: Direct execution
```bash
# Clone the repository
git clone https://github.com/RadjaShiqnals/ffmpeg-cli.git
cd ffmpeg-cli

# Make executable
chmod +x ffmpeg_cli.py

# Run directly
./ffmpeg_cli.py --help
```

### Method 2: Install as package
```bash
# Clone the repository
git clone https://github.com/RadjaShiqnals/ffmpeg-cli.git
cd ffmpeg-cli

# Install using pip
pip install .

# Use the installed command
ffmpeg-cli --help
```

## Usage

The tool provides several commands for common video and audio operations:

### Convert Video Format
```bash
ffmpeg-cli convert input.mov output.mp4
ffmpeg-cli convert input.avi output.mp4 --codec libx265 --quality high
```

### Extract Audio from Video
```bash
ffmpeg-cli extract-audio video.mp4 audio.mp3
ffmpeg-cli extract-audio video.mp4 audio.wav --format wav
```

### Resize Video
```bash
ffmpeg-cli resize video.mp4 small.mp4 640 480
ffmpeg-cli resize large.mov mobile.mp4 480 320
```

### Get Media File Information
```bash
ffmpeg-cli info video.mp4
ffmpeg-cli info audio.mp3
```

## Available Options

### Convert Command
- `--codec`: Video codec (default: libx264)
- `--quality`: Output quality - low, medium, high, lossless (default: medium)

### Extract Audio Command
- `--format`: Audio format - mp3, aac, wav, flac (default: mp3)

## Examples

```bash
# Convert a MOV file to MP4 with high quality
ffmpeg-cli convert presentation.mov presentation.mp4 --quality high

# Extract audio as MP3
ffmpeg-cli extract-audio concert.mp4 concert.mp3

# Extract audio as high-quality WAV
ffmpeg-cli extract-audio concert.mp4 concert.wav --format wav

# Resize video for mobile devices
ffmpeg-cli resize movie.mp4 mobile-movie.mp4 480 320

# Get information about a media file
ffmpeg-cli info unknown-file.mkv
```

## Quality Settings

- **low**: Smaller file size, lower quality (CRF 28)
- **medium**: Balanced size and quality (CRF 23) - default
- **high**: Larger file size, better quality (CRF 18)
- **lossless**: Maximum quality, largest file size (CRF 0)

## License

This project is open source and available under the MIT License.
