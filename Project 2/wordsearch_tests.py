"""
Project 2

CPE101
Spring 2021
Author: Jack Forrester
"""


import unittest
import wordsearch


class MyTest(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(wordsearch.reverse_string("ABCDEFGHIJ"),
                "JIHGFEDCBA")
        self.assertEqual(wordsearch.reverse_string("KiOlFnKiKp"),
                "pKiKnFlOiK")
        self.assertEqual(wordsearch.reverse_string("aaBBccDDee"),
                "eeDDccBBaa")
        self.assertEqual(wordsearch.reverse_string("ALL YOUR BASE"),
                "ESAB RUOY LLA")


    def test_transpose_string(self):
        self.assertEqual(wordsearch.transpose_string("ABCDEFGHI", 3),
                "ADGBEHCFI")
        self.assertEqual(wordsearch.transpose_string("LTRIASPSSURE", 4),
                "LASTSURPRISE")
        self.assertEqual(wordsearch.transpose_string("BBURRENAMDY!", 2),
                "BURNMYBREAD!")
        self.assertEqual(wordsearch.transpose_string("SANOLKCLGIIO", 3),
                "SOCIALLINKGO")


    def test_find_word(self):
        self.assertEqual(
                wordsearch.find_word("ABCDEFGHI","DEF",3),
                "DEF: (FORWARD) row: 1 column: 0"
                )
        self.assertEqual(wordsearch.find_word("ABCDEFGHI", "CAT", 3),
                "CAT: word not found")
        self.assertEqual(
                wordsearch.find_word(
                    "FYYHNRDRLJCINUAAWAAHRNTKLPNECILFDAPEOGOTPNHPOLAND",
                    "TOGO", 7), "TOGO: (BACKWARD) row: 5 column: 4")
        self.assertEqual(wordsearch.find_word("FAWARJOSOECUGOAT", "FROG", 4),
                "FROG: (DOWN) row: 0 column: 0")
        self.assertEqual(wordsearch.find_word("SKIODMNSRKOIRAMELAYJ",
            "LINK", 5),
                "LINK: (UP) row: 3 column: 1")


    def test_find_word_forward(self):
        self.assertEqual(wordsearch.find_word_forward("ABCDEFGHI", "DEF", 3),
                "DEF: (FORWARD) row: 1 column: 0")
        self.assertEqual(
                wordsearch.find_word_forward(
                    "FYYHNRDRLJCINUAAWAAHRNTKLPNECILFDAPEOGOTPNHPOLAND",
                    "POLAND", 7), "POLAND: (FORWARD) row: 6 column: 1")
        self.assertEqual(wordsearch.find_word_forward("FAWARJOSOECUGOAT",
            "GOAT", 4),
                "GOAT: (FORWARD) row: 3 column: 0")
        self.assertEqual(wordsearch.find_word_forward("SKIODMNSRKOIRAMELAYJ",
            "NESS", 5),
                None)


    def test_find_word_backward(self):
        self.assertEqual(wordsearch.find_word_backward("ABCDEFGHI", "CBA", 3),
                "CBA: (BACKWARD) row: 0 column: 2")
        self.assertEqual(
                wordsearch.find_word_backward(
                    "FYYHNRDRLJCINUAAWAAHRNTKLPNECILFDAPEOGOTPNHPOLAND",
                    "TOGO", 7), "TOGO: (BACKWARD) row: 5 column: 4")
        self.assertEqual(wordsearch.find_word_backward("FAWARJOSOECUGOAT",
            "COW", 4), None)
        self.assertEqual(wordsearch.find_word_backward("SKIODMNSRKOIRAMELAYJ",
            "MARIO", 5), "MARIO: (BACKWARD) row: 2 column: 4")


    def test_find_word_down(self):
        self.assertEqual(wordsearch.find_word_down("ABCDEFGHI", "BEH", 3),
                "BEH: (DOWN) row: 0 column: 1")
        self.assertEqual(
                wordsearch.find_word_down(
                    "FYYHNRDRLJCINUAAWAAHRNTKLPNECILFDAPEOGOTPNHPOLAND",
                    "PARIS", 7), None)
        self.assertEqual(wordsearch.find_word_down("FAWARJOSOECUGOAT",
            "FROG",4),
                "FROG: (DOWN) row: 0 column: 0")
        self.assertEqual(wordsearch.find_word_down("SKIODMNSRKOIRAMELAYJ",
            "DK", 5),
                "DK: (DOWN) row: 0 column: 4")


    def test_find_word_up(self):
        self.assertEqual(wordsearch.find_word_up("ABCDEFGHI", "CAT", 3),
                None)
        self.assertEqual(
                wordsearch.find_word_up(
                    "FYYHNRDRLJCINUAAWAAHRNTKLPNECILFDAPEOGOTPNHPOLAND",
                    "ITALY", 7), "ITALY: (UP) row: 4 column: 1")
        self.assertEqual(wordsearch.find_word_up("FAWARJOSOECUGOAT",
            "COW", 4),
                "COW: (UP) row: 2 column: 2")
        self.assertEqual(wordsearch.find_word_up("SKIODMNSRKOIRAMELAYJ",
            "LINK", 5),
                "LINK: (UP) row: 3 column: 1")


    def test_display_puzzle(self):
        self.assertEqual(wordsearch.display_puzzle("ABCDEFGHI", 3),
                'ABC\nDEF\nGHI')
        self.assertEqual(
                wordsearch.display_puzzle(
                    "FYYHNRDRLJCINUAAWAAHRNTKLPNECILFDAPEOGOTPNHPOLAND", 7),
                'FYYHNRD\nRLJCINU\nAAWAAHR\nNTKLPNE\nCILFDAP\nEOGOTPN\nHPOLAND')
        self.assertEqual(wordsearch.display_puzzle("FAWARJOSOECUGOAT", 4),\
                'FAWA\nRJOS\nOECU\nGOAT')
        self.assertEqual(wordsearch.display_puzzle("SKIODMNSRKOIRAMELAYJ", 5),\
                'SKIOD\nMNSRK\nOIRAM\nELAYJ')


if __name__ == '__main__':
    unittest.main()
