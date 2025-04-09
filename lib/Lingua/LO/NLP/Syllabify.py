import re
from .Data import get_sylre_basic, get_sylre_full, normalize_tone_marks
from unicodedata import normalize

class Syllabify:
    def __init__(self, text, normalize=False):
        if not text:
            raise ValueError("`text` argument missing or undefined")
        self.text = normalize('NFC', text)
        if normalize:
            normalize_tone_marks(self.text)

    def get_syllables(self):
        syl_re = get_sylre_full()
        return re.findall(syl_re, self.text)

    def get_fragments(self):
        syl_re = get_sylre_full()
        basic_re = get_sylre_basic()
        fragments = []
        pos = 0
        while pos < len(self.text):
            match = re.match(syl_re, self.text[pos:])
            if match:
                fragments.append({'text': match.group(), 'is_lao': True})
                pos += len(match.group())
            else:
                non_lao_match = re.match(r'.+?(?=' + syl_re.pattern + r'|$)', self.text[pos:])
                if non_lao_match:
                    fragments.append({'text': non_lao_match.group(), 'is_lao': False})
                    pos += len(non_lao_match.group())
                else:
                    pos += 1
        return fragments
