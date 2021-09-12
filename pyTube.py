from pytube import YouTube
from pytube import Search
import os.path
from threading import Thread
import moviepy.editor as mp

def download(yt,namefile):
    # yt = YouTube('https://www.youtube.com/watch?v=' + youtubeLink)
    try:
        video = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
        video.download('./videos', namefile + ".mp4")

        mclip = mp.VideoFileClip("./videos/" + namefile + ".mp4")
        audio = mclip.audio
        audio.write_audiofile("./audios/" + namefile + '.mp3')

        os.remove("./videos/" + namefile + ".mp4")

        print("audio de "+ namefile +" baixado com sucesso!")
    except:
        print("DeuRuim")


# s = Search('Never gonna Give you up')
# if (len(s.results) > 0):    
#     download(s.results[0])

with open('xae.txt') as listamusicas:
    for line in listamusicas:
        nomeMsc = line.replace("\n","")
        if os.path.isfile("./audios/"+ nomeMsc + ".mp3"):
            print(nomeMsc + " já foi baixada")
        else:
            s = Search(line)
            if  len(s.results) > 0:
                download(s.results[0],nomeMsc)





