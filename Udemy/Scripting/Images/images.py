from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img = img.convert('L')



# filtered_img.save("blur.png", 'png')
# filtered_img.save("smooth.png", 'png')
filtered_img.save("grey.png", 'png')

# filtered_img.show()

crooked = filtered_img.rotate(90)
crooked.show()

resize = filtered_img.resize((300, 300))
resize.show()

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.show()

# print(img.size)
# print(img.format)
# print(img.mode)
# print(dir(img))

