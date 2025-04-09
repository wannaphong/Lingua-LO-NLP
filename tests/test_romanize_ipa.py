import unittest
from lib.Lingua.LO.NLP.Romanize import Romanize

class TestRomanizeIPA(unittest.TestCase):

    def setUp(self):
        self.romanizer_tone = Romanize(variant='IPA', tone=True)
        self.romanizer_no_tone = Romanize(variant='IPA', tone=False)

    def test_romanize_ipa(self):
        tests = [
            ('ເຄື່ອງກໍາເນີດໄຟຟ້າ', 'kʰɯ̄ːəŋ kám nɤ̂ːt fáj fâː'),
            ('ສະບາຍດີ', 'sáʔ bàːj dìː'),
            ('ດີໆ', 'dìː-dìː'),
            ('ເລື້ອຍໆ', 'lɯ̂ːəi-lɯ̂ːəi'),
            ('ແນວໃດ', 'nɛ́ːw dàj'),
            ('ທີ່ສຸດ', 'tʰīː sút')
        ]

        for lao_text, expected_ipa in tests:
            self.assertEqual(self.romanizer_tone.romanize(lao_text), expected_ipa)

    def test_romanize_ipa_no_tone(self):
        tests = [
            ('ເຄື່ອງກໍາເນີດໄຟຟ້າ', 'kʰɯːəŋ kam nɤːt faj faː'),
            ('ສະບາຍດີ', 'saʔ baːj diː'),
            ('ດີໆ', 'diː-diː'),
            ('ເລື້ອຍໆ', 'lɯːəi-lɯːəi'),
            ('ແນວໃດ', 'nɛːw daj'),
            ('ທີ່ສຸດ', 'tʰiː sut')
        ]

        for lao_text, expected_ipa in tests:
            self.assertEqual(self.romanizer_no_tone.romanize(lao_text), expected_ipa)

if __name__ == '__main__':
    unittest.main()
