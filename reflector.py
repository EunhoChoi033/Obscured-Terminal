# reflector.py



class Reflector:
    def __init__(self, keywords: list[str], primary_keyword_preset: list[int], secondary_keyword_preset: list[int]):
        self._keywords = keywords
        self._rotor_num_alterations = dict(zip(primary_keyword_preset, secondary_keyword_preset))
        
    
    def determine_reflection(self, keyword: str) -> str:
        '''Takes in a keyword and returns the new keyword reflected by the reflector'''
        input_num = self._keywords.index(keyword)
        output_num = self._rotor_num_alterations[input_num]
        return self._keywords[output_num]