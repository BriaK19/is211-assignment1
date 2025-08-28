#!/usr/bin/env python
# coding: utf-8

# In[27]:


# assignment1_part1.py

class ListDivideException(Exception):
    """Custom exception raised when a list_divide test fails."""
def list_divide(numbers, divide=2):
    return sum(1 for n in numbers if n % divide == 0)
def test_list_divide():
    tests = [
        (([1, 2, 3, 4, 5],), {"divide": 2}, 2),
        (([2, 4, 6, 8, 10],), {}, 5),
        (([30, 54, 63, 98, 100],), {"divide": 10}, 2),
        (([],), {}, 0),
        (([1, 2, 3, 4, 5],), {"divide": 1}, 5),
    ]
    for args, kwargs, expected in tests:
        result = list_divide(*args, **kwargs)
        if result != expected:
            raise ListDivideException(
                f"Test failed for args={args}, kwargs={kwargs}: expected {expected}, got {result}"
            )
if __name__ == "__main__":
    test_list_divide()
    print("All tests passed.")


# In[29]:


get_ipython().system('ls')


# In[30]:


get_ipython().system('pwd')


# In[ ]:




