#User Class will keep track of users
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User's email address updated")

    def __repr__(self):
        return "User: " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books))
        
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return "Same User"
    
    def read_book(self, book, rating = None):
        if rating == None:
            self.books[book] = None
        elif rating >= 0 and rating <= 4:
            self.books[book] = rating
        else:
            print("Invalid Rating")
    
    def get_average_rating(self):
        average_rating = 0
        for value in self.books.values():
            if value == None:
                continue
            elif value >= 0 and value <= 4:
                average_rating += value
        return (average_rating / len(self.books))
    
#Book Class will keep track of Books    
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The book's isbn was updated")
    
    def add_rating(self, rating):
        if rating == None:
            pass
        elif rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return "Same Book"
    
    def get_average_rating(self):
        average_rate = 0
        for value in self.ratings:
            if value == None or value == 0:
                continue
            elif value > 1 and value <= 4:
                average_rate += value
        if average_rate == 0:
            return 0
        else:
            return (average_rate / len(self.ratings))
    
    def __hash__(self):
        return hash((self.title, self.isbn))

#Fiction is a Sub-class of Books        
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author    
    
    def __repr__(self):
        return self.title + " by " + self.author

#Non-Fiction is a Sub-class of Books        
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level
        
    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject

#TomeRater will allow for interaction between the User and Book Classes        
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
        self.isbn = []

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        if isbn in self.isbn:
            print("This book already exists")
        else:
            self.books[new_book] = 0
            self.isbn.append(isbn)
            return new_book
    
    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        if isbn in self.isbn:
            print("This novel already exists")
        else:
            self.books[new_novel] = 0
            self.isbn.append(isbn)
            return new_novel    
    
    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        if isbn in self.isbn:
            print("This non fiction already exists")
        else:
            self.books[new_non_fiction] = 0
            self.isbn.append(isbn)
            return new_non_fiction
        
    def add_book_to_user(self, book, email, rating = None):
        if email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email " + email + "!")
     
    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        if email in self.users:
            print("This user already exists")
        else:
            new_email = email + " "
            list = [".com ", ".edu ", ".org "]
            if "@" in new_email:
                for ext in list:
                    if ext in new_email:
                        self.users[new_user.email] = new_user
                        break
                else:
                    print("Invalid email address")
            else:
                print("Invalid email address")
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)
    
    def print_catalog(self):
        for book in self.books:
            print(book)
    
    def print_users(self):
        for user in self.users:
            print(user)    
            
    def most_read_book(self):
        return max(self.books.items(), key=lambda k: k[1])
    
    def highest_rated_book(self):
        ratings_list = {}
        for book in self.books:
            ratings_list[book] = book.get_average_rating()
        return max(ratings_list.items(), key=lambda k: k[1])
    
    def most_positive_user(self):
        user_ratings_list = {}
        for user in self.users:
            user_ratings_list[user] = self.users[user].get_average_rating()
        return max(user_ratings_list.items(), key=lambda k: k[1])        
        