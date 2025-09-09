from pyttt import Board

class Player:
    def __init__(self, name:str, mark: str) -> None:
        self._name = name
        self._mark = mark
        
    @property
    def name(self):
        return self._name
    
    @property
    def mark(self):
        return self._mark
    
    def place_mark(self, board: Board, index: int):
        pass
    
    