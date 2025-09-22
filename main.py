from emotion_detection import DetectEmotion
from music_player import MusicPlayer

def main():
    detect_emotion = DetectEmotion()
    player = MusicPlayer()

    detect_emotion.capture_image()
    emotion = detect_emotion.detect_emotion()

    print(f"Emotion detected: {emotion}")

    if player.play_music(emotion):
        print("Music played successfully")
    else:
        print("Music playback failed")

if __name__ == '__main__':
    main()