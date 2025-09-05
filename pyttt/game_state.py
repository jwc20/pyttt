from typing import Protocol
from dataclasses import dataclass


class GameState(Protocol):
    """
    Game state interface
    
    there are 4 states:
    - setup
    - ready
    - playing
    - ended
    """
    pass


class LockedGameState(GameState):
    """
    if game is locked, then players cannot play/make moves
    
    parent state of LockedSetupState and LockedEndedState
    """
    pass


#############################################

class GameContext(Protocol):
    def set_state(self, state: GameState): ...


#############################################

@dataclass
class LockedSetupState:
    pass


@dataclass
class LockedEndedState:
    pass


@dataclass
class ReadyState:
    pass


@dataclass
class PlayingState:
    pass
