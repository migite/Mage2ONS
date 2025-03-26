import os
import sys
import glob
import re
from PIL import Image

same_hierarchy = os.path.dirname(os.path.abspath(__file__))
system_dir=os.path.join(same_hierarchy,'data')

senario_dir=os.path.join(system_dir,'txt')
picture_dir=os.path.join(system_dir,'pic')

with open(os.path.join(same_hierarchy, 'default.txt')) as f:
    txt = f.read()

pathlist = glob.glob(os.path.join(senario_dir, '*.txt'))
# ========================================================================
# ここから画像切り出し。テキストウインドウなど。

def image_crop(input_image,x1,y1,x2,y2,img_dir,renamed_picture):
    
    im_Crop = input_image.crop((x1, y1, x2, y2))
    im_Crop.save(os.path.join(img_dir, renamed_picture +'.png'))
    return

def subwindow_crop(input_image,img_dir,renamed_picture):
    
    im_Crop = input_image.crop((4,0,253,150))
    im_Crop.save(os.path.join(img_dir, renamed_picture +'_1.png'))

    im_Crop = input_image.crop((4,151,253,301))
    im_Crop.save(os.path.join(img_dir, renamed_picture +'_2.png'))
    return

Open_picture = Image.open(os.path.join(system_dir, 'mes_win.png'))
image_crop(Open_picture,12,380,800,592,system_dir,'textwindow1')

Open_picture = Image.open(os.path.join(system_dir, 'mes_win2.png'))
image_crop(Open_picture,0,0,800,600,system_dir,'textwindow2')

#これ以降の画像は使わないかも
n = 0
UI_picture = ['copy','endmenu','endmenu2','format','ret_select','ret_title','return','saveconfirmmenu']

for f in UI_picture:
    Open_picture = Image.open(os.path.join(system_dir, UI_picture[n] +'.png'))
    subwindow_crop(Open_picture,system_dir,UI_picture[n])
    n += 1


# ========================================================================


for snr_path in pathlist:
    with open(snr_path, encoding='cp932', errors='ignore') as f:
        print(pathlist)
        def Theme_BGM_replace(input):

            line = line.replace('#絵麻のテーマ','bgm "bgm\\m_01.wav"')
            

        

        for line in f:
           
            line = line.replace('#絵麻のテーマ','bgm "bgm\\m_01.wav"')
            line = line.replace('#千尋のテーマ','bgm "bgm\\m_02.wav"')
            line = line.replace('#桐李のテーマ','bgm "bgm\\m_03.wav"')
            line = line.replace('#一葉のテーマ','bgm "bgm\\m_04.wav"')
            line = line.replace('#青井のテーマ','bgm "bgm\\m_05.wav"')
            line = line.replace('#楽しい日常のテーマ','bgm "bgm\\m_06.wav"')
            line = line.replace('#通常の日常のテーマ','bgm "bgm\\m_07.wav"')
            line = line.replace('#暗め日常のテーマ','bgm "bgm\\m_08.wav"')
            line = line.replace('#静かな不安のテーマ','bgm "bgm\\m_09.wav"')
            line = line.replace('#激しい不安のテーマ','bgm "bgm\\m_10.wav"')
            line = line.replace('#孤独のテーマ','bgm "bgm\\m_11.wav"')
            line = line.replace('#回想／夢のテーマ','bgm "bgm\\m_12.wav"')
            line = line.replace('#擦れ違い／切なさのテーマ','bgm "bgm\\m_13.wav"')
            line = line.replace('#悲しみのテーマ','bgm "bgm\\m_14.wav"')
            line = line.replace('#泣きのテーマ','bgm "bgm\\m_15.wav"')
            line = line.replace('#怪しい夢のテーマ','bgm "bgm\\m_16.wav"')
            line = line.replace('#子ども時代のテーマ','bgm "bgm\\m_17.wav"')
            line = line.replace('#別世界のテーマ','bgm "bgm\\m_18.wav"')
            line = line.replace('#敵のテーマ','bgm "bgm\\m_19.wav"')
            line = line.replace('#寄り添いのテーマ','bgm "bgm\\m_20.wav"')
            line = line.replace('#幸福のテーマ','bgm "bgm\\m_21.wav"')
            line = line.replace('#スタッフロール','bgm "bgm\\m_22.wav"')
            line = line.replace('#タイトル画面','bgm "bgm\\m_23.wav"')
            line = line.replace('#ＯＰ','bgm "bgm\\m_24.wav"')
            line = line.replace('#ＥＤ','bgm "bgm\\m_25.wav"')
            line = line.replace('#挿入歌','bgm "bgm\\m_26.wav"')

            txt += line


open (os.path.join(same_hierarchy, '0.txt'), 'w', errors='ignore').write(txt)