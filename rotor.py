# from collections import deque



class Rotor:
    def __init__(self, keywords: list[str], primary_keyword_preset: list[int], secondary_keyword_preset: list[int]):
        self._keywords = keywords
        self._rotor_num_alterations = dict(zip(primary_keyword_preset, secondary_keyword_preset))
        self._offset = 0


    def click_rotor_by_one(self) -> None:
        '''Changes the rotor\'s offset by one'''
        self._offset += 1


    def transfer_primary_to_secondary(self, keyword: str) -> str:
        '''Returns the keyword outputted forward from the given index'''
        input_num = (self._keywords.index(keyword) + self._offset) % len(self._keywords)
        output_num = (self._rotor_num_alterations[input_num] - self._offset) % len(self._keywords)
        return self._keywords[output_num]


    # def transfer_secondary_to_primary(self, index: int) -> str:
    #     '''Returns the index outputted backward from the given index'''
    #     new_index = self._secondary_keyword_preset.index(index)
    #     return self._primary_keyword_preset[index]