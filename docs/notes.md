# notes

## state machine pattern revisted

- deciding against using state machine pattern (for GameState and BoardState) for now because of complexity it adds and tight coupling it creates

```
There are 4 states for the board:

- NormalState: it's your turn and you have not placed the mark on the board
- LockedNormalState: it's the opponent's turn and they have not placed the mark on the board

- SelectedState: it's your turn and you have placed the mark on the board
- LockedSelectedState: it's the opponent's turn and they have placed the mark on the board

The board state is Locked while it is the opponents turn.
- (it's locked when its not your turn)
The board state is not Locked during your turn.

The board state is Selected when a player has selected a position.
- (the player has placed the mark on the board)
The board state is not Selected when a player has not selected a position.

note:
- After selecting a position, the player must confirm their play to change turn
- NormalState -> SelectedState -> LockedNormalState -> LockedSelectedState -> NormalState


---

Game state interface

there are 4 states:

- setup
- ready
- playing
- ended

```

## more on score string

- we can use a string to represent the score of a box

example:

- classic tic-tac-toe -> no score string
- ultimate tic-tac-toe (9x9 board)
    - score string: "x..x..xo."
- for larger ultimate tic-tac-toe (27x27 board), we need multiple score strings separated by semicolon
    - "x...x...o;xxx....../........./........./........./..x.x.x../........./........./........./..o..o..o"

