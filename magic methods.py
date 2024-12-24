class Book:
    def __init__(self, title,  author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    def __eq__(self,other):
        return self.title == other.title and self.author == other.author
    def __lt__(self,other):
        return self.num_pages < other.num_pages
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    def __add__(self,other):
        return self.num_pages + other.num_pages
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key {key} was not found"

book1 = Book("The Hobbit","J.R.R",340)
book2 = Book("Harry Potter","J.k",400)
book3 = Book("The lion","C.S",175)

#print(book1)  #this gives memory address. to customize that we use dunder string method def __str__(self):

print(book1)
print(book2)
print(book3)

print(book1 == book2) #dunder method to check if two object are equal
# if they have same title same author same num_pages it still show False as they are on diff memory address
# to solve this make dunder method def __eq__(self):
# now if name nd author are same it returns True

# print(book1<book2) error so lets change it def __lt__(self):
print(book1<book2)
print(book1>book3)
print(book1+book2)
print("Harry" in book2)
print(book2['title'])
print(book1['author'])
print(book3['num_pages'])
print(book2['audio'])
