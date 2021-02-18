# 2020 qualification round. Did not actually participate.
# https://codingcompetitions.withgoogle.com/hashcode/archive

from pathlib import Path

class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
    
    def __repr__(self):
        return str(self.__dict__)

class Library:
    def __init__(self, id, N, T, M, books):
        self.id = id
        self.N = N # N = number of books in library
        self.T = T # T = number of days it takes to sign up
        self.M = M # M = number of books ship per day once signed up
        self.books = books
        
        # self defined
        self.term_idx = 0
        self.to_send = []
        self.ltr = 0
    
    def __repr__(self):
        return f'(ID: {self.id} LTR: {self.ltr})'

    def get_book_ids_to_send(self):
        return [book.id for book in self.to_send]

    # long term return: a composite score?
    def calculate_ltr(self, D, day, book_sent):
        days_left = D - day - self.T
        if days_left <= 0:
            return 0

        max_per_day = self.M
        num_books_allowed = days_left * max_per_day
        to_send = self.to_send

        for idx, book in enumerate(self.books[self.term_idx:]):
            if len(to_send) >= num_books_allowed:
                self.term_idx = idx
                break
            if book.id not in book_sent:
                to_send.append(book)

        self.to_send = to_send
        if len(to_send) >= num_books_allowed:
            # more time needed than books to send
            self.term_idx = len(self.books)
        return sum(map(lambda x: x.score, self.to_send))

    def update_old_book(self, book_sent):
        updated_to_send = []
        for book in self.to_send:
            if book.id not in book_sent:
                updated_to_send.append(book)
        self.to_send = updated_to_send
    
    def update(self, **kwargs):
        day = kwargs.pop('day')
        D = kwargs.pop('D')
        book_sent = kwargs.pop('book_sent')
        self.update_old_book(book_sent)
        self.ltr = self.calculate_ltr(D, day, book_sent)

def book_scan(filename, freq):
    FILE = filename
    INPUT = Path(f'inputs/{FILE}')
    OUTPUT = Path(f'outputs/{FILE}')

    with open(INPUT, 'r') as f:
        lines = f.readlines()

    # B different books, L different libraries, D number of days
    BLOCK = 2
    OFFSET = 2
    B,L,D = (int(s) for s in lines[0].split())
    scores = {idx: int(s) for idx, s in enumerate(lines[1].split())}
    libraries = []
    for idx in range(L):
        N, T, M = (int(s) for s in lines[BLOCK*idx+OFFSET].split())
        books = sorted([Book(int(s), scores[int(s)]) for s in lines[BLOCK*idx+OFFSET+1].split()], key=lambda x: x.score)
        libraries.append(Library(idx, N, T, M, books))

    # Note: the only thing we want is sign up order, then book sending order
    RESULT = []
    book_sent = set()
    day = 0
    update_frequency = freq
    TERMINATE = False

    # looping through each day
    while day < D and len(libraries) and not TERMINATE:
        # max ltr is right, min ltr is left, thus pop()
        if day % update_frequency == 0:
            for lib in libraries:
                if day > 0 and lib.ltr <= 0:
                    TERMINATE = True
                    break
                lib.update(day=day, D=D, book_sent=book_sent)
            libraries.sort(key=lambda x: x.ltr)
        # we always want the last library since it has largest ltr, can change to dequeue
        library = libraries[-1]
        RESULT.append(library)
        book_sent.update(library.get_book_ids_to_send())    
        libraries.pop() # removing the added library
        day += 1
        TERMINATE = TERMINATE or (library.ltr <= 0)

    with open(OUTPUT, 'w+') as f:
        num_library = len(RESULT)
        f.write(f'{num_library}\n')
        for library in RESULT:
            books_to_scan = ' '.join(map(str, library.get_book_ids_to_send()))
            f.write(f'{library.id} {len(library.to_send)}\n')
            f.write(f'{books_to_scan}\n')

FILES = ['a_example.txt', 'b_read_on.txt', 'c_incunabula.txt', 'd_tough_choices.txt', 'e_so_many_books.txt', 'f_libraries_of_the_world.txt']
FREQUENCIES = [1,1,100,14000,15,100]

for idx, f in enumerate(zip(FILES, FREQUENCIES)):
    EXCLUDE = []
    if idx in EXCLUDE:
        continue
    print(f'Scanning {f[0]}')
    book_scan(f[0], f[1])
print('Finished analysis')