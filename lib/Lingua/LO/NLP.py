import re
from .Syllabify import Syllabify
from .Analyze import Analyze
from .Romanize import Romanize

class LaoNLP:
    def __init__(self, normalize=False):
        self.normalize = normalize

    def split_to_syllables(self, text, **options):
        syllabifier = Syllabify(text, normalize=self.normalize, **options)
        return syllabifier.get_syllables()

    def analyze_syllable(self, syllable, **options):
        return Analyze(syllable, normalize=self.normalize, **options)

    def romanize(self, text, **options):
        options.setdefault('variant', 'PCGN')
        romanizer = Romanize(**options)
        return romanizer.romanize(text)
