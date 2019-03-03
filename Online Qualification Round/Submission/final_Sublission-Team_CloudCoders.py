'''
Soulution by the team CloudCoders
Contact: asiriofficial@gmail.com
'''

import numpy as np
import tqdm
from random import randint


def read_input_pizza(filename):
   
    lines = open(filename).readlines()
    R, C, L, H = [int(val) for val in lines[0].split()]
    pizza = np.array([list(map(lambda item: 1 if item == 'T' else 0, row.strip())) for row in lines[1:]])
    return R, C, L, H, pizza

R, C, L, H, pizza = read_input_pizza('d_big.in')


import sympy
from random import shuffle


def get_random_available_location(slice_mask):

    nonzero_elements = np.nonzero(1 - slice_mask)
    n = len(nonzero_elements[0])
    index = randint(0, n - 1)
    return nonzero_elements[0][index], nonzero_elements[1][index]

def satisfy_constraints(location, shape, slice_mask, pizza, L, H):
    r, c = location
    dr, dc = shape
    if slice_mask[r:r+dr, c:c+dc].size == dr * dc:
        if np.all(slice_mask[r:r+dr, c:c+dc] == 0):
            if dr * dc <= H:
                tomatoes = np.sum(pizza[r:r+dr, c:c+dc])
                mushrooms = dr * dc - tomatoes
                if tomatoes >= L and mushrooms >= L:
                    return True
    return False

def cut_slice(location, shape, current_slices, slice_mask):
    r, c = location
    dr, dc = shape
    slice_mask[r:r + dr, c:c + dc] = 1
    current_slices.append((r, c, dr, dc))

def score(pizza_slices):

    s = 0
    for pizza_slice in pizza_slices:
        s += pizza_slice[2] * pizza_slice[3]
    return s

def write_output_pizza(filename, pizza_slices):
    with open(filename, 'w') as f:
        f.write(f"{len(pizza_slices)}\n")
        for slice in pizza_slices:
            r, c, dr, dc = slice
            f.write(f"{r} {c} {r+dr-1} {c+dc-1}\n")

def greedy1(fname):
    R, C, L, H, pizza = read_input_pizza(fname)
    possible_shapes = [(4, 2), (2, 4), (3, 3), (5, 2), (2, 5), (11, 1), (1,11), (2, 6), (6, 2), (3, 4), (4, 3)]
    slice_mask = np.zeros_like(pizza) # stores the sliced cells as 1 for easy lookup
    pizza_slices = [] # stores the slices we made
    for _ in tqdm.tqdm(range(20000)):
        location = get_random_available_location(slice_mask)
        shape = possible_shapes[randint(0, len(possible_shapes) - 1)]
        if satisfy_constraints(location, shape, slice_mask, pizza, L, H):
            cut_slice(location, shape, pizza_slices, slice_mask)
    #print('\n')
    #print(f"score: {score(pizza_slices)}")
    write_output_pizza(fname.split('.')[0]+'.out', pizza_slices)

    
def generate_all_shapes(L, H):
    possible_shapes = []
    for size in range(2*L, H+1):
        factors = sympy.factorint(size)
        if len(factors) == 1:
            prime = list(factors.keys())[0]
            max_exp = list(factors.values())[0]
            for exp in range(0, max_exp+1):
                factor1 = prime ** exp
                factor2 = prime ** (max_exp - exp)
                possible_shapes.append((factor1, factor2))
        elif len(factors) == 2:
            prime1, prime2 = list(factors.keys())
            max_exp1, max_exp2 = list(factors.values())
            for exp1 in range(0, max_exp1+1):
                for exp2 in range(0, max_exp2+1):
                    factor1 = prime1 ** (max_exp1 - exp1) * prime2 ** (max_exp2 - exp2)
                    factor2 = prime1 ** (exp1) * prime2 ** (exp2)
                    possible_shapes.append((factor1, factor2))
        else:
            raise NotImplementedError
    return possible_shapes

def get_random_available_location_set2(random_locations, empty_cells):
    while len(random_locations) > 0:
        candidate = random_locations.pop()
        if candidate in empty_cells:
            return candidate
    else:
        return None

def update_empty_cells(location, shape, empty_cells):
    r, c = location
    dr, dc = shape
    for rr in range(r, r+dr):
        for cc in range(c, c+dc):
            empty_cells.discard((rr, cc))
    
def main(fname, iters=30000):
    R, C, L, H, pizza = read_input_pizza(fname)
    possible_shapes = generate_all_shapes(L, H)
    slice_mask = np.zeros_like(pizza)  # stores the sliced cells as 1 for easy lookup
    pizza_slices = []  # stores the slices we made
    empty_cells = set(tuple(args) for args in np.transpose(np.nonzero(1-slice_mask)).tolist())
    random_locations = list(x for x in empty_cells)
    shuffle(random_locations)
    current_score = 0
    for _ in tqdm.tqdm(range(iters)):
        location = get_random_available_location_set2(random_locations, empty_cells)
        if location is None:
            break
        selected_shapes = []
        for shape in possible_shapes:
            if satisfy_constraints(location, shape, slice_mask, pizza, L, H):
                selected_shapes.append(shape)
        if len(selected_shapes) > 0:
            current_score = score(pizza_slices)
            shape = max(selected_shapes, key=lambda shp: current_score + shp[0]*shp[1])
            cut_slice(location, shape, pizza_slices, slice_mask)
            update_empty_cells(location, shape, empty_cells)
    print('\n')
    print(f"Total Number of Cells: {score(pizza_slices)}")
    write_output_pizza(fname.split('.')[0] + '.out', pizza_slices)

##---------------------------------- run --------------------------
main('d_big.in',iters=3000)
