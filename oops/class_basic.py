class student:
    college="DBIT"

    def __init__(self,name,rollno):
        self.name=name
        self.id=rollno
        self.pc=student.laptop()

    def show(self):
        print(self.name,self.id,student.college)
        self.pc.show()
    
    class laptop:
        def __init__(self) -> None:
            self.name="dell"
            self.cpu="i5"
            self.ram="8gb"

        def show(self):
            print(self.name,self.cpu,self.ram)

    @classmethod
    def newclg(cls,name):
        cls.college=name


sahil=student("sahil",59)
aditya=student("aditya",58)
sahil.pc.cpu="i7"
sahil.show()
aditya.show()