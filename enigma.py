import random



_ENCRYPT_MODE_KEYWORD = 'E'
_DECRYPT_MODE_KEYWORD = 'D'
_NUM_ROTORS = 5



class Rotor:
    def __init__(self, keyword_preset: list[str]):
        self._keyword_preset = keyword_preset
        self._offset = 0
        
    
    def increase_offset(self):
        '''Increases the offset of the rotor by one'''
        self._offset += 1


    def get_keyword_at_index(self, index):
        '''Returns the keyword at a certain index'''
        return self._keyword_preset[index]



class Enigma:
    def __init__(self):
        self._keywords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '[', ']', '{', '}', '|', ';', '\'', ':', '\\', '"', ',', '.', '<', '>', '/', '?']
        self._mode = None
        self._message = None
        self._rotors = self._setup_rotors()
        random.seed(3301)        


    def _setup_rotors(self) -> list[list[Rotor]]:
        '''Sets up all the Enigma rotors'''
        rotors = []
        for i in range(_NUM_ROTORS):
            randomized_preset = random.sample(self._keywords, len(self._keywords))
            rotors.append(Rotor(randomized_preset))
        return rotors
    
    
    def set_mode(self, new_mode: str) -> None:
        '''Sets the Enigma mode to the one given'''
        self._mode = new_mode
        
        
    def set_message(self, new_message: str) -> None:
        '''Sets the Enigma message to the one given'''
        self._message = new_message
                
            
    def get_mode(self) -> None | str:
        '''Returns the current mode of the Enigma'''
        return self._mode


    def get_message(self) -> None | str:
        '''Returns the current message stored in the Enigma'''
        return self._message
    
    
    def get_keywords(self) -> list[str]:
        '''Returns the keywords of the Enigma'''
        return self._keywords


    def verify_mode_request(self, user_input: str) -> bool:
        if user_input == _ENCRYPT_MODE_KEYWORD or user_input == _DECRYPT_MODE_KEYWORD:
            return True
        else:
            return False



    def encrypt_message(self, message: str) -> str:
        '''Returns the encrypted version of the given message'''
        return ''
    
    
    
# sent time and date sum + product of length of each word in notable quote + number of vowels in the notable quote

# https://www.geeksforgeeks.org/python/python-tkinter-tutorial/
# https://www.geeksforgeeks.org/python/python-ways-to-shuffle-a-list/
# https://echoes.soferity.com/
# https://www.markdownguide.org/basic-syntax/

# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 0123456789
# !@#$%^&*()-=_+[]{}|;\':",.<>/?