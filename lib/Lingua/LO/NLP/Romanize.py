import re
from .Analyze import Analyze
from .Syllabify import Syllabify

class Romanize:
    def __init__(self, variant, hyphen=None, normalize=False, **kwargs):
        self.variant = variant
        self.hyphen = hyphen if hyphen is not None else ' '
        self.normalize = normalize
        self.kwargs = kwargs

        if variant == 'PCGN':
            from .Romanize_PCNG import RomanizePCGN
            self.romanizer = RomanizePCGN(**kwargs)
        elif variant == 'IPA':
            from .Romanize_IPA import RomanizeIPA
            self.romanizer = RomanizeIPA(**kwargs)
        else:
            raise ValueError(f"Unknown variant: {variant}")

    def romanize(self, text):
        result = ''
        fragments = Syllabify(text, normalize=self.normalize).get_fragments()
        for fragment in fragments:
            if fragment['is_lao']:
                result += self.hyphen.join(self.romanizer.romanize_syllable(fragment['text']))
            else:
                result += fragment['text']
        return result

    def romanize_syllable(self, syllable):
        if not isinstance(syllable, Analyze):
            syllable = Analyze(syllable)
        return self.romanizer.romanize_syllable(syllable)
