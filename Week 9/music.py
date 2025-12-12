import json
import random
import os

class MusicRecommender:
    def __init__(self):
        with open(r"E:/Python/CS50x/Week 9/project/data/music.json", "r") as file:
            self.music_data = json.load(file)

        self.music_folder = r"E:/Python/CS50x/Week 9/project/music"

    def recommend_music(self, category):
        filename = random.choice(self.music_data[category])
        
        if os.path.isabs(filename):
            return filename

        return os.path.join(self.music_folder, filename)
