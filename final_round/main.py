import argparse

from Book import Book
from Library import Library


class PlayBookTeam:
    def __init__(self, deadline, book_score_list, libraries):
        self.deadline = deadline
        self.pile_of_libraries = self.populate_libraries(
            book_score_list, libraries)
        self.in_process_libraries = []
        self.registered_libraries = []
        self.is_busy = False  # if any library is in signup process

    def populate_libraries(self, book_score_list, libraries):
        my_libraries = []
        # Distributing books to libraries
        for l_id, library in enumerate(libraries):
            prop, books = library
            desirable_books_list = []
            for book_id in books:
                book_score = book_score_list[book_id]
                desirable_books_list.append(
                    Book(b_id=book_id, b_score=book_score))

            _, buff_time, capacity = prop
            my_libraries.append(
                Library(l_id, buff_time, capacity, desirable_books_list))
        return my_libraries

    def get_efficient_library(self):
        # TODO: make optimization to get best libraries here
        # print(
            # [f'Registration Status:{library.registered}' for library in libraries])
        for library in self.pile_of_libraries:
            if not library.registered:
                return library

    def regular_team_check(self):
        for library in self.pile_of_libraries:
            if not library.registered and library.processing_left == 0:
                self.registered_libraries.append(library)
                library.registered = True
                library.processing = False
                self.is_busy = False
                # print('processed library appended to registed queue')
            else:
                if library.processing:
                    # print("processing library found", library.l_id)
                    library.processing_left = library.processing_left - 1

    def main(self):

        while self.deadline > 0:
            # updating register libraries queue everyday
            if self.deadline % 1000 == 0:
                print("DAYS LEFT", self.deadline)
            self.regular_team_check()  # daily library status chaking

            if not self.is_busy:
                lib = self.get_efficient_library()
                # print("NEW SCANNING START for library", lib.l_id)
                lib.processing = True
                self.is_busy = True

            # processign parrallal book scanning here
            for registered_library in self.registered_libraries:
                registered_library.process_books()
            self.deadline -= 1
            # print([lib.l_id for lib in obj_playbooks.registered_libraries])
            # print("--"*20)

    def save_file(self):
        line1 = str(len(self.registered_libraries))+'\n'
        # print("line1", line1)
        lines = ""
        for library in self.registered_libraries:
            lines = lines + str(library.l_id)+" " + str(len(library.scanned_books)) + \
                "\n"+" ".join([str(book.b_id)
                               for book in library.scanned_books])+"\n"
            with open("file.txt", "w") as f:
                f.write(line1)
                f.write(lines)
        # print(lines)


parser = argparse.ArgumentParser()
parser.add_argument(
    "--filename", help="Filename you want to get output from it")
args = parser.parse_args()

input_file_name = args.filename
with open(input_file_name, 'r') as f:
    NO_OF_BOOKS, NO_OF_LIBRARY, DEADLINE = [
        int(i) for i in f.readline()[:-1].split(" ")]
    BOOK_SCORE_LIST = [int(i) for i in f.readline()[:-1].split(" ")]
    LIBRARIES = []
    temp = []
    for lines in f.readlines():
        try:
            temp.append([int(i) for i in lines[:-1].split(" ")])
        except:
            pass
        if len(temp) == 2:
            LIBRARIES.append(temp)
            temp = []
            # print(LIBRARIES)
    # print(len(LIBRARIES))


obj_playbooks = PlayBookTeam(DEADLINE, BOOK_SCORE_LIST, LIBRARIES)
obj_playbooks.main()
obj_playbooks.save_file()
