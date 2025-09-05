from typing import Protocol


class GameState(Protocol):
    """
    there are 3 states:
    - ready
    - playing
    - locked (ended or before ready)
    
    """
    pass


class GameContext(Protocol):
    pass
