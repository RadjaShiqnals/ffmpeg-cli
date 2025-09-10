#!/usr/bin/env python3
"""
Simple test script for ffmpeg-cli functionality.
Tests the CLI interface and argument parsing without requiring FFmpeg to be installed.
"""

import subprocess
import sys
import os


def run_command(cmd):
    """Run a command and return (exit_code, stdout, stderr)."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)


def test_help_commands():
    """Test that help commands work correctly."""
    tests = [
        "python3 ffmpeg_cli.py --help",
        "python3 ffmpeg_cli.py convert --help",
        "python3 ffmpeg_cli.py extract-audio --help",
        "python3 ffmpeg_cli.py resize --help",
        "python3 ffmpeg_cli.py info --help"
    ]
    
    print("Testing help commands...")
    for cmd in tests:
        print(f"  Running: {cmd}")
        exit_code, stdout, stderr = run_command(cmd)
        if exit_code == 0 and "usage:" in stdout:
            print("    ✓ PASS")
        else:
            print(f"    ✗ FAIL (exit code: {exit_code})")
            return False
    return True


def test_error_handling():
    """Test error handling for missing files and invalid arguments."""
    print("\nTesting error handling...")
    
    # Test missing FFmpeg (expected to fail gracefully)
    print("  Testing FFmpeg detection...")
    exit_code, stdout, stderr = run_command("python3 ffmpeg_cli.py info nonexistent.file")
    if exit_code != 0 and ("FFmpeg not found" in stdout or "not found" in stdout):
        print("    ✓ PASS - FFmpeg detection works")
    else:
        print("    ? INFO - FFmpeg might be installed")
    
    # Test invalid command
    print("  Testing invalid command...")
    exit_code, stdout, stderr = run_command("python3 ffmpeg_cli.py invalid-command")
    if exit_code != 0:
        print("    ✓ PASS - Invalid command handled")
    else:
        print("    ✗ FAIL - Invalid command not handled")
        return False
    
    return True


def test_cli_structure():
    """Test that the CLI has the expected structure."""
    print("\nTesting CLI structure...")
    
    # Test main help contains expected commands
    exit_code, stdout, stderr = run_command("python3 ffmpeg_cli.py --help")
    expected_commands = ["convert", "extract-audio", "resize", "info"]
    
    for cmd in expected_commands:
        if cmd in stdout:
            print(f"    ✓ Command '{cmd}' found in help")
        else:
            print(f"    ✗ Command '{cmd}' NOT found in help")
            return False
    
    return True


def main():
    """Run all tests."""
    print("FFmpeg CLI Test Suite")
    print("=" * 50)
    
    # Change to the directory containing the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    tests = [
        test_help_commands,
        test_error_handling,
        test_cli_structure
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                print(f"  Test {test.__name__} failed!")
        except Exception as e:
            print(f"  Test {test.__name__} raised exception: {e}")
    
    print("\n" + "=" * 50)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())