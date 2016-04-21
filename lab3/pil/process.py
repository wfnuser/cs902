from __future__ import print_function
import os,sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def main():
	im  = Image.open("4.png")
	im1 = Image.open("1.png")
	im2 = Image.open("2.png")
	im3 = Image.open("3.png")
	im4 = Image.open("watermark.png").resize((30,30),Image.ANTIALIAS)
	
	txt = 'wfnuser'
	font = ImageFont.truetype('font.ttf',24)

	print(im4.format, im4.size, im4.mode)
	
	box1 = (0,0,130,400)
	box2 = (131,0,270,400)
	box3 = (271,0,400,400)
	box4 = (0,0,30,30)
	box5 = (360,360,390,390)

	region = im1.crop(box1)
	im.paste(region, box1)
	
	region = im2.crop(box2)
	im.paste(region, box2)
	
	region = im3.crop(box3)
	im.paste(region, box3)

	region = im4.crop(box4)
	im.paste(region, box5)

	draw = ImageDraw.Draw(im)
	draw.text( (0,50), unicode(txt,'UTF-8'), font=font)

	
	im.save("out.jpg","JPEG")
main()
