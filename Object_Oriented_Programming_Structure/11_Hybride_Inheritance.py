class A:
    def method1(self):
        print("a")
class B(A):
    def method2(self):
        print("b")
class C(A):
    def method3(self):
        print("c")
class D(A,B):
    def method4(self):
        print("d")

obj=D()
obj.method4() # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B