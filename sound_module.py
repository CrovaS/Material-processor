import os
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor as mp

def youtube_extraction(url, output_filename, mode, cuttinglist = False):
    try:
        output_path = './'+ mode + '/'
        filename = output_filename + '.' + mode
        if mode == 'mp3': status = True
        elif mode == 'mp4': status = False
        else: return 0
        YouTube(url).streams.filter(file_extension='mp4', only_audio=status).first() \
        .download(output_path=output_path, filename=filename)
        if cuttinglist:
            if mode != 'mp3' or cuttinglist[0] >= cuttinglist[1]: return 0
            else:
                ffmpeg_extract_subclip(output_filename + ".mp3", \
                cuttinglist[0], cuttinglist[1], \
                targetname = output_filename + "_modified"+".mp3")
    except: return 0
    return 1

# mp4 to mp3
def mp4_extraction(directory):
    directory = directory + '/'
    for filename in os.listdir(directory + "mp4/"):
            if filename.endswith(".mp4"): 
                directory_mp4 = directory + "mp4/" + filename
                directory_mp3 = directory + "mp3/" + filename.rsplit('.')[0] + ".mp3"
                try:
                    clip = mp.VideoFileClip(directory_mp4)
                    clip.audio.write_audiofile(directory_mp3)
                except: pass
    return 1

def sound_mode_selector(umode, directory):
    if umode == 'listmode':
        # This mode needs mode
        mode = input("추출하고 싶은 확장자를 선택하세요(mp3/mp4): ")
        # readline_all.py
        f = open("youtube_links.txt", 'r')
        count = 0
        while True:
            line = f.readline()
            if not line: break
            try:
                count = count + 1
                url = line
                output_filename = "list" + str(count)
                youtube_extraction(url, output_filename, mode, cuttinglist = False)
            except: pass
        f.close()
        return 1
    elif umode == 'singlemode':
        # This mode needs url, mode, output_filename
        url = input("추출하고 싶은 유튜브 url을 입력하세요: ")
        mode = input("추출하고 싶은 확장자를 선택하세요(mp3/mp4): ")
        output_filename = input("결과물의 이름을 정해주세요: ")
        welldone = youtube_extraction(url, output_filename, mode, cuttinglist = False)
    elif umode == 'cuttingtube': 
        # This mode needs url, output_filename, cuttinglist
        url = input("추출하고 싶은 유튜브 url을 입력하세요: ")
        output_filename = input("결과물의 이름을 정해주세요: ")
        cuttinglist = []
        cutting_start = input("추출을 시작할 시간대를 선택하세요: ")
        cutting_end = input("추출을 종료할 시간대를 선택하세요: ")
        cuttinglist.append(cutting_start)
        cuttinglist.append(cutting_end)
        welldone = youtube_extraction(url, output_filename, mode = 'mp3', cuttinglist = cuttinglist)
    elif umode == 'cuttingsound':
        # This mode needs target mp3
        output_filename = input("타겟 mp3의 이름을 입력하세요: ")
        output_filename = directory + '/mp3/' + output_filename
        cuttinglist = []
        cutting_start = input("추출을 시작할 시간대를 선택하세요: ")
        cutting_end = input("추출을 종료할 시간대를 선택하세요: ")
        cuttinglist.append(cutting_start)
        cuttinglist.append(cutting_end)
        try:
            ffmpeg_extract_subclip(output_filename + ".mp3", \
                cuttinglist[0], cuttinglist[1], \
                targetname = output_filename + "_modified"+".mp3")
            return 1
        except: return 0
    elif umode == 'mp4tomp3': 
        mp4_extraction(directory)
    else: return 0
    return welldone

# url = 'https://www.youtube.com/watch?v=roIE15sIex4'