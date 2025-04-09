import re
from .Data import get_sylre_named, is_long_vowel, normalize_tone_marks

SUNG = 0  # "high class"
KANG = 1  # "middle class"
TAM = 2   # "low class"

TONE_MARKS = {
    "\u0ec9": ["MID", "MID", "MID"],
    "\u0eca": ["MID_FALLING", "HIGH_FALLING", "HIGH_FALLING"],
    "\u0ecb": ["HIGH", "HIGH", "HIGH"],
    "\u0ecc": ["RISING", "RISING", "RISING"],
}

TONE_NOMARK = [
    ["RISING", "HIGH", "MID_FALLING"],  # SUNG/high
    ["LOW", "HIGH", "MID_FALLING"],     # KANG/mid
    ["HIGH", "MID", "HIGH_FALLING"],    # TAM/low
]

CONSONANTS = {
    'ກ': KANG, 'ຂ': SUNG, 'ຄ': TAM, 'ງ': TAM, 'ຈ': KANG, 'ສ': SUNG, 'ຊ': TAM, 'ຍ': TAM,
    'ດ': KANG, 'ຕ': KANG, 'ຖ': SUNG, 'ທ': TAM, 'ນ': TAM, 'ບ': KANG, 'ປ': KANG, 'ຜ': SUNG,
    'ຝ': SUNG, 'ພ': TAM, 'ຟ': TAM, 'ມ': TAM, 'ຢ': KANG, 'ລ': TAM, 'ວ': TAM, 'ຫ': SUNG,
    'ອ': KANG, 'ຮ': TAM, 'ຣ': TAM, 'ຫງ': SUNG, 'ຫຍ': SUNG, 'ຫນ': SUNG, 'ໜ': SUNG,
    'ຫມ': SUNG, 'ໝ': SUNG, 'ຫລ': SUNG, 'ຫຼ': SUNG, 'ຫວ': SUNG,
}

CONS_H_MNL = {'ມ': 'ໝ', 'ນ': 'ໜ', 'ລ': "\u0ec4"}
ENDCONS_STOP = {'ກ': 1, 'ດ': 1, 'ບ': 1}

class Analyze:
    def __init__(self, syllable, normalize=False):
        if normalize:
            syllable = normalize_tone_marks(syllable)
        self.syllable = syllable
        self.parse = self._classify(syllable)

    def _classify(self, s):
        if not s:
            raise ValueError("`syllable` argument missing or undefined")

        sylre_named = get_sylre_named()
        match = re.match(sylre_named, s)
        if not match:
            raise ValueError(f"`{s}` does not start with a valid syllable")

        class_dict = {
            'syllable': s,
            'parse': match.groupdict()
        }

        consonant = match.group('consonant')
        end_consonant = match.group('end_consonant')
        h = match.group('h')
        semivowel = match.group('semivowel')
        tone_mark = match.group('tone_mark')

        vowels = [match.group('vowel0') or '']
        vowels.append("\u25cc")
        vowels.extend(filter(None, [match.group('vowel1'), match.group('vowel2'), match.group('vowel3')]))
        class_dict['vowel'] = ''.join(vowels)

        cc = CONSONANTS.get(consonant)
        if h:
            cc = SUNG
            if consonant in CONS_H_MNL and not match.group('vowel0'):
                class_dict['consonant'] = CONS_H_MNL[consonant]
                h = None
            else:
                if consonant not in ['ວ', 'ຍ']:
                    end_consonant = consonant
                    consonant = 'ຫ'
                    h = None

        long_vowel = is_long_vowel(class_dict['vowel'])
        class_dict['vowel_length'] = 'long' if long_vowel else 'short'

        live = 1 if end_consonant and end_consonant not in ENDCONS_STOP else long_vowel
        class_dict['live'] = live

        if tone_mark:
            class_dict['tone'] = TONE_MARKS[tone_mark][cc]
        else:
            class_dict['tone'] = TONE_NOMARK[cc][0 if live else long_vowel + 1]

        class_dict['consonant'] = consonant
        if end_consonant:
            class_dict['end_consonant'] = end_consonant

        return class_dict

    def __getattr__(self, name):
        if name in self.parse:
            return self.parse[name]
        raise AttributeError(f"'Analyze' object has no attribute '{name}'")
