# importing the libraries
from deepface import DeepFace
import cv2
import os
from dotenv import load_dotenv

# loading the environment variables
load_dotenv()

video_source = os.getenv("video_source", 0)

class DetectEmotion:
    def __init__(self):
        self.video_source = int(video_source)

    def save_image(self, image):
        cv2.imwrite('image.jpg', image)

    def capture_image(self):
        cap = cv2.VideoCapture(self.video_source)
        ret, frame = cap.read()
        
        if not ret:
            print('Unable to capture image')
            return
        else:
            cap.release()
            cv2.destroyAllWindows()
            self.save_image(frame)
        
   
    def detect_emotion(self):
        try:
            image = cv2.imread('image.jpg')
            emotion = DeepFace.analyze(image, actions=['emotion'], enforce_detection=False)[0]['dominant_emotion']
            if emotion in ['neutral', 'fear']:
                return 'sad'
            else:
                return emotion
        except Exception as e:
            print("DeepFace error")
            return False