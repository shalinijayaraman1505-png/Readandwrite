def read_file_binary():
    with open("grimjow.png", "rb") as file:
        content = file.read()

    with open("grimjow_copy.png", "wb") as new_file:
        new_file.write(content)

    print("New image file created successfully!")


read_file_binary()