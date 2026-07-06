from PIL import Image
img = Image.open("C:\Users\HP\Desktop\HandmadeVsMachinemade_Images\pexels-ahmet-ciftci-1413580052-27205138.jpg").convert("RGB")
img = Image.resize((224,224))
img.save("C:\Users\HP\Desktop\HandmadeVsMachinemade_Images\pexels-ahmet-ciftci-1413580052-27205138.jpg")