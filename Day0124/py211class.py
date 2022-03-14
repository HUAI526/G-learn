
class MyClass:
    count = 0
    name = 'Default Name'
    
    def __init__(self, name):
        self.name = name
        print('費別的變數是%s\nㄝ物件 , 物件的變數是%s' % (MyClass.name, self.name))
     
    def setCount(self, count):
        self.count = count
         
    def selgetCount(self):
        return self.count 
    
if __name__  == "__main__":
    cls = MyClass('lisi')
    cls.setCount(10)
    print('count=%d' % cls.getCount()) 