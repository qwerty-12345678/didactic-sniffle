from pic_to_ascii import AsciiConverter
import cv2 
from PIL import Image
import time
import os

class VideoAsciiConverter:
    def __init__(self, vid_path):
        self.video = cv2.VideoCapture(vid_path)

    def read_frames(self):
        self.ascii_frames = []
        while True:
            ret, frame = self.video.read()
            if not ret:
                break
            
            pil_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            converter = AsciiConverter(pil_frame)
            converter.to_grayscale()
            converter.resize()
            ascii_frame = converter.pixels_to_ascii()

            self.ascii_frames.append(ascii_frame)
        
        self.video.release()

    def play_ascii(self, fps=24):
        delay = 1 / fps
        for frame in self.ascii_frames:
            os.system('cls' if os.name == 'nt' else 'clear')  # clears terminal
            print(frame)
            time.sleep(delay)
                