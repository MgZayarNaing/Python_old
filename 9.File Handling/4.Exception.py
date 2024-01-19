try:
    file = open("aa.txt", "r")
except IOError:
    print("File Not Found")
else:
    print(file.read())