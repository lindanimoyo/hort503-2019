from sys import argv

script, filename = argv

txt = open(filename, 'w')

usermessage = f"""We're going to erase {filename},
If you don't want that, hit CTRL-C (^C)."
If you do want that, hit RETURN"""

input(usermessage)

txt.truncate()

txt.write(input("write into the file: > "))

txt.close
