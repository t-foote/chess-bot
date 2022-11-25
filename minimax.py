from main import *


class GameState:
    pass


class GameState:
    _board:         Board
    _real_board:    Board
    _children:      List[GameState]
    value:         int
    _p:             Optional[Piece]
    _m:             Optional[Tuple[int, int]]
    _alpha:         int
    _beta:          int
    root_turn:      bool

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __init__(self, b: Board, depth: int = 2, root_turn: bool = None, _p=None, _m=None):

        self._board = BoardCopy(b)
        self._real_board = b
        self._children = []
        self._p, self._m = _p, _m
        if root_turn is None:
            self.root_turn = b.turn
        else:
            self.root_turn = root_turn

        if depth >= 1:
            for p in self._board.turn_pieces():
                for m in p.available_moves():
                    copy = BoardCopy(b)
                    copy.move(p, m)
                    self._children.append(GameState(copy, depth - 1, self.root_turn, p, m))

        # Calculating value:
        if not self._children:
            self.value = self._board.value()
        elif self._real_board.turn == root_turn:
            self.value = max(self._children).value
        else:
            self.value = min(self._children).value

    def make_best_move(self) -> None:

        if self._children:
            print(max(self._children).value)
            self._real_board.move(max(self._children)._p, max(self._children)._m)
