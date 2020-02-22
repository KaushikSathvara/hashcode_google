class Library:
    def __init__(self, l_id, buffer_time, capacity, books):
        self.books = books
        self.no_of_books = len(self.books)
        self.capacity = capacity
        self.buffer_time = buffer_time
        self.l_id = l_id
        self.l_score = self.get_library_score()
        self.processing_left = self.buffer_time
        self.scanned_books = []
        self.processing = False
        self.registered = False
        self.scanned_all_books = False

    def get_library_score(self):
        '''
        Main formula for defining library score and makes easy to 
        take which library will be scanned first
        '''
        score_list = [book.b_score for book in self.books]
        total_cost_of_books = sum(score_list)
        return (total_cost_of_books/self.buffer_time)*self.capacity

    def process_books(self):
        '''
        process book according it's capacity
        '''
        if not self.scanned_all_books and self.registered:
            count = 0
            for book in self.books:
                # only scan book if it's not scanned and some capacity is left today
                if count < self.capacity and not book.is_scanned:
                    book.is_scanned = True
                    self.scanned_books.append(book)
                    count += 1
