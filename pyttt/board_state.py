from typing import Protocol


class BoardState(Protocol):
    """
    There are 4 states for the board:
    - NormalState
    - LockedNormalState
    - SelectedState
    - LockedSelectedState
    
    The board state is Locked while it is the opponents turn.
    The board state is not Locked during your turn.
    
    The board state is Selected when a player has selected a position.
    The board state is not Selected when a player has not selected a position.
    """
    pass


class BoardContext(Protocol):
    pass


class LockedBoardState(BoardState):
    """parent state of LockedNormalState and LockedSelectedState"""
    pass


class NormalState(BoardState):
    """current player's turn and no position is selected"""
    pass


class LockedNormalState(LockedBoardState):
    """opponent's turn and no position is selected"""
    pass


class SelectedState(BoardState):
    """current player's turn and a position is selected"""
    pass


class LockedSelectedState(LockedBoardState):
    """opponent's turn and a position is selected"""
    pass
