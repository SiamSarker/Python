from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img = img.convert('L')



# filtered_img.save("blur.png", 'png')
# filtered_img.save("smooth.png", 'png')
filtered_img.save("grey.png", 'png')


# print(img.size)
# print(img.format)
# print(img.mode)
# print(dir(img))

