import librosa

class ArabicKeyAnalyzer:
    def detect_maqam(self, audio_path):
        y, sr = librosa.load(audio_path)
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr, bins_per_octave=48)
        return self._map_to_maqam(chroma.mean(axis=1))