![CleanShot 2025-09-09 at 14 29 55@2x](https://github.com/user-attachments/assets/90a656bf-54f1-49c1-ad22-59d8f334657e)

## future consideration: design patterns for win conditions for other variants ttt

- might want to use strategy pattern

## should i use a class for the square?

example:

```python
class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

- prob not, doesn't seem necessary (for now)

## dynamic programming, recursion

- to handle the case where the board is infinite, we need to use dynamic programming and recursion
- we need to use memoization to avoid redundant calculation

- check 3x3 board (box, classic tic-tac-toe) for win condition, ... (recursion)
- we keep a score string to represent if the box is won
    - example:
        - if at top-left box (`boxes[0]`), we have "xxx......" (the box is won by x)
        - then the board string should be "x........"

![CleanShot 2025-09-09 at 13 51 03@2x](https://github.com/user-attachments/assets/ac3e2b4e-fde9-4a00-8cd1-3cbe1add28c0)

string format:

- a 3x3 board has a t3n (tic-tac-toe notation) of "o;xoxoxoxox"

## which class should be responsible for making moves by players?

- Game class or Board class or Player class
- Game class should be responsible for making moves by players since it has the logic for allowed moves
- if it's in the Player or the Board class, it's not following the single responsibility principle

## for ultimate tic-tac-toe, where should the logic for allowed moves be?

- either in the Game class or the Board class
- it should be in the Game class since the Board class is a data structure and Game class is the one that has the logic

## Player object - where should it be (dependency) injected?

- it could be injected into either the Game class or the Board class
- in the [bncpy library](https://github.com/jwc20/bncpy) the Player object was injected into the Board class, because in
  one game, each players should have their own board
- in pyttt, it might be better to have Player in the Game class since each players don't need their own board

```python
# example
def main():
    players = [Player("player_1"), Player("player_2")]
    board = Board(...)
    game = Game(board, players)
```

## memoization/caching

- memoization variable `cache` is used in the minimax method in the Game class.
    - this is used to avoid redundant calculation that it's going
    - we are using the `__repr__()` as key
    - we are using `.get()` method (as opposed to using `cache[key]`) to aboid key errors (since the initial cache
      dictionary is empty)

## tic-tac-toe board notation

- taking influence from FEN notation from chess and from [ultimattt](https://github.com/nelhage/ultimattt)

    - `O;@........;X.OO...../X..X.O.O./X.X...O.O/.X.OXO.../O.O.X..../.XX....O./......X.O/.O.X.X.../.O.....XX`

- note that the notation needs to be updated for larger boards

## board/grid coordinate system

![CleanShot 2025-09-06 at 15 23 55@2x](https://github.com/user-attachments/assets/7645830c-ad34-42fe-8b35-4c324f59dc4d)

## numpy vs nested list for board

- numpy is faster than nested list
- numpy is more memory efficient than nested list

### example

without numpy:

```python
board_str = "xoxoxoxox x..x..xo. x..x..xo. ooooooooo x..x..xo. x..x..xo. xoxoxoxox x..x..xo. x..x..xo."
```

## players and multi-players

- this should allow more than 2 players to play
- where each player are assigned to either "X" or "O" teams

## abc vs protocol

- narrow protocols are more useful (Fluent Python p.476)
    - narrow protocols have a single method
    - we also dont have to use a decorator in a protocol

```
...sometimes you see a protocol defined near the function that uses it—that is,
defined in “client code” instead of being defined in a library. This is makes it easy to
create new types to call that function, which is good for extensibility and testing with
mocks.

The practices of narrow protocols and client-code protocols both avoid unnecessary
tight coupling, in line with the Interface Segregation Principle, which we can summa‐
rize as “Clients should not be forced to depend upon interfaces that they do not use.”
```

- https://peps.python.org/pep-0544/

## classes/files

- Game
- Board
    - factory method pattern(?)
    - linked list for history
- Player
- BoardState
    - State machine pattern
- GameState
    - State machine pattern
- utils.py

## array(list) vs string

- we can store pieces(x's and o's) in an array and reference them using an array index

    - arr = [[".", ".", "x"],[".", ".", "x"],[".", ".", "x"]] => arr[0][2] = "x"
    - the issue is that passing around the array bunch of times can use lot of resource.
    - also there are risks of array being altered accidentally because arrays are passed between functions by reference.

- string manipulation is optimized in Python
- since strings are immutable, we need to pass around copy of the string with the cost of speed but with less risk of
  string being altered when passed between functions(like arrays)
    - using immutable data types prevents using `deepcopy()` and deep copying is slow and use up memory

### string manipulation and getting position

- have string like "xxxxxxxxx x..x..xo. x..x..xo. ooooooooo x..x..xo. x..x..xo. xoxoxoxox x..x..xo. x..x..xo." for
  ultimate tic-tac-toe.

3x3 board/grid of tic-tac-toe squares

```
xxxxxxxxx x..x..xo. x..x..xo.
ooooooooo x..x..xo. x..x..xo.
xoxoxoxox x..x..xo. x..x..xo.
```

or

```
xxx x.. x..
xxx x.. x..
xxx xo. xo.

ooo x.. x..
ooo x.. x..
ooo xo. xo.

xox x.. x..
oxo x.. x..
xox xo. xo.
```

- each 3x3 square is separated by whitespace

- multi-dimensional arrays are slow and uses lot of memory so we should instead use 1d-array (a block of memory)
- calculate the index of the 1d-array from the matrix row and column
    - (e.g. row \* width + col)
- matrix multiplication requires going through rows and the columns of the matrix
    - (prob have to use cross product to determine positions of the squares in the board using the board string ("
      x..x..xo."))
    - must consider recursion for infinite fractal board

---

## cool

- (Goal) https://pgrim.org/fractal/2Tic.html
- https://www.dubberly.com/concept-maps/tic-tac-toe.html
- https://www.talkingelectronics.com/projects/TicTacToe/TicTacToe-P1.html
- https://xkcd.com/832/
- https://mathwithbaddrawings.com/2013/06/16/ultimate-tic-tac-toe/

## tic-tac-toe variants

- https://en.wikipedia.org/wiki/Tic-tac-toe_variants
- https://www.cs.umd.edu/~gasarch/COURSES/752/S22/Combgamesttt.pdf
- https://dhkts1.github.io/ultimate-nd-tictactoe-3d/
- https://nrich.maths.org/articles/sprouts-explained
- https://en.wikipedia.org/wiki/Gomoku
- https://en.wikipedia.org/wiki/Connect6
- http://www.geom.uiuc.edu/video/sos/materials/surfaces/tictactoe.html
- https://ranger.uta.edu/~weems/NOTES6319/PAPERSONE/patashnik.pdf (4x4x4 ttt)
- https://en.m.wikipedia.org/wiki/Quantum_tic-tac-toe

## algorithms, programming ttt, etc

- https://leetcode.ca/2016-11-12-348-Design-Tic-Tac-Toe/
- https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/
- https://leetcode.com/problems/valid-tic-tac-toe-state/description/

- https://lemmoscripts.com/wp/2018/09/03/creating-a-simple-tic-tac-toe-or-naughts-and-crosses-game-in-javascript-and-jquery/
- https://andrewfischergames.com/blog/obfuscation
- https://en.wikipedia.org/wiki/Game_complexity
- https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation (notation for chess)
- https://sasankyadati.github.io/Tic-Tac-Toe/ (summary of Peter Norvig & Stuart Russell - Artificial Intelligence : A
  Modern Approach (3rd edition))
- https://github.com/nelhage/ultimattt

## strategy

- https://sasankyadati.github.io/Tic-Tac-Toe/
- http://www.se16.info/hgb/tictactoe.htm

## other links

- https://hn.algolia.com/?dateRange=all&page=0&prefix=false&query=tic%20tac%20toe&sort=byPopularity&type=story
- https://lobste.rs/search?q=tic+tac+toe&what=comments&order=newest
- https://slashdot.org/index2.pl?fhfilter=tic+tac+toe
