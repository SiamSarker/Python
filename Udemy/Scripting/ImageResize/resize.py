from PIL import Image

img = Image.open('alexandre-debieve.jpg')
# print(img.size)

new_img = img.resize((400, 400))

new_img.save('resized.jpg')

new_img.show()