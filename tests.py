import unittest
from unittest.mock import patch

from SPM2 import kysy_luku, hae_lomakkeesta, valitse_asteikko, valitse_lomake, laske_st_pisteet, tee_tulkinta


class TestKysyLuku(unittest.TestCase):
    @patch('builtins.input', side_effect=['25'])
    def test_valid_input(self, mock_input):
        self.assertEqual(kysy_luku(), 25)

    @patch('builtins.input', side_effect=['5'])
    def test_below_range(self, mock_input):
        self.assertIsNone(kysy_luku())

    @patch('builtins.input', side_effect=['45'])
    def test_above_range(self, mock_input):
        self.assertIsNone(kysy_luku())

    @patch('builtins.input', side_effect=['invalid'])
    def test_invalid_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.assertIsNone(kysy_luku())
            mock_print.assert_called_with("Arvon tulee olla kokonaisluku.")


class TestHaeLomakkeesta(unittest.TestCase):
    # Kodin lomake
    def test_kodin_lomake_nako_valid_input_returns_correct_values(self):
        test_cases = [
            # (ikä, lomake, asteikko, luku, expected_output)
            ("lapsi", "kodin lomake", "näkö", 16, (60, "84")),  # normal case
            ("lapsi", "kodin lomake", "näkö", 10, (40, "16")),  # minimum value
            ("lapsi", "kodin lomake", "näkö", 40, (80, ">99")), # maximum value
            ("lapsi", "kodin lomake", "näkö", 50, None) # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_kodin_lomake_kuulo_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "kodin lomake", "kuulo", 16, (60, "84")), # normal case
            ("lapsi", "kodin lomake", "kuulo", 10, (40, "16")), # minimum value
            ("lapsi", "kodin lomake", "kuulo", 40, (80, ">99")), # maximum value
            ("lapsi", "kodin lomake", "kuulo", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_kodin_lomake_tunto_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "kodin lomake", "tunto", 16, (59, "82")), # normal case
            ("lapsi", "kodin lomake", "tunto", 10, (40, "16")), # minimum value
            ("lapsi", "kodin lomake", "tunto", 40, (80, ">99")), # maximum value
            ("lapsi", "kodin lomake", "tunto", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_kodin_lomake_makujahaju_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "kodin lomake", "maku ja haju", 16, (57, "76")), # normal case
            ("lapsi", "kodin lomake", "maku ja haju", 10, (40, "16")), # minimum value
            ("lapsi", "kodin lomake", "maku ja haju", 40, (80, ">99")), # maximum value
            ("lapsi", "kodin lomake", "maku ja haju", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_kodin_lomake_kehotietoisuus_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "kodin lomake", "kehotietoisuus", 16, (57, "76")), # normal case
            ("lapsi", "kodin lomake", "kehotietoisuus", 10, (40, "16")), # minimum value
            ("lapsi", "kodin lomake", "kehotietoisuus", 40, (80, ">99")), # maximum value
            ("lapsi", "kodin lomake", "kehotietoisuus", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_kodin_lomake_tasapainojaliike_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "kodin lomake", "tasapaino ja liike", 16, (63, "90")), # normal case
            ("lapsi", "kodin lomake", "tasapaino ja liike", 10, (41, "18")), # minimum value
            ("lapsi", "kodin lomake", "tasapaino ja liike", 40, (80, ">99")), # maximum value
            ("lapsi", "kodin lomake", "tasapaino ja liike", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_kodin_lomake_suunnittelujaoivallukset_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "kodin lomake", "suunnittelu ja oivallukset", 16, (56, "73")), # normal case
            ("lapsi", "kodin lomake", "suunnittelu ja oivallukset", 10, (40, "16")), # minimum value
            ("lapsi", "kodin lomake", "suunnittelu ja oivallukset", 40, (80, ">99")), # maximum value
            ("lapsi", "kodin lomake", "suunnittelu ja oivallukset", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_kodin_lomake_sosiaalinenosallistuminen_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "kodin lomake", "sosiaalinen osallistuminen", 16, (50, "50")), # normal case
            ("lapsi", "kodin lomake", "sosiaalinen osallistuminen", 10, (40, "16")), # minimum value
            ("lapsi", "kodin lomake", "sosiaalinen osallistuminen", 40, (80, ">99")), # maximum value
            ("lapsi", "kodin lomake", "sosiaalinen osallistuminen", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    # Koulun lomake
    def test_koulun_lomake_nako_valid_input_returns_correct_values(self):
        test_cases = [
            # (ikä, lomake, asteikko, luku, expected_output)
            ("lapsi", "koulun lomake", "näkö", 16, (58, "79")),  # normal case
            ("lapsi", "koulun lomake", "näkö", 10, (40, "16")),  # minimum value
            ("lapsi", "koulun lomake", "näkö", 40, (80, ">99")), # maximum value
            ("lapsi", "koulun lomake", "näkö", 50, None) # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_koulun_lomake_kuulo_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "koulun lomake", "kuulo", 16, (60, "84")), # normal case
            ("lapsi", "koulun lomake", "kuulo", 10, (40, "16")), # minimum value
            ("lapsi", "koulun lomake", "kuulo", 40, (80, ">99")), # maximum value
            ("lapsi", "koulun lomake", "kuulo", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_koulun_lomake_tunto_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "koulun lomake", "tunto", 16, (70, "98")), # normal case
            ("lapsi", "koulun lomake", "tunto", 10, (43, "24")), # minimum value
            ("lapsi", "koulun lomake", "tunto", 40, (80, ">99")), # maximum value
            ("lapsi", "koulun lomake", "tunto", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_koulun_lomake_makujahaju_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "koulun lomake", "maku ja haju", 16, (71, "98")), # normal case
            ("lapsi", "koulun lomake", "maku ja haju", 10, (44, "27")), # minimum value
            ("lapsi", "koulun lomake", "maku ja haju", 40, (80, ">99")), # maximum value
            ("lapsi", "koulun lomake", "maku ja haju", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_koulun_lomake_kehotietoisuus_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "koulun lomake", "kehotietoisuus", 16, (65, "93")), # normal case
            ("lapsi", "koulun lomake", "kehotietoisuus", 10, (43, "24")), # minimum value
            ("lapsi", "koulun lomake", "kehotietoisuus", 40, (80, ">99")), # maximum value
            ("lapsi", "koulun lomake", "kehotietoisuus", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_koulun_lomake_tasapainojaliike_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "koulun lomake", "tasapaino ja liike", 16, (63, "90")), # normal case
            ("lapsi", "koulun lomake", "tasapaino ja liike", 10, (42, "21")), # minimum value
            ("lapsi", "koulun lomake", "tasapaino ja liike", 40, (80, ">99")), # maximum value
            ("lapsi", "koulun lomake", "tasapaino ja liike", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_koulun_lomake_suunnittelujaoivallukset_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "koulun lomake", "suunnittelu ja oivallukset", 16, (55, "69")), # normal case
            ("lapsi", "koulun lomake", "suunnittelu ja oivallukset", 10, (40, "16")), # minimum value
            ("lapsi", "koulun lomake", "suunnittelu ja oivallukset", 40, (80, ">99")), # maximum value
            ("lapsi", "koulun lomake", "suunnittelu ja oivallukset", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)

    def test_koulun_lomake_sosiaalinenosallistuminen_valid_input_returns_correct_values(self):
        test_cases = [
            ("lapsi", "koulun lomake", "sosiaalinen osallistuminen", 16, (53, "62")), # normal case
            ("lapsi", "koulun lomake", "sosiaalinen osallistuminen", 10, (40, "16")), # minimum value
            ("lapsi", "koulun lomake", "sosiaalinen osallistuminen", 40, (78, ">99")), # maximum value
            ("lapsi", "koulun lomake", "sosiaalinen osallistuminen", 50, None)  # out of range
        ]

        for ika, lomake, asteikko, luku, expected in test_cases:
            with self.subTest(ika=ika, lomake=lomake, asteikko=asteikko, luku=luku):
                self.assertEqual(hae_lomakkeesta(ika, lomake, asteikko, luku), expected)


class TestValitseAsteikko(unittest.TestCase):
    @patch('builtins.input', side_effect=["näkö"])
    def test_valid_input_full_name(self, mock_input):
        self.assertEqual(valitse_asteikko(), "näkö")

    @patch('builtins.input', side_effect=["VIS"])
    def test_valid_input_abbreviation(self, mock_input):
        self.assertEqual(valitse_asteikko(), "VIS")

    @patch('builtins.input', side_effect=["invalid", "kuulo"])
    @patch('builtins.print')
    def test_invalid_then_valid_input(self, mock_print, mock_input):
        self.assertEqual(valitse_asteikko(), "kuulo")
        mock_print.assert_any_call("Valitsemaasi asteikkoa ei ole olemassa.")

    @patch('builtins.input', side_effect=["poistu"])
    def test_exit_input(self, mock_input):
        self.assertIsNone(valitse_asteikko())


class TestValitseLomake(unittest.TestCase):
    @patch('builtins.input', side_effect=["kodin lomake"])
    def test_valid_input(self, mock_input):
        self.assertEqual(valitse_lomake(["kodin lomake", "koulun lomake"]), "kodin lomake")

    @patch('builtins.input', side_effect=["poistu"])
    def test_exit_input(self, mock_input):
        self.assertIsNone(valitse_lomake(["kodin lomake", "koulun lomake"]))

    @patch('builtins.input', side_effect=["invalid", "koulun lomake"])
    @patch('builtins.print')
    def test_invalid_then_valid_input(self, mock_print, mock_input):
        self.assertEqual(valitse_lomake(["kodin lomake", "koulun lomake"]), "koulun lomake")
        mock_print.assert_any_call("Valitsemaasi lomaketta ei ole olemassa.")


class TestLaskeSTPisteet(unittest.TestCase):
    @patch('builtins.input', side_effect=['10', '15', '20', '25', '30', '35'])
    @patch('builtins.print')
    def test_laske_st_pisteet(self, mock_print, mock_input):
        laske_st_pisteet()
        mock_print.assert_any_call("Osa-alueiden yhteenlasketut ST-pisteet ovat 135.\n")

    @patch('builtins.input', side_effect=['10', '10', '10', '10', '10', '10'])
    @patch('builtins.print')
    def test_laske_st_pisteet_min_values(self, mock_print, mock_input):
        laske_st_pisteet()
        mock_print.assert_any_call("Osa-alueiden yhteenlasketut ST-pisteet ovat 60.\n")

    @patch('builtins.input', side_effect=['40', '40', '40', '40', '40', '40'])
    @patch('builtins.print')
    def test_laske_st_pisteet_max_values(self, mock_print, mock_input):
        laske_st_pisteet()
        mock_print.assert_any_call("Osa-alueiden yhteenlasketut ST-pisteet ovat 240.\n")


class TestTeeTulkinta(unittest.TestCase):
    # Kodin lomake
    @patch('SPM2.hae_lomakkeesta', return_value=(49, "46%"))
    @patch('builtins.input', side_effect=["näkö", "12"])
    @patch('builtins.print')
    def test_tyypilliseen_reagointiin(self, mock_print, mock_input, mock_hae):
        tee_tulkinta("kodin lomake", "lapsi")
        mock_print.assert_any_call(
            "Raakapistettä 12 vastaava standardoitu T-piste on 49 ja persentiili on 46%, joka viittaa tyypilliseen reagointiin.\n"
        )

    @patch('SPM2.hae_lomakkeesta', return_value=(65, "93%"))
    @patch('builtins.input', side_effect=["maku ja haju", "21"])
    @patch('builtins.print')
    def test_kohtalaisiin_vaikeuksiin(self, mock_print, mock_input, mock_hae):
        tee_tulkinta("kodin lomake", "lapsi")
        mock_print.assert_any_call(
            "Raakapistettä 21 vastaava standardoitu T-piste on 65 ja persentiili on 93%, joka viittaa kohtalaisiin vaikeuksiin.\n"
        )

    @patch('SPM2.hae_lomakkeesta', return_value=(74, "99%"))
    @patch('builtins.input', side_effect=["sosiaalinen osallistuminen", "32"])
    @patch('builtins.print')
    def test_huomattaviin_vaikeuksiin(self, mock_print, mock_input, mock_hae):
        tee_tulkinta("kodin lomake", "lapsi")
        mock_print.assert_any_call(
            "Raakapistettä 32 vastaava standardoitu T-piste on 74 ja persentiili on 99%, joka viittaa huomattaviin vaikeuksiin.\n"
        )

    # Koulun lomake
    @patch('SPM2.hae_lomakkeesta', return_value=(49, "46%"))
    @patch('builtins.input', side_effect=["näkö", "13"])
    @patch('builtins.print')
    def test_tyypilliseen_reagointiin(self, mock_print, mock_input, mock_hae):
        tee_tulkinta("koulun lomake", "lapsi")
        mock_print.assert_any_call(
            "Raakapistettä 13 vastaava standardoitu T-piste on 49 ja persentiili on 46%, joka viittaa tyypilliseen reagointiin.\n"
        )

    @patch('SPM2.hae_lomakkeesta', return_value=(64, "92%"))
    @patch('builtins.input', side_effect=["maku ja haju", "14"])
    @patch('builtins.print')
    def test_kohtalaisiin_vaikeuksiin(self, mock_print, mock_input, mock_hae):
        tee_tulkinta("koulun lomake", "lapsi")
        mock_print.assert_any_call(
            "Raakapistettä 14 vastaava standardoitu T-piste on 64 ja persentiili on 92%, joka viittaa kohtalaisiin vaikeuksiin.\n"
        )

    @patch('SPM2.hae_lomakkeesta', return_value=(75, "99%"))
    @patch('builtins.input', side_effect=["sosiaalinen osallistuminen", "33"])
    @patch('builtins.print')
    def test_huomattaviin_vaikeuksiin(self, mock_print, mock_input, mock_hae):
        tee_tulkinta("koulun lomake", "lapsi")
        mock_print.assert_any_call(
            "Raakapistettä 33 vastaava standardoitu T-piste on 75 ja persentiili on 99%, joka viittaa huomattaviin vaikeuksiin.\n"
        )
