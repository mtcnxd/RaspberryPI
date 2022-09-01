import time

def callbacktesting(persona):
    print("Hola mundo: ", persona )

def callbackFunc(s):
    print('Length of the text file is : ', s)

def printFileLength(path, callback):
    f = open(path, "r")
    length = len(f.read())
    f.close()
    callback(length)


def myFunction(callback):
    print('Mi nombre es:')
    callback('Marcos Tzuc')

if __name__ == '__main__':
    myFunction(callbacktesting)
    printFileLength("sample.txt", callbackFunc)