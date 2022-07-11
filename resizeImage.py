#必要なライブラリのインポート　import the required libralies
import os
import glob
from PIL import Image

#globで現在のフォルダの中のjpgファイルのパスを取得
def setting():
    print('Set the path、Either　Relative path or　Absolute path is fine ')
    path = input()
    
    print('Set the extension')
    extension = input()

    target = path+'/*.'+extension
    
    img_files = glob.glob(target)
    print(f'Your target files are {img_files}')

    
    #リサイズするサイズを指定
    print("Set the width !default is 640")
    width = input()
    width = 640 if width == "" else width
    
    print("Set the height !default is 480")
    height = input()
    height = 480 if height == "" else width
    
    print(f'you are setting is width : {width} height : {height}')
    return (path,img_files, width, height)
    #img_files = glob.glob('images/*.jpg')

#リサイズ処理
def doRiseze(path,img_files, width, height):
    for f in img_files:
        #https://note.nkmk.me/python-pillow-basic/
        #画像読み込み
        img = Image.open(f)
        #https://note.nkmk.me/python-pillow-image-resize/
        #リサイズ処理を行う
        img_resize = img.resize((width,height))
        #保管先と保管名称を指定
        file_name = os.path.basename(f)
        #例 images/名前_640x480.jpgという名前で保管される
        img_resize.save(path + '/resize' + file_name)

path,img_files, width, height = setting()
doRiseze(path,img_files, width, height)