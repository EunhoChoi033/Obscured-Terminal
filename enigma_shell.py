from enigma import Enigma



class EnigmaShell:
    def __init__(self):
        self._enigma = Enigma()


    def run(self):
        '''Runs the Enigma Shell Program'''
        while True:
            new_mode = self._ask_encrypt_or_decrypt()
            if new_mode is None:
                break
            else:
                self._enigma.set_mode(new_mode)

            message = self._input_message()
            if message is None:
                break
            else:
                self._enigma.set_message(message)
    
    
    def _ask_encrypt_or_decrypt(self) -> None | str:
        '''Returns E if Enigma should encrypt, D if Enigma should decrypt, otherwise returns None'''
        user_input = input('| Encrypt or Decrypt (E / D)?: ')
        user_input = user_input.strip().upper()
        
        if self._enigma.verify_mode_request(user_input):
            return user_input
        else:
            return None

    
    def _input_message(self) -> None | str:
        '''Asks the user for the message to either encrypt or decrypt and returns it; returns None if the user inputted nothing'''
        message = input('| | Message: ')
        if message:
            return message
        else:
            return None
        
        
    def get_mode(self) -> None | str:
        '''Returns the current mode of the Enigma'''
        return self._enigma.get_mode()
    
    
    def get_message(self) -> None | str:
        '''Returns the current message of the Enigma'''
        return self._enigma.get_message()