import unittest
from lib.Lingua.LO.NLP.Romanize import Romanize

class TestRomanizePCGN(unittest.TestCase):

    def setUp(self):
        self.romanizer = Romanize(variant='PCGN', hyphen='-')
        self.romanizer_no_hyphen = Romanize(variant='PCGN', hyphen=' ')

    def test_romanize_pcgn(self):
        tests = [
            ('ເຄື່ອງກໍາເນີດໄຟຟ້າ', 'khuang-kam-neut-fai-fa'),
            ('ສະບາຍດີ', 'sa-bay-di'),
            ('ດີໆ', 'di-di'),
            ('ແຫນ', 'hèn'),
            ('ແໜ', 'nè'),
            ('ເຫັນ', 'hén'),
            ('ຫົກສິບ', 'hôk-sip'),
            ('ມື້ນີ້', 'mu-ni'),
            ('ມື້ວານນີ້', 'mu-van-ni'),
            ('ໃຫຍ່', 'gnai'),
            ('ຕົວ', 'toua'),
            ('ຄົນ', 'khôn'),
            ('ໃນວົງ', 'nai-vông'),
            ('ເຫຼົາ', 'lao'),
            ('ເຫງ', 'héng'),
            ('ຫວາດ', 'vat'),
            ('ເສລີ', 'sleu'),
            ('ຄວາມ', 'khoam'),
            ('ຫຼາຍ', 'lay'),
            ('ຊອຍ', 'xoy'),
            ('ສະບາຍດີ foo bar ສະ', 'sa-bay-di foo bar sa'),
            ('ຫນ່າງກັນຍຸງ', 'nang-kan-gnoung'),
            ('ພອຍໄພລິນ', 'phoy-phai-lin'),
            ('ຄ່ອຍໆ', 'khoy-khoy'),
            ('ມາຕີອາຊ໌', 'ma-ti-a'),
            ('ຫິວ', 'hiou'),
            ('ເພາະ', 'pho'),
            ('ແນວໃດ', 'nèo-dai'),
            ('ຂີ້ເຫຍື່ອ', 'khi-gnua'),
            ('ເຄີຍ', 'kheuy')
        ]

        for lao_text, expected_pcgn in tests:
            self.assertEqual(self.romanizer.romanize(lao_text), expected_pcgn)

    def test_romanize_pcgn_no_hyphen(self):
        tests = [
            ('ເຄື່ອງກໍາເນີດໄຟຟ້າ', 'khuang kam neut fai fa'),
            ('ສະບາຍດີ', 'sa bay di'),
            ('ດີໆ', 'di di'),
            ('ແຫນ', 'hèn'),
            ('ແໜ', 'nè'),
            ('ເຫັນ', 'hén'),
            ('ຫົກສິບ', 'hôk sip'),
            ('ມື້ນີ້', 'mu ni'),
            ('ມື້ວານນີ້', 'mu van ni'),
            ('ໃຫຍ່', 'gnai'),
            ('ຕົວ', 'toua'),
            ('ຄົນ', 'khôn'),
            ('ໃນວົງ', 'nai vông'),
            ('ເຫຼົາ', 'lao'),
            ('ເຫງ', 'héng'),
            ('ຫວາດ', 'vat'),
            ('ເສລີ', 'sleu'),
            ('ຄວາມ', 'khoam'),
            ('ຫຼາຍ', 'lay'),
            ('ຊອຍ', 'xoy'),
            ('ສະບາຍດີ foo bar ສະ', 'sa bay di foo bar sa'),
            ('ຫນ່າງກັນຍຸງ', 'nang kan gnoung'),
            ('ພອຍໄພລິນ', 'phoy phai lin'),
            ('ຄ່ອຍໆ', 'khoy khoy'),
            ('ມາຕີອາຊ໌', 'ma ti a'),
            ('ຫິວ', 'hiou'),
            ('ເພາະ', 'pho'),
            ('ແນວໃດ', 'nèo dai'),
            ('ຂີ້ເຫຍື່ອ', 'khi gnua'),
            ('ເຄີຍ', 'kheuy')
        ]

        for lao_text, expected_pcgn in tests:
            self.assertEqual(self.romanizer_no_hyphen.romanize(lao_text), expected_pcgn)

if __name__ == '__main__':
    unittest.main()
