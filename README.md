# AI Music Recommendation System

## Overview
This project is an AI-powered music recommendation system that detects user emotions and suggests music tracks accordingly. It leverages emotion detection and music playback modules to provide a personalized listening experience.

## Features
- **Emotion Detection:** Analyzes user emotions using computer vision.
- **Music Recommendation:** Suggests music tracks based on detected emotions.
- **Music Player:** Plays recommended tracks directly within the application.

## Project Structure
- `main.py` — Entry point for the application.
- `emotion_detection.py` — Handles emotion detection logic.
- `music_player.py` — Manages music playback functionality.
- `env/` — Python virtual environment and dependencies.

## Setup Instructions
1. **Clone the repository:**
   ```cmd
   git clone <repository-url>
   cd "ai music recommendation"
   ```
2. **Create and activate a virtual environment:**
   ```cmd
   python -m venv env
   env\Scripts\activate
   ```
3. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```
4. **Run the application:**
   ```cmd
   python main.py
   ```

## Requirements
- Python 3.9 or higher
- See `requirements.txt` for all dependencies

## Usage
1. Start the application.
2. The system will detect your emotion and recommend music accordingly.
3. Enjoy the personalized music experience!

## License
This project is for educational purposes.
