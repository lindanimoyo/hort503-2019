from sys import argv

script, filename = argv

toberead = open(filename)

print(toberead.read())

toberead.close()
