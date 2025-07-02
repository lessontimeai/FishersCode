def print_until_you_hit(x):
    for i in range(x):
        print(i)


print_until_you_hit(10)



def does_it_end_with_ing(s:str):
    if s.endswith("ing"):
        return True
    else:
        return False

def test_does_it_end_with_ing():
    assert does_it_end_with_ing("running") == True
    assert does_it_end_with_ing("run") == False
    assert does_it_end_with_ing("swimming") == True
    assert does_it_end_with_ing("swim") == False
    assert does_it_end_with_ing("going") == True
    assert does_it_end_with_ing("go") == False
    assert does_it_end_with_ing("playing") == True
    assert does_it_end_with_ing("play") == False
    print("All tests passed!")

def time_function(func):
    import time
    start_time = time.time()
    func()
    end_time = time.time()
    print(f"Function {func.__name__} took {end_time - start_time} seconds to run.")



class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")



#pip install numpy 

import numpy as np


print(np.eye(3).dot(np.eye(3)))

print(np.log(2.714))

print(np.exp(0))

alist = [0, 1, 2, 'o']



from bs4 import BeautifulSoup

html_doc = """
<html>
  <head><title>Sample Page</title></head>
  <body>
    <h1>Welcome!</h1>
    <p>This is a <b>sample</b> HTML page.</p>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
text = soup.get_text()
print(text)