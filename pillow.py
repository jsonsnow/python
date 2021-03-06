from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

def rndChar():
	return chr(random.randint(65, 90))

def rndColor():
	return (random.randint(64,255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 255))

width = 60 * 4
height = 60
image = Image.new('RGB',(width, height), (255, 255, 255))

font = ImageFont.truetype('Arial.ttf', 36)

draw = ImageDraw.Draw(image)

for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndColor())


for t in range(4):
	draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)
#image.show()
image.save('code.jpg','jpeg')

import requests
r = requests.get('https://www.douban.com/')
print(r.status_code)
print(r.text)

print('===============================')
r = requests.get('https://www.douban.com/search', params = {'q':'python','cat':'1001'})
print(r.url)
print(r.text)