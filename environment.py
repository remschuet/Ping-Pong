class A:
    def hello(self):
        print("Hello")


class B:
    hello = A.hello


b = B()
b.hello()

