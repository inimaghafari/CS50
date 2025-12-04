text = input("send your file name: ")

result = text.lower().strip().split(".")[-1]

if result in ("jpg", "jpeg"):
    print("image/jpeg")
elif result == "gif":
    print("image/gif")
elif result == "png":
    print("image/png")
elif result == "txt":
    print("text/plain")
elif result == "pdf":
    print("application/pdf")
elif result == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
