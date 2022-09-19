# f1 = open('public/csv/text1.txt','a+')
# f1.write("xin chao cac ban \n")
# f1.close()

# f2 = open('public/text.txt','r+')
# print(f2.read())
# import os
# os.rename('public/text.txt', 'public/text.txt')
# os.remove('public/text1.txt')
# os.mkdir('public/csv')
# os.rmdir('public/csv')
# list = os.listdir('./')
# print(list)
# print(os.getcwd())
# print(os.path.exists('public/text2.txt'))
# print(os.path.getsize('public/text.txt'))
# print(os.path.isfile('public'))
# print(os.path.isdir('public'))
# print(os.path.dirname('public/csv/csv.csv'))
# print(os.path.getatime('public/csv/csv.csv'))
# print(os.path.getmtime('public/csv/csv.csv'))
# print(os.path.getctime('public/csv/csv.csv'))

from PIL import Image

im = Image.open("public/img/web5.png")
# print(im)
# im.save('public/img/web3.jpeg', 'JPEG')
im.thumbnail((100, 100))
im.save('public/img/web1.jpeg', 'JPEG')

