with open('temp.file', 'r+') as temp:
    temp.write('Hello')

# try:
#     temp = open('temp.file', 'x')
#     temp.write('Hello Python World')
# finally:
#     temp.close()


class MyCloseable:
    def __init__(self):
        self.resource = open('temp.file', 'r+')

    def write_str(self, value: str = 'Hello'):
        self.resource.write(value)

    def __enter__(self):
        return self

    def __exit__(self,exc_type, exc_value, traceback):
        print('Closing MyCloseable...')
        self.resource.close()

with MyCloseable() as temp:
    temp.write_str('My Python created file')
    temp.write_str()