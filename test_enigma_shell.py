from enigma_shell import EnigmaShell
import unittest
import sys
import io
import contextlib



class TestEnigma(unittest.TestCase):
    def test_asking_user_for_mode_an_encrypt(self):
        original_stdin = sys.stdin
        try:
            sys.stdin = io.StringIO('E\n\n')
            enigma = EnigmaShell()
            with contextlib.redirect_stdout(io.StringIO()):
                enigma.run()
        finally:
            sys.stdin = original_stdin
            
        self.assertEqual(enigma.get_mode(), 'E')


    def test_asking_user_for_mode_an_decrypt(self):
        original_stdin = sys.stdin
        try:
            sys.stdin = io.StringIO('D\n\n')
            enigma = EnigmaShell()
            with contextlib.redirect_stdout(io.StringIO()):
                enigma.run()
        finally:
            sys.stdin = original_stdin
            
        self.assertEqual(enigma.get_mode(), 'D')


    def test_updating_enigma_mode(self):
        original_stdin = sys.stdin
        try:
            sys.stdin = io.StringIO('D\nHi Mom!\nE\n\n')
            enigma = EnigmaShell()
            with contextlib.redirect_stdout(io.StringIO()):
                enigma.run()
        finally:
            sys.stdin = original_stdin
            
        self.assertEqual(enigma.get_mode(), 'E')


    def test_setting_a_message_for_the_enigma(self):
        original_stdin = sys.stdin
        try:
            sys.stdin = io.StringIO('D\nHi Mom!\n\n')
            enigma = EnigmaShell()
            with contextlib.redirect_stdout(io.StringIO()):
                enigma.run()
        finally:
            sys.stdin = original_stdin
            
        self.assertEqual(enigma.get_message(), 'Hi Mom!')


    def test_updating_a_message_for_the_enigma(self):
        original_stdin = sys.stdin
        try:
            sys.stdin = io.StringIO('D\nHi Mom!\nD\nHi Dad!\n\n')
            enigma = EnigmaShell()
            with contextlib.redirect_stdout(io.StringIO()):
                enigma.run()
        finally:
            sys.stdin = original_stdin
            
        self.assertEqual(enigma.get_message(), 'Hi Dad!')



if __name__ == '__main__':
    unittest.main()