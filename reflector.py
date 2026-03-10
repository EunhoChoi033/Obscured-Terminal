class Reflector:
    def __init__(self, keywords: list[str]):
        self._keywords = keywords
        
    
    def determine_reflection_index(self, input_index: int) -> int:
        '''Takes the input index and determines the output index from the reflector'''
        keyword = self._keywords[input_index]
        
        if self._keywords.index(keyword) == input_index:
            return self._keywords[input_index + 1:].index(keyword)
        else:
            return self._keywords.index(keyword)