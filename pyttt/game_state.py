from typing import Protocol
from dataclasses import dataclass


class GameState(Protocol):
    """
    there are 4 states:
    - setup
    - ready
    - playing
    - ended
    """
    pass


class GameContext(Protocol):
    def set_state(self, state: GameState): ...

@dataclass
class SetupGameState:
    pass

@dataclass
class ReadyGameState:
    pass

@dataclass
class PlayingGameState:
    pass

@dataclass
class EndedGameState:
    pass