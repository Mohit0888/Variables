#And your understanding is incorrect. __init__ is called when the object is created, __
# enter__ when it is entered with with statement, and these are 2 quite distinct things.
# Often it is so that the constructor is directly called in with initialization,
# with no intervening code, but this doesn't have to be the case.
class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self):
        self.file.close()

 # using with statement with MessageWriter


with MessageWriter('my_file.txt') as xfile:
    xfile.write('hello world')