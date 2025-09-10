#!/usr/bin/env python3
"""
FFmpeg CLI - A user-friendly command-line interface for FFmpeg on Linux systems.

This tool provides simplified commands for common video and audio processing tasks
using FFmpeg as the underlying engine.
"""

import argparse
import subprocess
import sys
import os
import shutil
from pathlib import Path


class FFmpegCLI:
    """Main class for FFmpeg CLI operations."""
    
    def __init__(self):
        self.ffmpeg_path = self._find_ffmpeg()
    
    def _find_ffmpeg(self):
        """Find FFmpeg executable in system PATH."""
        ffmpeg_path = shutil.which('ffmpeg')
        if not ffmpeg_path:
            print("Error: FFmpeg not found in system PATH. Please install FFmpeg first.")
            sys.exit(1)
        return ffmpeg_path
    
    def _run_ffmpeg(self, args, input_file=None, output_file=None):
        """Execute FFmpeg command with given arguments."""
        cmd = [self.ffmpeg_path] + args
        
        if input_file:
            cmd.extend(['-i', input_file])
        
        if output_file:
            cmd.append(output_file)
        
        print(f"Running: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"Error: {result.stderr}")
                return False
            else:
                print("Success!")
                if result.stdout:
                    print(result.stdout)
                return True
        except Exception as e:
            print(f"Error running FFmpeg: {e}")
            return False
    
    def convert_video(self, input_file, output_file, codec='libx264', quality='medium'):
        """Convert video to different format."""
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return False
        
        quality_settings = {
            'low': ['-crf', '28'],
            'medium': ['-crf', '23'],
            'high': ['-crf', '18'],
            'lossless': ['-crf', '0']
        }
        
        args = ['-y', '-c:v', codec] + quality_settings.get(quality, quality_settings['medium'])
        args.extend(['-c:a', 'aac'])
        
        return self._run_ffmpeg(args, input_file, output_file)
    
    def extract_audio(self, input_file, output_file, codec='mp3'):
        """Extract audio from video file."""
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return False
        
        codec_map = {
            'mp3': 'libmp3lame',
            'aac': 'aac',
            'wav': 'pcm_s16le',
            'flac': 'flac'
        }
        
        args = ['-y', '-vn', '-c:a', codec_map.get(codec, 'libmp3lame')]
        
        return self._run_ffmpeg(args, input_file, output_file)
    
    def resize_video(self, input_file, output_file, width, height):
        """Resize video to specified dimensions."""
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return False
        
        args = ['-y', '-vf', f'scale={width}:{height}', '-c:a', 'copy']
        
        return self._run_ffmpeg(args, input_file, output_file)
    
    def get_info(self, input_file):
        """Get information about media file."""
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return False
        
        cmd = [self.ffmpeg_path, '-i', input_file]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            # FFmpeg outputs info to stderr
            print(result.stderr)
            return True
        except Exception as e:
            print(f"Error getting file info: {e}")
            return False


def main():
    """Main entry point for the CLI application."""
    parser = argparse.ArgumentParser(
        description='FFmpeg CLI - User-friendly FFmpeg interface for Linux',
        epilog='Examples:\n'
               '  ffmpeg-cli convert input.mov output.mp4\n'
               '  ffmpeg-cli extract-audio video.mp4 audio.mp3\n'
               '  ffmpeg-cli resize video.mp4 small.mp4 640 480\n'
               '  ffmpeg-cli info video.mp4',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Convert command
    convert_parser = subparsers.add_parser('convert', help='Convert video format')
    convert_parser.add_argument('input', help='Input video file')
    convert_parser.add_argument('output', help='Output video file')
    convert_parser.add_argument('--codec', default='libx264', 
                              help='Video codec (default: libx264)')
    convert_parser.add_argument('--quality', choices=['low', 'medium', 'high', 'lossless'],
                              default='medium', help='Output quality (default: medium)')
    
    # Extract audio command
    audio_parser = subparsers.add_parser('extract-audio', help='Extract audio from video')
    audio_parser.add_argument('input', help='Input video file')
    audio_parser.add_argument('output', help='Output audio file')
    audio_parser.add_argument('--format', choices=['mp3', 'aac', 'wav', 'flac'],
                            default='mp3', help='Audio format (default: mp3)')
    
    # Resize command
    resize_parser = subparsers.add_parser('resize', help='Resize video')
    resize_parser.add_argument('input', help='Input video file')
    resize_parser.add_argument('output', help='Output video file')
    resize_parser.add_argument('width', type=int, help='Target width')
    resize_parser.add_argument('height', type=int, help='Target height')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Show file information')
    info_parser.add_argument('input', help='Input media file')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    cli = FFmpegCLI()
    
    if args.command == 'convert':
        success = cli.convert_video(args.input, args.output, args.codec, args.quality)
    elif args.command == 'extract-audio':
        success = cli.extract_audio(args.input, args.output, args.format)
    elif args.command == 'resize':
        success = cli.resize_video(args.input, args.output, args.width, args.height)
    elif args.command == 'info':
        success = cli.get_info(args.input)
    else:
        parser.print_help()
        sys.exit(1)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()