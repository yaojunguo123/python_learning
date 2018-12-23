# -*- coding: utf-8 -*-

import itchat
import math
from PIL import Image
import os


itchat.auto_login()#微信扫码登录
friends = itchat.get_friends(update=True)#获取好友列表
num = 0
if not os.path.exists("image"):
	os.mkdir("image")
for friend in friends:
	img = itchat.get_head_img(userName = friend['UserName'])#获取好友头像图片
	# 循环生成图片保存到 image 文件夹
	fileImage = open('image'+'/'+str(num)+'.jpg','wb')
	fileImage.write(img)
	fileImage.close()
	num += 1
all_image = os.listdir('image')
each_size = int(math.sqrt(float(640*640)/len(all_image))) #每个图片在最后图片中的大小
print(each_size)
lines = int(640/each_size) #图片的边长
image = Image.new('RGB',(640,640))
x = 0
y = 0
for i in range(0,len(all_image)):
	try:
		img = Image.open('image'+"/"+str(i)+".jpg")#打开之前获得的图片  该表尺寸 放到 img里面
		img = img.resize((each_size,each_size),Image.ANTIALIAS)
		image.paste(img,(x*each_size,y*each_size))
		x += 1
		if x== lines:
			x=0
			y += 1
	except:
		pass
image.save('image'+"/"+"all.jpg")#baocun
itchat.send_image('image'+"/"+"all.jpg",'filehelper')  # 发送到文件传输助手


