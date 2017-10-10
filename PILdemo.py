# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rdmCh():
    return chr(random.randint(65, 90))


def rdmColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rdmColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width, height = 240, 60
img = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(img)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rdmColor())
font = ImageFont.truetype('aller-bold.ttf', 36)
for t in range(4):
    draw.text((60*t+10,10),rdmCh(),font=font,fill=rdmColor2())
img = img.filter(ImageFilter.BLUR)
img.save('code.jpg', 'jpeg')
