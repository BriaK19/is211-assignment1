#!/usr/bin/env python
# coding: utf-8

# In[7]:


# assignment1_part2.py - Part 2: Simple Class
class Book:
    author: str = ""
    title: str = ""
    def __init__(self, author: str = "", title: str = "") -> None:
        self.author = author
        self.title = title
    def display(self) -> None:
        print(f"{self.title}, written by {self.author}")
def main() -> None:
    # Instantiate two objects with the required books
    book1 = Book(author="J. K. Rowling", title="Harry Potter and the Goblet of Fire")
    book2 = Book(author="Walter Scott", title="Ivanhoe: A Romance")
    # Print both by calling display()
    book1.display()
    book2.display()
if __name__ == "__main__":
    main()


# In[ ]:




