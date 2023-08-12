from src.media import Image, Video


class MediaComparer:
    def __init__(self, threads: int, images: list[Image], videos: list[Video]):
        self.threads = threads
        self.images = images
        self.videos = videos
        
    def find_duplicates(self):
        self.find_duplicate_images()
        self.find_duplicate_videos()

    def find_duplicate_images(self):
        pass

    def find_duplicate_videos(self):
        pass
        