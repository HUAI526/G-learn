
class MyClass:
    count = 0
    name = 'Default Name'
    
    def __init__(self, name):
        self.name = name
        print('�O�O���ܼƬO%s\n������ , �����ܼƬO%s' % (MyClass.name, self.name))
     
    def setCount(self, count):
        self.count = count
         
    def selgetCount(self):
        return self.count 
    
if __name__  == "__main__":
    cls = MyClass('lisi')
    cls.setCount(10)
    print('count=%d' % cls.getCount()) 