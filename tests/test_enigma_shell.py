import unittest
import sys
import os
import io
import contextlib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from enigma_shell import EnigmaShell



class TestEnigma(unittest.TestCase):
    def test_setting_a_message_for_the_enigma(self):
        original_stdin = sys.stdin
        try:
            sys.stdin = io.StringIO('Hi Mom!\n\n')
            enigma_shell = EnigmaShell()
            with contextlib.redirect_stdout(io.StringIO()):
                enigma_shell.run()
        finally:
            sys.stdin = original_stdin
            
        self.assertEqual(enigma_shell.get_message(), 'Hi Mom!')



if __name__ == '__main__':
    unittest.main()