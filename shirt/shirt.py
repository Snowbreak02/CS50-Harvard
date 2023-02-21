import sys
from PIL import Image,ImageOps

if len(sys.argv) == 3 :
    input = str(sys.argv[1]).lstrip()
    if input.endswith(".csv"):
        try:
            images = []
            image_1 = Image.open(sys.argv[1])
            res_image = ImageOps.fit(image_1, (400, 400))
            images.append(res_image)
            image_2 = Image.open(sys.argv[2])
            res_image2 = ImageOps.fit(image_2, (500,500))
            images.append(res_image2)

        images[0].paste(images[1], box=(-50,-100), mask=images[1])
        images[0].save("after.png")


        except FileNotFoundError:
            print(f"Could not read {sys.argv[1]}")
            sys.exit(1)

    elif sys.argv[1].lower().endswith(tuple(ext))  and sys.argv[2].lower().endswith(tuple(ext)) == False:
        sys.exit("File does not exist")
        
elif len(sys.argv) < 3:
    print("Too few command-line argument")
    sys.exit(1)

else:
    print("Too many command-line arguments")
    sys.exit(1)

