x = str(input("File name: "))

if "gif" in x:
    print("image/gif")
elif "jpg" in x:
    print("image/jpeg")
elif "jpeg" in x:
    print("image/jpeg")
elif "png" in x:
    print("image/png")
elif "pdf" in x:
    print("image/pdf")
elif "txt" in x:
    print("image/txt")
elif "zip" in x:
    print("image/zip")
else:
    print("application/octet-stream")