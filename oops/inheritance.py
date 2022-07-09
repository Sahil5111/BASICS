class node1:
    age = 40
    def __init__(self):
        print("this is init by node1")

    def work(self):
        print("working1")

class node2:
    age=38
    def __init__(self) -> None:
        print("this is init by node2")
    def work(self):
        print("working2")

class son (node1,node2):
    age = 18

    def __init__(self):
        print("this is init by child")
    def play(self):
        print("playing")

son1 = son()
dad1=node1()

dad1.work()
son1.play()
son1.work()#work funtions calls work from line 6 because when inheriting properties precedence is from left to right
# i.e interpreter will first check node1for the funtion then check node2