import numpy as np

def get_score_grid(w,d):
    n = w**(d//2 - 1)
    print(f"{n}x{n} matrix")
    score_grid_d = np.zeros((n, n)) 
    return score_grid_d



def show_index_score_grid(w,d):
    n = w**(d//2 - 1)
    num_of_grids = n * n
    matrix = np.arange(num_of_grids).reshape(n, n)
    return matrix



# print(np.arange(81).reshape(9, 9))

if __name__ == "__main__":
    w = 3
    d4 = 4 
    d6 = 6

    # print(get_score_grid(w, d4))
    # print(show_index_score_grid(w, d4))


    # print(get_score_grid(w, d6))
    # print(show_index_score_grid(w, d6))

    d8 = 8
    # print(get_score_grid(w, d8))
    # print(show_index_score_grid(w, d8))


    print(np.zeros((9,9), dtype=int))
