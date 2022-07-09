class father:
  age=40
  def __init__(self):
    print("this is init by father")

class son (father):
    age=18
    def __init__(self):
       print("this is init by son")

son1=son()
