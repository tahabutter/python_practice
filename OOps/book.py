class book:
    def __init__(self,title,author,reviews):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self,review):
        self.reviews.append(review)
        print("Review added successfully")

    def count_reviews(self):
         print("Total Reviews:", len(self.reviews))

    def display_reviews(self):
        print("Book Reviews:")

        for review in self.reviews:
            print("- " + review)
    def info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")        


b1 = book("Python Basics", "Taha", [])
b1.add_review("Great for beginners!")
b1.add_review("Well explained concepts.")

b1.count_reviews()
b1.display_reviews()
b1.info()

b2 = book("Python Basics", "hanan", [])
b2.add_review("Great for beginners!")
b2.add_review("Well explained concepts.")

b2.count_reviews()
b2.display_reviews()
b2.info()

