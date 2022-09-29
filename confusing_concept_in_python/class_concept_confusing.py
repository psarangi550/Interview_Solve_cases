class A(object):
    def test(self):
        print("A")
    def __init__(self):
        self.test()
class B(A):
    def __init__(self):
        self.test()
    def test(self):
        super().test()
        print("B")
a=A()
b=B()

