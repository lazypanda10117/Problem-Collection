from collections import deque 
from pathlib import Path


def book_score(filename):
    FILE = filename
    INPUT = Path(f'inputs/{FILE}')
    OUTPUT = Path(f'outputs/{FILE}')
    
    with open(INPUT, 'r') as f:
        lines = f.readlines()
    
    B,L,D = (int(s) for s in lines[0].split())
    scores = {idx: int(s) for idx, s in enumerate(lines[1].split())}

    libraries = {}
    for idx in range(L):
        N, T, M = (int(s) for s in lines[2*idx+2].split())
        libraries[idx] = (N,T,M)

    with open(OUTPUT, 'r') as f:
        lines = f.readlines()
    
    num_library = int(lines[0])

    BLOCK = 2
    OFFSET = 1
    lib_queue = deque([])
    for idx in range(num_library):
        lib_id, num_book = (int(s) for s in lines[BLOCK*idx+OFFSET].split())
        books = deque([int(s) for s in lines[BLOCK*idx+OFFSET+1].split()])
        _, T, M = libraries[lib_id]
        lib_queue.append(dict(id=lib_id, T=T, M=M, books=books))
        
    day = 0
    books_scored = set()
    library_operation = []
    library_in_line = lib_queue.popleft()

    while day < D:
        if library_in_line and library_in_line['T'] == 0:
            library_operation.append(library_in_line)
            library_in_line = None
            if len(lib_queue):
                library_in_line = lib_queue.popleft()
    
        for lib in library_operation:
            to_remove = lib['M']
            while to_remove > 0 and len(lib['books']):
                b = lib['books'].popleft()
                books_scored.add(b)
                to_remove -= 1
    
        if library_in_line:
            library_in_line['T'] -= 1
        day += 1
    
    score = 0
    for book_id in books_scored:
        score += scores[book_id]
    return score

FILES = ['a_example.txt', 'b_read_on.txt', 'c_incunabula.txt', 'd_tough_choices.txt', 'e_so_many_books.txt', 'f_libraries_of_the_world.txt']
scores = []
for f in FILES:
    print(f'Scoring {f}')
    scores.append(book_score(f))
print(scores)
print(f'Total score: {sum(scores)}')

# Example outputs
# Scoring a_example.txt
# Scoring b_read_on.txt
# Scoring c_incunabula.txt
# Scoring d_tough_choices.txt
# Scoring e_so_many_books.txt
# Scoring f_libraries_of_the_world.txt
# [21, 5822900, 1463113, 4911010, 821675, 1105913]
# Total score: 14124632

# This is an average solution at around ~52th percentile