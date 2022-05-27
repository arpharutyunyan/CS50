name = input("File name: ")
name = name.split(".")[1].lower().rstrip().lstrip()
ext_list = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]

image = "image/"
if name in ext_list:
    if name in ext_list[:4]:
        if name == "jpg":
            name = "jpeg"
            print(image + name)
        else:
            print(image + name)
    elif name == "pdf":
        print("application/" + name)
    elif name == "txt":
        print("text/plain")
    elif name == "zip":
        print("application/zip")
else:
    print("application/octet-stream")