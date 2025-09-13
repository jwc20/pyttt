"""
pyttt/player.py
"""

class Player:
    """
    this class exists to distinguish between players and set the mark ("x" or "o")
    """
    def __init__(self, name:str, mark: str) -> None:
        self._name = name
        self._mark = mark
        
    @property
    def name(self):
        return self._name
    
    @property
    def mark(self):
        return self._mark
    