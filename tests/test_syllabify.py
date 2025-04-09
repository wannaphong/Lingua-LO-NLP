import unittest
from lib.Lingua.LO.NLP.Syllabify import Syllabify

class TestSyllabify(unittest.TestCase):

    def test_get_syllables(self):
        tests = {
            "": [],
            "ສະບາຍດີ": ["ສະ", "ບາຍ", "ດີ"],
            "ກວ່າດອກ": ["ກວ່າ", "ດອກ"],
            "ເພື່ອນ": ["ເພື່ອນ"],
            "ກວ່າດອກ໐໑໒໓": ["ກວ່າ", "ດອກ", "໐໑໒໓"],
            "ຄຳດີ": ["ຄຳ", "ດີ"],
            "ຄໍາດີ": ["ຄໍາ", "ດີ"],
            "ຄໍາູດີ": ["ດີ"],
            "ກັ": [],
            "ກັນ": ["ກັນ"],
            "ກັວນ": ["ກັວນ"],
            "ກົ": [],
            "ກົດ": ["ກົດ"],
            "ກັອກ": [],
            "ແປຽ": ["ແປຽ"],
            "ເກັາະ": [],
            "ມື້ນີ້": ["ມື້", "ນີ້"],
            "ມະນຸດທຸກຄົນເກີດມາມີກຽດສັກສີ/ສິດທິ/ເສຣີພາບແລະຄວາມສເມີພາບເທົ່າທຽມກັນ. ທຸກໆຄົນມີເຫດຜົນແລະຄວາມຄິດຄວາມເຫັນສ່ວນຕົວຂອງໃຜຂອງມັນ/ແຕ່ວ່າມະນຸດທຸກໆຄົນຄວນປະພຶດຕໍ່ກັນຄືກັນກັບເປັນອ້າຍນ້ອງກັນ": [
                "ມະ", "ນຸດ", "ທຸກ", "ຄົນ", "ເກີດ", "ມາ", "ມີ", "ກຽດ", "ສັກ", "ສີ", "ສິດ", "ທິ", "ເສຣີ", "ພາບ", "ແລະ", "ເມີ", "ພາບ", "ເທົ່າ", "ທຽມ", "ກັນ", "ທຸກໆ", "ຄົນ", "ມີ", "ເຫດ", "ຜົນ", "ແລະ", "ຄວາມ", "ຄິດ", "ຄວາມ", "ເຫັນ", "ສ່ວນ", "ຕົວ", "ຂອງ", "ໃຜ", "ຂອງ", "ມັນ", "ແຕ່", "ວ່າ", "ມະ", "ນຸດ", "ທຸກໆ", "ຄົນ", "ຄວນ", "ປະ", "ພຶດ", "ຕໍ່", "ກັນ", "ຄື", "ກັນ", "ກັບ", "ເປັນ", "ອ້າຍ", "ນ້ອງ", "ກັນ"
            ]
        }

        for text, expected in tests.items():
            syllabify = Syllabify(text)
            self.assertEqual(syllabify.get_syllables(), expected)

    def test_get_fragments(self):
        tests = {
            'bla ສະບາຍ ດີ foo ດີ bar baz': [
                {'text': 'bla ', 'is_lao': False},
                {'text': 'ສະ', 'is_lao': True},
                {'text': 'ບາຍ', 'is_lao': True},
                {'text': ' ', 'is_lao': False},
                {'text': 'ດີ', 'is_lao': True},
                {'text': ' foo ', 'is_lao': False},
                {'text': 'ດີ', 'is_lao': True},
                {'text': ' bar baz', 'is_lao': False}
            ],
            "bla\nfoo ສະບາຍດີ\nbazດີ ເພື່ອນ": [
                {'text': "bla\nfoo ", 'is_lao': False},
                {'text': "ສະ", 'is_lao': True},
                {'text': "ບາຍ", 'is_lao': True},
                {'text': "ດີ", 'is_lao': True},
                {'text': "\nbaz", 'is_lao': False},
                {'text': "ດີ", 'is_lao': True},
                {'text': " ", 'is_lao': False},
                {'text': "ເພື່ອນ", 'is_lao': True}
            ],
            "ບ່ອນ\N{ZERO WIDTH SPACE}ຈອດ\N{ZERO WIDTH SPACE}ລົດ": [
                {'text': "ບ່ອນ", 'is_lao': True},
                {'text': "ຈອດ", 'is_lao': True},
                {'text': "ລົດ", 'is_lao': True}
            ]
        }

        for text, expected in tests.items():
            syllabify = Syllabify(text)
            self.assertEqual(syllabify.get_fragments(), expected)

if __name__ == '__main__':
    unittest.main()
