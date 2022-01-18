# Python program showing
# file management using
# context manager

class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# loading a file
with FileManager('test.txt', 'w') as f:
    f.write('Test1test')

with FileManager('first/test.txt', 'w') as f:
    f.write('123')


print(f.closed)
print(type(f))