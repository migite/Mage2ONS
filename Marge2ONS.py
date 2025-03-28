import os
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

#音楽、背景、立ち絵はエイリアスが使われているので(対応はuser.txt参照)
            #変換処理をしたいが、いまいち良い方法がわかりません。
            #今のままだと立ち絵関連で2400行くらいになるんだな、これが。
            #背景は正規表現でくくれそうなので大丈夫
            #取得する変数使ってBGM_listのやつみたいにぶん回すのが多分正解
    BGM_list = {'#絵麻のテーマ':'bgm "bgm\\m_01.wav"','#千尋のテーマ':'bgm "bgm\\m_02.wav"',
                '#桐李のテーマ':'bgm "bgm\\m_03.wav"','#一葉のテーマ':'bgm "bgm\\m_04.wav"',
                '#青井のテーマ':'bgm "bgm\\m_05.wav"','#楽しい日常のテーマ':'bgm "bgm\\m_06.wav"',
                '#通常の日常のテーマ':'bgm "bgm\\m_07.wav"','#暗め日常のテーマ':'bgm "bgm\\m_08.wav"',
                '#静かな不安のテーマ':'bgm "bgm\\m_09.wav"','#激しい不安のテーマ':'bgm "bgm\\m_10.wav"',
                '#孤独のテーマ':'bgm "bgm\\m_11.wav"','#回想／夢のテーマ':'bgm "bgm\\m_12.wav"',
                '#擦れ違い／切なさのテーマ':'bgm "bgm\\m_13.wav"','#悲しみのテーマ':'bgm "bgm\\m_14.wav"',
                '#泣きのテーマ':'bgm "bgm\\m_15.wav"','#怪しい夢のテーマ':'bgm "bgm\\m_16.wav"',
                '#子ども時代のテーマ':'bgm "bgm\\m_17.wav"','#別世界のテーマ':'bgm "bgm\\m_18.wav"',
                '#敵のテーマ':'bgm "bgm\\m_19.wav"','#寄り添いのテーマ':'bgm "bgm\\m_20.wav"',
                '#幸福のテーマ':'bgm "bgm\\m_21.wav"','#スタッフロール':'bgm "bgm\\m_22.wav"',
                '#タイトル画面':'bgm "bgm\\m_23.wav"','#ＯＰ':'bgm "bgm\\m_24.wav"',
                '#ＥＤ':'bgm "bgm\\m_25.wav"','#挿入歌':'bgm "bgm\\m_26.wav"'}



# ========================================================================

for snr_path in pathlist:

    with open(snr_path, encoding='cp932', errors='ignore') as f:

        nametag = ''
        
        for line in f:
            comment_line = re.match(r'％(\S+)',line)
            voice_line = re.match(r'#VOICE=VOICE\\(\S+)\\(\S+)',line)
            name_text = re.match(r'/{0,4}【(\S+)】',line)
            text_line = re.match(r'^[^ -~｡-ﾟ]{3,}',line)
            repage_line = re.match(r'#NEXT',line)
            bgm_line = re.fullmatch(r'#[^ -~｡-ﾟ]{1,8}のテーマ\n|#スタッフロール|#タイトル画面|#ＯＰ|#ＥＤ',line)
            bg_line = re.match(r'#bg_(\d+)(\S+)',line)

            line = line.replace('#MES_WINDOW_OFF','setwin0')
            line = line.replace('#MES_WINDOW_LOAD','setwin1')
            line = line.replace('#NOVEL_WINDOW_LOAD','setwin2')


            if comment_line:
                line = ';;' + comment_line[1] + '\n'

            elif voice_line:
                #print(line)

                line = 'dwave 1,"voice\\' + voice_line[1] + '\\' + voice_line[2] + '"\n'

            elif name_text:
                nametag = name_text[1]
                #print(line)
                line = '\n'
            
            elif text_line:

                if re.match(r'^[^ -~｡-ﾟ]{3,}\＠',line):
                    line = '[' +nametag + ']' + line.replace('＠','@') + '\n'
                    nametag = ''

                else:
                    line = '[' +nametag + ']' + line + '\n'

            elif repage_line:
                nametag = ''
                line = '\\\n' 

            elif bgm_line:
                for line in BGM_list:
                    print(line)
                    line = BGM_list[line] + '\n'

            elif bg_line:
                bg_trance =  re.match(r'#bg_(\d+)(\S+)、(\S+){1,3}',line)
                if bg_trance:
                    match bg_trance[3]:
                        case '曇り':
                            line = 'lsp 39,":a;data\\pic\\bg\\' + 'bg_' + bg_trance[1] + '_c.png",0,0\nprint 1\n'
                        case '夕方':
                            line = 'lsp 39,":a;data\\pic\\bg\\' + 'bg_' + bg_trance[1] + '_y.png",0,0\nprint 1\n'
                        case '夜':
                            line = 'lsp 39,":a;data\\pic\\bg\\' + 'bg_' + bg_trance[1] + '_n.png",0,0\nprint 1\n'
                        case '過去':
                            line = 'lsp 39,":a;data\\pic\\bg\\' + 'bg_' + bg_trance[1] + '.png",0,0\nprint 1\n'
                        case '消灯':
                            line = 'lsp 39,":a;data\\pic\\bg\\' + 'bg_' + bg_trance[1] + '_sh.png",0,0\nprint 1\n'

                    line = line.replace('bg_23_n.png"','bg_23.png')
                else:
                    match bg_line[2]:
                        case '夜空－差分':
                            line = 'lsp 39,":a;data\\pic\\bg\\' + 'bg_' + bg_line[2] + '_a.png",0,0\nprint 1\n'
                        case '夜空':
                            line = 'lsp 39,":a;data\\pic\\bg\\' + 'bg_' + bg_line[2] + '_b.png",0,0\nprint 1\n'
                        case '病院廊下－差分':
                            line = 'lsp 39,":a;data\\pic\\bg\\' + 'bg_' + bg_line[2] + '_a.png",0,0\nprint 1\n'
                        case '病院廊下':
                            line = 'lsp 39,":a;data\\pic\\bg\\' + 'bg_' + bg_line[2] + '_b.png",0,0\nprint 1\n'

                        case _:
                            line = 'lsp 39,":a;data\\pic\\bg\\' + 'bg_' + bg_line[2] + '.png",0,0\nprint 1\n'


            txt += line


open (os.path.join(same_hierarchy, '0.txt'), 'w', errors='ignore').write(txt)