# FFmpeg CLI Makefile

.PHONY: help install test clean dev-install

help:
	@echo "Available commands:"
	@echo "  install     - Install ffmpeg-cli globally"
	@echo "  dev-install - Install in development mode"
	@echo "  test        - Run test suite"
	@echo "  clean       - Clean build artifacts"
	@echo "  help        - Show this help message"

install:
	@echo "Installing ffmpeg-cli..."
	pip install .

dev-install:
	@echo "Installing ffmpeg-cli in development mode..."
	pip install -e .

test:
	@echo "Running test suite..."
	python3 test_cli.py

clean:
	@echo "Cleaning build artifacts..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# Check if FFmpeg is installed
check-deps:
	@echo "Checking dependencies..."
	@which ffmpeg > /dev/null && echo "✓ FFmpeg found" || echo "✗ FFmpeg not found - please install FFmpeg"
	@python3 --version