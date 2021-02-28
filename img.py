from PIL import Image,ImageEnhance,ImageFilter
import os,shutil
# lista = os.listdir()
# i = 1
# for item in lista:
#     if item.endswith('.jpg'):
#         shutil.move(item,f'{os.getcwd()}/{i}.jpg')
#         i += 1

ext_tuple = ('.jpg', '.jpeg', '.png', '.tif', '.gif', '.svg', '.webp', '.raw')
def crop(img1):
    width, height = img1.size
    left = width*0.1
    top = height*0.35
    right = width - left
    bottom = height*0.93
    img1 = img1.crop((left,top,right,bottom))
    return img1

initial_path = input('Please write the path of folder: ')

folder_path = os.path.join(initial_path, "Cropped")

item_list = os.listdir(initial_path)
for item in item_list:
    for extension in ext_tuple:
            if item.endswith(extension):
                if os.path.exists(folder_path) == False: 
                    os.mkdir(folder_path)
                item_initial = os.path.join(initial_path, item)
                item_final = os.path.join(folder_path, item)
                img = Image.open(item_initial)
                img_cropped = crop(img)
                img_cropped.save(item_final)

# img1 = Image.open(r"E:\Practice\Python\practice\os\5.jpg")








# img1.save('B.jpg')
# max = (130,130)
# img1.thumbnail(max)
# img1.save(r"E:\Practice\python\projects\CalC\icons\icon3.png")


# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(1.4).save('5.jpg')
# img1.filter(ImageFilter.GaussianBlur(radius = 1.4)).save('5.jpg')