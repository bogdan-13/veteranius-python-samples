def main():
    get_connection()
    print('Saving test data to DB')

def get_connection():
    print('Retrieving one connection from pool...')

# __name var holds name of the current module
print(f'Executing code inside {__name__}')

# we use this if guard to not execute some code if script gets imported as a module
if __name__ == '__main__':
    main()    
