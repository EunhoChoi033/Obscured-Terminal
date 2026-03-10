# rotor.py



class Rotor:
    def __init__(self, keywords: list[str], primary_keyword_preset: list[int], secondary_keyword_preset: list[int]):
        self._keywords = keywords
        self._forward_rotor_num_alterations = dict(zip(primary_keyword_preset, secondary_keyword_preset))
        self._reverse_rotor_num_alterations = dict(zip(secondary_keyword_preset, primary_keyword_preset))
        self._offset = 0


    def click_rotor_by_one(self) -> None:
        '''Changes the rotor\'s offset by one'''
        self._offset += 1


    def transfer_primary_to_secondary(self, keyword: str) -> str:
        '''Returns the keyword outputted forward from the given index'''
        input_num = (self._keywords.index(keyword) + self._offset) % len(self._keywords)
        output_num = (self._forward_rotor_num_alterations[input_num] - self._offset) % len(self._keywords)
        return self._keywords[output_num]


    def transfer_secondary_to_primary(self, keyword: str) -> str:
        '''Returns the keyword outputted in reverse from the given index'''
        input_num = (self._keywords.index(keyword) + self._offset) % len(self._keywords)
        output_num = (self._reverse_rotor_num_alterations[input_num] - self._offset) % len(self._keywords)
        return self._keywords[output_num]