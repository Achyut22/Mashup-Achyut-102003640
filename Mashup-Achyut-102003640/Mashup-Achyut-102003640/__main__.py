import urllib.request
import re
import pandas as pd
import random
from pytube import YouTube
from pydub import AudioSegment
import sys
import os


def main():
    if len(sys.argv) == 5:
        X = sys.argv[1]
        N =int(sys.argv[2])
        Y=int(sys.argv[3])
    else:
        print("Incorrect number of arguements ❌ ")

    print("Singer Name :",X)
    print("Number of Youtube Videos whose audio is to be extracted :",N)
    print("Duration(in sec) for which audio is to cut :",Y)

    X=X.lower()
    X=X.replace(" ", "")+"videosongs"

    html=urllib.request.urlopen("https://www.youtube.com/results?search_query="+X)
    video_ids=re.findall(r"watch\?v=(\S{11})" , html.read().decode())

    l=len(video_ids)
    url = []
    for i in range(N):
        url.append("https://www.youtube.com/watch?v=" + video_ids[random.randint(0,l-1)])

    final_aud = AudioSegment.empty()
    for i in range(N):   
        audio = YouTube(url[i]).streams.filter(only_audio=True).first()
        audio.download(filename='Audio-'+str(i)+'.mp3')
        print("\n\t\t\t\tAudio-"+str(i)+" Downloaded successfully✅")
        aud_file = str(os.getcwd()) + "/Audio-"+str(i)+".mp3"
        file1 = AudioSegment.from_file(aud_file)
        extracted_file = file1[:Y*1000]
        final_aud +=extracted_file
        final_aud.export(sys.argv[4], format="mp3")
    print("\n\t\t\t\t\tMashup Created ♫♫")

if __name__ == '__main__':
	main()

