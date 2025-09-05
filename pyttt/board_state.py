from dataclasses import dataclass
from typing import Protocol


class BoardState(Protocol):
    """
    There are 4 states for the board:
    - NormalState: it's your turn and you have not placed the piece on the board
    - LockedNormalState: it's the opponent's turn and they have not placed the piece on the board
    
    - SelectedState: it's your turn and you have placed the piece on the board
    - LockedSelectedState: it's the opponent's turn and they have placed the piece on the board
    
    
    The board state is Locked while it is the opponents turn.
        - (it's locked when its not your turn)
    The board state is not Locked during your turn.
    
    
    The board state is Selected when a player has selected a position. 
        - (the player has placed the piece on the board) 
    The board state is not Selected when a player has not selected a position.
    
    
    note:
        - After selecting a position, the player must confirm their play to change turn 
        - NormalState -> SelectedState -> LockedNormalState -> LockedSelectedState -> NormalState
    """
    pass


class LockedBoardState(BoardState):
    """parent state of LockedNormalState and LockedSelectedState"""
    pass


#############################################

class BoardContext(Protocol):
    board_str: str

    def set_state(self, state: BoardState): ...


#############################################

@dataclass
class NormalState:
    """
    parent: BoardState
    current player's turn and no position is selected
    """
    pass


@dataclass
class LockedNormalState:
    """
    parent: LockedBoardState
    opponent's turn and no position is selected
    """
    pass


@dataclass
class SelectedState:
    """
    parent: BoardState
    current player's turn and a position is selected
    """
    pass


@dataclass
class LockedSelectedState:
    """
    parent: LockedBoardState
    opponent's turn and a position is selected
    """
    pass
