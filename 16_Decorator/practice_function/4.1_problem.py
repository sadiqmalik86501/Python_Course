class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __str__(self):
        print(f"{self.title} by Author {self.author}")
    def __len__(self):
        return len(self.title)

b=Book("Hello  so that printing the object displays","Harry")
print(len(b))
