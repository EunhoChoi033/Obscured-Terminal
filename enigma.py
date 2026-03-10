import random
from datetime import datetime
from rotor import Rotor
from typing import Generator
from reflector import Reflector



_NUM_ROTORS = 5
_CODE_NUMBER = 3301



class Enigma:
    def __init__(self):
        self._keywords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '[', ']', '{', '}', '|', ';', '\'', ':', '\\', '"', ',', '.', '<', '>', '/', '?', '`', ' ']
        self._keyword_indexes = list(range(len(self._keywords))) # [0, 1, 2, 3, 4, 5, ..., 93]
        self._message = None
        self._set_random_seed()
        self._rotors = self._setup_rotors()
        self._reflector = self._setup_reflector()
        self._rotor_offsets = [0] * _NUM_ROTORS


    def _setup_rotors(self) -> list[Rotor]:
        '''Returns a list containing set up rotors'''
        rotors = []
        for _ in range(_NUM_ROTORS):
            primary_keyword_preset = random.sample(self._keyword_indexes, len(self._keyword_indexes))
            secondary_keyword_preset = random.sample(self._keyword_indexes, len(self._keyword_indexes))
            rotors.append(Rotor(self._keywords, primary_keyword_preset, secondary_keyword_preset))
        return rotors
    
    
    def _setup_reflector(self) -> Reflector:
        '''Returns a set up reflector'''
        return Reflector(random.sample(self._keywords, len(self._keywords)) + random.sample(self._keywords, len(self._keywords)))


    def _set_random_seed(self) -> None:
        '''Sets up the current random seed'''
        today = datetime.today()
        random.seed(_CODE_NUMBER + (today.year * today.month * today.day))
    
    
    def set_message(self, new_message: str) -> None:
        '''Sets the Enigma message to the one given'''
        self._message = new_message


    def _click_rotor_offsets(self) -> None:
        '''Offsets the appropriate rotors based off of how each of them are currently offset'''
        self._rotor_offsets[0] += 1
        for index in range(1, len((self._rotors))):
            previous_rotor_offset, current_rotor_offset = self._rotor_offsets[index - 1], self._rotor_offsets[index]

            if previous_rotor_offset >= len(self._keywords):
                previous_rotor_offset = 0
                self._rotors[index - 1].click_rotor_by_one()
            
            current_rotor_offset += 1
            self._rotors[index].click_rotor_by_one()
            


    def _cascade_message_forward(self, message: str) -> Generator[str, None, None]:
        '''Cascades the given message forward through the rotor(s) and returns a Generator with each character'''
        for character in list(message):
            self._click_rotor_offsets()
            for rotor in self._rotors:
                character = rotor.transfer_primary_to_secondary(character)
            yield character


    def process_message(self, message: None | str) -> str:
        '''Returns the processed version of the given message'''
        if message is not None:
            return ''.join(self._cascade_message_forward(message))
        else:
            return ''
                

    def get_message(self) -> None | str:
        '''Returns the current message stored in the Enigma'''
        return self._message
    
    
    def get_keywords(self) -> list[str]:
        '''Returns the keywords of the Enigma'''
        return self._keywords
    
    
    def get_rotor(self, index: int) -> Rotor:
        '''Returns the rotor from the specified index of the Enigma\'s rotors list'''
        return self._rotors[index]
    
    
# Random seed preset:
# 3301 + (year * month * day)
    
    
# For the future:    
# sent time and date sum + product of length of each word in notable quote + number of vowels in the notable quote

# https://www.geeksforgeeks.org/python/python-tkinter-tutorial/
# https://www.geeksforgeeks.org/python/python-ways-to-shuffle-a-list/
# https://echoes.soferity.com/
# https://www.markdownguide.org/basic-syntax/
# https://youtu.be/UKbP3Rjxhy0
# https://enigma.alextebbs.com/

# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 0123456789
# !@#$%^&*()-=_+[]{}|;\':",.<>/?