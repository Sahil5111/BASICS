class father:
    age = 40
    def __init__(self):
        print("this is init by father")

    def work(self):
        print("working")


class son (father):
    age = 18

    def __init__(self):
        print("this is init by son")

    def play(self):
        print("playing")

son1 = son()
dad1=father()

dad1.work()
son1.play()
son1.work()