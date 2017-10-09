# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open('test.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((192, 120))
im.save('thumb.jpg', 'JPEG')

std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Michael', 'score': 98}
print(std1 == std2)


