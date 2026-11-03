import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import post  # noqa: E402


class Label(unittest.TestCase):
    def test_label_vorhanden(self):
        self.assertEqual(post.label_id("Nachweis", [{"id": 9, "name": "Nachweis"}]), 9)

    def test_label_fehlt(self):
        self.assertIsNone(post.label_id("Nachweis", [{"id": 9, "name": "nostr"}]))


class Verweise(unittest.TestCase):
    def test_ersetzt(self):
        self.assertEqual(post.ersetze_verweise("siehe {{nachweis:04-ap-4-5}}", {"04-ap-4-5": "https://x/1"}), "siehe https://x/1")

    def test_unbekannt_bleibt(self):
        self.assertEqual(post.ersetze_verweise("{{nachweis:99-x}}", {}), "{{nachweis:99-x}}")


class Ergebnis(unittest.TestCase):
    def test_ergebnis_ueberspringt(self):
        self.assertTrue(post.zu_ueberspringen("04-ap-4-5", {"04-ap-4-5": {"number": 900}}))


if __name__ == "__main__":
    unittest.main()
