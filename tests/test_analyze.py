import unittest
from lib.Lingua.LO.NLP.Analyze import Analyze

class TestAnalyze(unittest.TestCase):

    def test_analyze_syllable(self):
        tests = {
            'ກວກ': {'consonant': 'ກ', 'end_consonant': 'ກ', 'live': 0, 'tone': 'MID_FALLING', 'vowel': '◌ວ', 'vowel_length': 'long'},
            'ກວງ': {'consonant': 'ກ', 'end_consonant': 'ງ', 'live': 1, 'tone': 'LOW', 'vowel': '◌ວ', 'vowel_length': 'long'},
            'ກ່ວງ': {'consonant': 'ກ', 'end_consonant': 'ງ', 'live': 1, 'tone': 'MID', 'tone_mark': '່', 'vowel': '◌ວ', 'vowel_length': 'long'},
            'ກ່າ': {'consonant': 'ກ', 'tone': 'MID', 'live': 1, 'tone_mark': '່', 'vowel': '◌າ', 'vowel_length': 'long'},
            'ກ່າຍ': {'consonant': 'ກ', 'end_consonant': 'ຍ', 'live': 1, 'tone': 'MID', 'tone_mark': '່', 'vowel': '◌າ', 'vowel_length': 'long'},
            'ກໍ': {'consonant': 'ກ', 'live': 1, 'tone': 'LOW', 'vowel': '◌ໍ', 'vowel_length': 'long'},
            'ກໍ່': {'consonant': 'ກ', 'live': 1, 'tone': 'MID', 'tone_mark': '່', 'vowel': '◌ໍ', 'vowel_length': 'long'},
            'ກໍ໋': {'consonant': 'ກ', 'live': 1, 'tone': 'RISING', 'tone_mark': '໋', 'vowel': '◌ໍ', 'vowel_length': 'long'},
            'ແໜ': {'consonant': 'ໜ', 'live': 1, 'tone': 'RISING', 'vowel': 'ແ◌', 'vowel_length': 'long'},
            'ແຫນ': {'consonant': 'ຫ', 'end_consonant': 'ນ', 'live': 1, 'tone': 'RISING', 'vowel': 'ແ◌', 'vowel_length': 'long'},
            'ຫາມ': {'consonant': 'ຫ', 'end_consonant': 'ມ', 'live': 1, 'tone': 'RISING', 'vowel': '◌າ', 'vowel_length': 'long'},
            'ເກິ່ຍ': {'consonant': 'ກ', 'end_consonant': 'ຍ', 'live': 1, 'tone': 'MID', 'tone_mark': '່', 'vowel': 'ເ◌ິ', 'vowel_length': 'short'},
            'ກະ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ະ', 'vowel_length': 'short'},
            'ກາ': {'consonant': 'ກ', 'live': 1, 'tone': 'LOW', 'vowel': '◌າ', 'vowel_length': 'long'},
            'ກິ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ິ', 'vowel_length': 'short'},
            'ກີ': {'consonant': 'ກ', 'live': 1, 'tone': 'LOW', 'vowel': '◌ີ', 'vowel_length': 'long'},
            'ກຶ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ຶ', 'vowel_length': 'short'},
            'ກື': {'consonant': 'ກ', 'live': 1, 'tone': 'LOW', 'vowel': '◌ື', 'vowel_length': 'long'},
            'ກຸ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ຸ', 'vowel_length': 'short'},
            'ກູ': {'consonant': 'ກ', 'live': 1, 'tone': 'LOW', 'vowel': '◌ູ', 'vowel_length': 'long'},
            'ເກະ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': 'ເ◌ະ', 'vowel_length': 'short'},
            'ເກັນ': {'consonant': 'ກ', 'live': 1, 'end_consonant': 'ນ', 'tone': 'LOW', 'vowel': 'ເ◌ັ', 'vowel_length': 'short'},
            'ເກ': {'consonant': 'ກ', 'live': 1, 'tone': 'LOW', 'vowel': 'ເ◌', 'vowel_length': 'long'},
            'ແກະ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': 'ແ◌ະ', 'vowel_length': 'short'},
            'ແກັດ': {'consonant': 'ກ', 'end_consonant': 'ດ', 'live': 0, 'tone': 'HIGH', 'vowel': 'ແ◌ັ', 'vowel_length': 'short'},
            'ແກ': {'consonant': 'ກ', 'live': 1, 'tone': 'LOW', 'vowel': 'ແ◌', 'vowel_length': 'long'},
            'ໂກະ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': 'ໂ◌ະ', 'vowel_length': 'short'},
            'ໂກ': {'consonant': 'ກ', 'live': 1, 'tone': 'LOW', 'vowel': 'ໂ◌', 'vowel_length': 'long'},
            'ກັນ': {'consonant': 'ກ', 'end_consonant': 'ນ', 'live': 1, 'tone': 'LOW', 'vowel': '◌ັ', 'vowel_length': 'short'},
            'ກົດ': {'consonant': 'ກ', 'end_consonant': 'ດ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ົ', 'vowel_length': 'short'},
            'ເກາະ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': 'ເ◌າະ', 'vowel_length': 'short'},
            'ກອດ': {'consonant': 'ກ', 'end_consonant': 'ດ', 'live': 0, 'tone': 'MID_FALLING', 'vowel': '◌ອ', 'vowel_length': 'long'},
            'ເກິ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': 'ເ◌ິ', 'vowel_length': 'short'},
            'ເກີ': {'consonant': 'ກ', 'live': 1, 'tone': 'LOW', 'vowel': 'ເ◌ີ', 'vowel_length': 'long'},
            'ເກຍ': {'consonant': 'ກ', 'end_consonant': 'ຍ', 'live': 1, 'tone': 'LOW', 'vowel': 'ເ◌', 'vowel_length': 'long'},
            'ເກົາ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': 'ເ◌ົາ', 'vowel_length': 'short'},
            'ເກຶອ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': 'ເ◌ຶອ', 'vowel_length': 'short'},
            'ເກືອ': {'consonant': 'ກ', 'live': 1, 'tone': 'LOW', 'vowel': 'ເ◌ືອ', 'vowel_length': 'long'},
            'ກວດ': {'consonant': 'ກ', 'end_consonant': 'ດ', 'live': 0, 'tone': 'MID_FALLING', 'vowel': '◌ວ', 'vowel_length': 'long'},
            'ກັວກ': {'consonant': 'ກ', 'end_consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ັວ', 'vowel_length': 'short'},
            'ໄກ': {'consonant': 'ກ', 'live': 1, 'tone': 'LOW', 'vowel': 'ໄ◌', 'vowel_length': 'long'},
            'ໃນ': {'consonant': 'ນ', 'live': 1, 'tone': 'HIGH', 'vowel': 'ໃ◌', 'vowel_length': 'long'},
            'ກາຍ': {'consonant': 'ກ', 'end_consonant': 'ຍ', 'live': 1, 'tone': 'LOW', 'vowel': '◌າ', 'vowel_length': 'long'},
            'ກັຍ': {'consonant': 'ກ', 'end_consonant': 'ຍ', 'live': 1, 'tone': 'LOW', 'vowel': '◌ັ', 'vowel_length': 'short'},
            'ແປຽ': {'consonant': 'ປ', 'live': 0, 'tone': 'HIGH', 'vowel': 'ແ◌ຽ', 'vowel_length': 'short'},
            'ກໍາ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ໍາ', 'vowel_length': 'short'},
            'ກຳ': {'consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ຳ', 'vowel_length': 'short'},
            'ກຽດ': {'consonant': 'ກ', 'end_consonant': 'ດ', 'live': 0, 'tone': 'MID_FALLING', 'vowel': '◌ຽ', 'vowel_length': 'long'},
            'ຈື່ງ': {'consonant': 'ຈ', 'end_consonant': 'ງ', 'live': 1, 'tone': 'MID', 'tone_mark': '່', 'vowel': '◌ື', 'vowel_length': 'long'},
            'ຊັນ': {'consonant': 'ຊ', 'end_consonant': 'ນ', 'live': 1, 'tone': 'HIGH', 'vowel': '◌ັ', 'vowel_length': 'short'},
            'ຊົ່ວ': {'consonant': 'ຊ', 'end_consonant': 'ວ', 'live': 1, 'tone': 'MID', 'tone_mark': '່', 'vowel': '◌ົ', 'vowel_length': 'short'},
            'ຍະ': {'consonant': 'ຍ', 'live': 0, 'tone': 'MID', 'vowel': '◌ະ', 'vowel_length': 'short'},
            'ດີ': {'consonant': 'ດ', 'live': 1, 'tone': 'LOW', 'vowel': '◌ີ', 'vowel_length': 'long'},
            'ດ້ວຍ': {'consonant': 'ດ', 'end_consonant': 'ຍ', 'live': 1, 'tone': 'HIGH_FALLING', 'tone_mark': '້', 'vowel': '◌ວ', 'vowel_length': 'long'},
            'ຕິ': {'consonant': 'ຕ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ິ', 'vowel_length': 'short'},
            'ຕົນ': {'consonant': 'ຕ', 'end_consonant': 'ນ', 'live': 1, 'tone': 'LOW', 'vowel': '◌ົ', 'vowel_length': 'short'},
            'ຕ້ອງ': {'consonant': 'ຕ', 'end_consonant': 'ງ', 'live': 1, 'tone': 'HIGH_FALLING', 'tone_mark': '້', 'vowel': '◌ອ', 'vowel_length': 'long'},
            'ຕໍ່': {'consonant': 'ຕ', 'live': 1, 'tone': 'MID', 'tone_mark': '່', 'vowel': '◌ໍ', 'vowel_length': 'long'},
            'ທາງ': {'consonant': 'ທ', 'end_consonant': 'ງ', 'live': 1, 'tone': 'HIGH', 'vowel': '◌າ', 'vowel_length': 'long'},
            'ທຳ': {'consonant': 'ທ', 'live': 0, 'tone': 'MID', 'vowel': '◌ຳ', 'vowel_length': 'short'},
            'ນຸດ': {'consonant': 'ນ', 'end_consonant': 'ດ', 'live': 0, 'tone': 'MID', 'vowel': '◌ຸ', 'vowel_length': 'short'},
            'ນ້ອງ': {'consonant': 'ນ', 'end_consonant': 'ງ', 'live': 1, 'tone': 'HIGH_FALLING', 'tone_mark': '້', 'vowel': '◌ອ', 'vowel_length': 'long'},
            'ປະ': {'consonant': 'ປ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ະ', 'vowel_length': 'short'},
            'ປັດ': {'consonant': 'ປ', 'end_consonant': 'ດ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ັ', 'vowel_length': 'short'},
            'ພາບ': {'consonant': 'ພ', 'end_consonant': 'ບ', 'live': 0, 'tone': 'HIGH_FALLING', 'vowel': '◌າ', 'vowel_length': 'long'},
            'ພີ່': {'consonant': 'ພ', 'live': 1, 'tone': 'MID', 'tone_mark': '່', 'vowel': '◌ີ', 'vowel_length': 'long'},
            'ພຶດ': {'consonant': 'ພ', 'end_consonant': 'ດ', 'live': 0, 'tone': 'MID', 'vowel': '◌ຶ', 'vowel_length': 'short'},
            'ມະ': {'consonant': 'ມ', 'live': 0, 'tone': 'MID', 'vowel': '◌ະ', 'vowel_length': 'short'},
            'ມາ': {'consonant': 'ມ', 'live': 1, 'tone': 'HIGH', 'vowel': '◌າ', 'vowel_length': 'long'},
            'ມີ': {'consonant': 'ມ', 'live': 1, 'tone': 'HIGH', 'vowel': '◌ີ', 'vowel_length': 'long'},
            'ສະ': {'consonant': 'ສ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ະ', 'vowel_length': 'short'},
            'ສັກ': {'consonant': 'ສ', 'end_consonant': 'ກ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ັ', 'vowel_length': 'short'},
            'ສຳ': {'consonant': 'ສ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ຳ', 'vowel_length': 'short'},
            'ສິດ': {'consonant': 'ສ', 'end_consonant': 'ດ', 'live': 0, 'tone': 'HIGH', 'vowel': '◌ິ', 'vowel_length': 'short'},
            'ຮູ້': {'consonant': 'ຮ', 'live': 1, 'tone': 'HIGH_FALLING', 'tone_mark': '້', 'vowel': '◌ູ', 'vowel_length': 'long'},
            'ເກີດ': {'consonant': 'ກ', 'end_consonant': 'ດ', 'live': 0, 'tone': 'MID_FALLING', 'vowel': 'ເ◌ີ', 'vowel_length': 'long'},
            'ເໝີ': {'consonant': 'ໝ', 'live': 1, 'tone': 'RISING', 'vowel': 'ເ◌ີ', 'vowel_length': 'long'},
            'ແລະ': {'consonant': 'ລ', 'live': 0, 'tone': 'MID', 'vowel': 'ແ◌ະ', 'vowel_length': 'short'},
            'ໂນ': {'consonant': 'ນ', 'live': 1, 'tone': 'HIGH', 'vowel': 'ໂ◌', 'vowel_length': 'long'},
            'ໃກ': {'consonant': 'ກ', 'live': 1, 'tone': 'LOW', 'vowel': 'ໃ◌', 'vowel_length': 'long'},
            'ໜ້າ': {'consonant': 'ໜ', 'live': 1, 'tone': 'MID_FALLING', 'tone_mark': '້', 'vowel': '◌າ', 'vowel_length': 'long'},
            'ເຫດ': {'consonant': 'ຫ', 'end_consonant': 'ດ', 'live': 0, 'tone': 'MID_FALLING', 'vowel': 'ເ◌', 'vowel_length': 'long'},
            'ເອື້ອຢ': {'consonant': 'ອ', 'end_consonant': 'ຢ', 'live': 1, 'tone': 'HIGH_FALLING', 'tone_mark': '້', 'vowel': 'ເ◌ືອ', 'vowel_length': 'long'},
            'ສວນ': {'consonant': 'ສ', 'end_consonant': 'ນ', 'live': 1, 'tone': 'RISING', 'vowel': '◌ວ', 'vowel_length': 'long'}
        }

        for syllable, expected in tests.items():
            analysis = Analyze(syllable)
            for key, value in expected.items():
                self.assertEqual(getattr(analysis, key), value)

    def test_tone(self):
        tone_tests = {
            'ກາ': 'LOW',
            'ຄາ': 'HIGH',
            'ຂາ': 'RISING',
            'ກ່າ': 'MID',
            'ຄ່າ': 'MID',
            'ຂ່າ': 'MID',
            'ກ້າ': 'HIGH_FALLING',
            'ຄ້າ': 'HIGH_FALLING',
            'ຂ້າ': 'MID_FALLING',
            'ກ໊າ': 'HIGH',
            'ຄ໊າ': 'HIGH',
            'ຂ໊າ': 'HIGH',
            'ກ໋າ': 'RISING',
            'ຄ໋າ': 'RISING',
            'ຂ໋າ': 'RISING',
            'ກະ': 'HIGH',
            'ຄະ': 'MID',
            'ຂະ': 'HIGH'
        }

        for syllable, expected_tone in tone_tests.items():
            analysis = Analyze(syllable)
            self.assertEqual(analysis.tone, expected_tone)

if __name__ == '__main__':
    unittest.main()
