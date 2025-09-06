# notes

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
    - (e.g. row * width + col)
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

## links

- https://sasankyadati.github.io/Tic-Tac-Toe/
- https://ranger.uta.edu/~weems/NOTES6319/PAPERSONE/patashnik.pdf
- https://leetcode.ca/2016-11-12-348-Design-Tic-Tac-Toe/
- https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/
- https://leetcode.com/problems/valid-tic-tac-toe-state/description/

- https://lemmoscripts.com/wp/2018/09/03/creating-a-simple-tic-tac-toe-or-naughts-and-crosses-game-in-javascript-and-jquery/
- https://andrewfischergames.com/blog/obfuscation

## strategy

- https://sasankyadati.github.io/Tic-Tac-Toe/
- http://www.se16.info/hgb/tictactoe.htm

## matrix

- https://rocm.blogs.amd.com/high-performance-computing/spmv/part-1/README.html
- https://medium.com/gpgpu/block-sparse-matrix-vector-multiplication-with-cuda-4e616b30267
- https://developer.nvidia.com/blog/accelerating-matrix-multiplication-with-block-sparse-format-and-nvidia-tensor-cores/
- https://www.geeksforgeeks.org/dsa/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
- https://www.researchgate.net/publication/288933300_Compressed_k_d-tree_for_temporal_graphs
- https://www.researchgate.net/publication/26487637_Scalable_Multiple-Description_Image_Coding_Based_on_Embedded_Quantization

## things to know

- recursive block matrix
- block space matrix-vector
- Block Compressed Sparse Row (BCSR)
- trace (in a matrix)
- minimax
- dynamic programming, recursion
- fractal
