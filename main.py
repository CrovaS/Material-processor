try: import sound_module as sm
except: pass
try: import text_module as tm
except: pass

def ok(welldone):
    if welldone == 0: return "Well Done!"
    elif welldone == 1: return "Error..."
    else: return "What is it?"

def converse(typemode):
    if typemode == 1: return 'pptpdftotxt'
    elif typemode == 2: return 'listmode'
    elif typemode == 3: return 'singlemode'
    elif typemode == 4: return 'cuttingtube'
    elif typemode == 5: return 'cuttingsound'
    elif typemode == 6: return 'mp4tomp3'
    else: return None

folder_directory="C:/Ekenda Bia/ppt-txt-shrinker"
welldone = 0
mode = None

print("사용 설명서")
print("------------------")
typemode = input("사용하실 모드를 숫자로 입력해주세요(1/2/3/4/5/6): ")
mode = converse(typemode)

if mode == None: print("모드를 잘못 입력하셨습니다.")
elif mode == 'pptpdftotxt':
    welldone = tm.pdf_ppt_extraction(directory = folder_directory)
    print(ok(welldone))
else:
    welldone = sm.sound_mode_selector(umode = mode, directory = folder_directory)
    print(ok(welldone))