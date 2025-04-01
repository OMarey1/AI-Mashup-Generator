from pydub import AudioSegment

class CrossfadeEngine:
    def arabic_style_fade(self, track1, track2, duration=3000):
        return track1.append(track2, crossfade=duration)
