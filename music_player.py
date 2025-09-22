import os
from dotenv import load_dotenv
import pywhatkit

load_dotenv()

class MusicPlayer:
    def __init__(self):
        self.music_path = os.getenv('music_path', None)
        self.found_music = []


    def get_files_with_extension(self, directory: str, extensions: list[str] = [".mp3"]):
        self.found_music = []
        for filename in os.listdir(directory):
            for extension in extensions:
                if filename.endswith(extension):
                    self.found_music.append(os.path.join(directory, filename))
        return self.found_music
    
                
    def play_music(self, emotion: str, method: str ="online"):
        if method == "online":
            try:
                search_query = {
                    "happy": "happy trending hindi songs",
                    "sad": "heart touching hindi songs",
                    "angry": "relax hindi music songs"
                }
                if emotion not in search_query.keys():
                    raise ValueError("Invalid emotion provided")
                pywhatkit.playonyt(search_query[emotion], use_api=False)
                return True
            except Exception as e:
                print(e)
                return False

        else: # runs locally
            try:
                files = self.get_files_with_extension(os.path.join(self.music_path, emotion), [".mp3", ".wav", "m4a"])
                if not files:
                    raise FileNotFoundError("No music found for the given emotion")
                file_path = files[0]
                os.startfile(file_path)
                return True
            except Exception as e:
                print(e)
                return False