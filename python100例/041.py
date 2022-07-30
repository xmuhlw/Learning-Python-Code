class Test:
    var = 0
    def test(self):
        self.var += 1
        print(self.var)
a = Test()
print(Test.var)
print(a.var)
a.test()
a.test()
a.test()
print(a.var)
print(Test.var)
