from audio_separator import Separator

class StemProcessor:
    def __init__(self):
        self.separator = Separator(model_name='UVR_MDXNET_KARA_2')
    
    def process_track(self, file_path):
        return self.separator.separate(file_path)
