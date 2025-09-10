#!/usr/bin/env python3
"""Setup script for ffmpeg-cli."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ffmpeg-cli",
    version="1.0.0",
    author="FFmpeg CLI Contributors",
    description="A user-friendly command-line interface for FFmpeg on Linux systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RadjaShiqnals/ffmpeg-cli",
    py_modules=["ffmpeg_cli"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Multimedia :: Video",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "ffmpeg-cli=ffmpeg_cli:main",
        ],
    },
)