# notes


## array(list) vs string

- we can store pieces(x's and o's) in an array and reference them using an array index
    - arr = [[".", ".", "x"],[".", ".", "x"],[".", ".", "x"]] => arr[0][2] = "x"
    - the issue is that passing around the array bunch of times can use lot of resource.
    - also there are risks of array being altered accidently because arrays are passed between functions by reference.

- string manipulation is optimized in Python
- since strings are immutable, we need to pass around copy of the string with the cost of speed but with less risk of string being altered when passed between functions(like arrays)

## cool

- (Goal) https://pgrim.org/fractal/2Tic.html
- https://www.dubberly.com/concept-maps/tic-tac-toe.html
- https://www.talkingelectronics.com/projects/TicTacToe/TicTacToe-P1.html
- https://xkcd.com/832/

## links

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
