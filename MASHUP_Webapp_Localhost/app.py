from flask import Flask, request, render_template
import urllib.request
import re
import random
from pytube import YouTube
from pydub import AudioSegment
import sys
import os
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
   singer_name = request.form['singer_name']
   num_videos = int(request.form['num_videos'])
   duration = int(request.form['duration'])
   email = request.form['email']
   
   singer_name=singer_name.lower()
   singer_name=singer_name.replace(" ", "")+"videosongs"
   html=urllib.request.urlopen("https://www.youtube.com/results?search_query="+singer_name)
   video_ids=re.findall(r"watch\?v=(\S{11})" , html.read().decode())
   l=len(video_ids)
   url = []
   for i in range(num_videos):
      url.append("https://www.youtube.com/watch?v=" + video_ids[random.randint(0,l-1)])

   final_aud = AudioSegment.empty()
   for i in range(num_videos):   
      audio = YouTube(url[i]).streams.filter(only_audio=True).first()
      audio.download(filename='Audio-'+str(i)+'.mp3')
      aud_file = str(os.getcwd()) + "/Audio-"+str(i)+".mp3"
      file1 = AudioSegment.from_file(aud_file)
      extracted_file = file1[:duration*1000]
      final_aud +=extracted_file
      final_aud.export("102003640-output.mp3", format="mp3")
    # Create the zip file
   with zipfile.ZipFile('extracted_audio.zip', 'w') as myzip:
      myzip.write('102003640-output.mp3')

   # Send the email
   msg = MIMEMultipart()
   msg['From'] = 'mashup.achyut@gmail.com'
   msg['To'] = email
   msg['Subject'] = 'Extracted Audio File'
   msg.attach(MIMEText("Here is the extracted audio file as a zip."))
   with open("extracted_audio.zip", "rb") as f:
      attachment = MIMEBase("application", "zip")
      attachment.set_payload(f.read())
   encoders.encode_base64(attachment)
   attachment.add_header("Content-Disposition", "attachment", filename="extracted_audio.zip")
   msg.attach(attachment)

   # Connect to the email server and send the email
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login("mashup.achyut@gmail.com", "bdxxlpwygkioyity")
   server.send_message(msg)
   server.quit()

   return 'Mashup Created and Sent via Email'

if __name__ == '__main__':
   app.run(debug = True)