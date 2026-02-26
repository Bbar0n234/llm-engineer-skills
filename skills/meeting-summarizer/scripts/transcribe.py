#!/usr/bin/env python3
"""
Meeting Transcription Script

Usage:
    python transcribe.py <audio_or_video_file>

Output:
    Creates transcript.txt in the same directory as input file.
    Format: "Спикер A: текст\nСпикер B: текст\n..."
"""

import os
import sys
from pathlib import Path

ASSEMBLYAI_API_KEY = os.environ.get("ASSEMBLYAI_API_KEY")
if not ASSEMBLYAI_API_KEY:
    print("Error: ASSEMBLYAI_API_KEY environment variable is not set.")
    print("Set it with: export ASSEMBLYAI_API_KEY='your-key-here'")
    sys.exit(1)

VIDEO_EXT = {'.mp4', '.mov', '.avi', '.mkv', '.webm'}
AUDIO_EXT = {'.mp3', '.wav', '.m4a', '.ogg', '.flac', '.aac', '.opus'}


def extract_audio(video_path: Path) -> Path:
    """Extract audio from video file using ffmpeg, returns path to mp3."""
    import subprocess

    audio_path = video_path.with_suffix('.mp3')
    print(f"Extracting audio: {video_path} -> {audio_path}")

    result = subprocess.run(
        ["ffmpeg", "-i", str(video_path), "-vn", "-acodec", "libmp3lame", "-q:a", "2", str(audio_path), "-y"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Error extracting audio: {result.stderr}")
        sys.exit(1)

    return audio_path


def prepare_audio(source_path: Path) -> Path:
    """
    Prepare audio for transcription.
    - Video files: extract audio
    - Audio files: return as-is
    """
    if not source_path.exists():
        print(f"Error: File not found: {source_path}")
        sys.exit(1)

    ext = source_path.suffix.lower()

    if ext in VIDEO_EXT:
        return extract_audio(source_path)
    elif ext in AUDIO_EXT:
        print(f"Using audio directly: {source_path}")
        return source_path
    else:
        print(f"Error: Unknown file type: {ext}")
        print(f"Supported video: {VIDEO_EXT}")
        print(f"Supported audio: {AUDIO_EXT}")
        sys.exit(1)


def transcribe(audio_path: Path) -> str:
    """Transcribe audio using AssemblyAI with speaker diarization."""
    try:
        import assemblyai as aai
    except ImportError:
        print("Error: assemblyai not installed. Run: pip install assemblyai")
        sys.exit(1)

    aai.settings.api_key = ASSEMBLYAI_API_KEY

    config = aai.TranscriptionConfig(
        speech_model="universal",
        speaker_labels=True,
        language_code="ru",
    )

    transcriber = aai.Transcriber()

    print("Starting transcription...")
    transcript = transcriber.transcribe(str(audio_path), config=config)

    if transcript.status == aai.TranscriptStatus.error:
        print(f"Transcription error: {transcript.error}")
        sys.exit(1)

    print("Transcription completed.")

    # Format with speaker labels
    formatted = ""
    if transcript.utterances:
        for utterance in transcript.utterances:
            formatted += f"Спикер {utterance.speaker}: {utterance.text}\n"
    elif transcript.text:
        formatted = transcript.text

    return formatted


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    source_path = Path(sys.argv[1]).resolve()
    audio_path = prepare_audio(source_path)

    transcript_text = transcribe(audio_path)

    # Save transcript next to original file
    output_path = source_path.parent / "transcript.txt"
    output_path.write_text(transcript_text, encoding='utf-8')

    print(f"\nTranscript saved: {output_path}")
    print(f"Length: {len(transcript_text)} characters")


if __name__ == "__main__":
    main()
