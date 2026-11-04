import importlib.util
import os
import sys
import unittest

pfad = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ersetze-platzhalter.py")
spec = importlib.util.spec_from_file_location("ersetze_platzhalter", pfad)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class Ersetze(unittest.TestCase):
    def test_ersetzt_und_meldet(self):
        neu, offen = mod.ersetze("a {{issue:01}} b {{r3:06}} c {{r2:99}}", {"issue": {"01": "U1"}, "r3": {"06": "U6"}})
        self.assertEqual(neu, "a U1 b U6 c {{r2:99}}")
        self.assertEqual(offen, ["{{r2:99}}"])


if __name__ == "__main__":
    unittest.main()
