class Player:
    def __init__(self, name:str, piece: str) -> None:
        self._name = name
        self._piece = piece
        
    @property
    def name(self):
        return self._name
    
    @property
    def piece(self):
        return self._piece