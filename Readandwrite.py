
def write_file(content):
    with open("file.txt", "w") as file:
        file.write(content)


def read_file():
    with open("file.txt", "r") as file:
        content = file.read()
        print(content)


def append(content):
    with open("file.txt", "a") as file:
        file.write(content)

def read_file_binary():
    with open("grimjow.png", "rb") as file:
       content = file.read()
       print(content)


#write_file("This is the sample text written in the file.")

#read_file()

#append("\nThis is the sample text appended in the file.")

#print("\nAfter appending:")
#read_file()
read_file_binary()