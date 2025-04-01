from audio_separator.separator import Separator

class StemProcessor:
    def __init__(self):
        self.separator = Separator()
        self.separator.load_model(model_filename='UVR_MDXNET_KARA_2.onnx)
    
    def process_track(self, file_path):
        return self.separator.separate(file_path)
