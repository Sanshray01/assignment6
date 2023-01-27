class Student():
    pass #WE HAVE MADE AN ENPTY CLASS STRUCTURE IS AS FOLLOWS
    '''
    year = 1

    def __init__(self, name, branch, sid, age):
        self.name = name
        self.branch = branch
        self.sid = sid
        self.age = age
    '''
class Marks(): pass
a = Student()
if isinstance(a, Student):print('Is instance.')
else: print('No')

b = Marks()
if isinstance(b, Marks):print('Is instance.')
else: print('No')

if issubclass(Student, object):print('Is sub.')
else: print('No')
if issubclass(Marks, object):print('Is sub.')
else: print('No')