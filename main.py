from email.mime import audio
from fileinput import filename
from operator import truediv
from pytube import YouTube

while True:

    format_str = input("Yüklenecek olan videonun formatı :\n1- MP4\n2- MP3\n")
    format_int = int(format_str)

    video_url = input("Yüklenecek videonun urlsini giriniz : ")

    yt = YouTube(video_url)

    video_title = yt.title

    if format_int == 1:
        video = yt.streams.get_highest_resolution()

        video.download("/Users/alikaanbuke/Desktop", filename=f"{video_title}.mp4")
        print("Youtube videonuz MP4 formatında indirildi")
    if format_int == 2:
        audio = yt.streams.filter(only_audio=True).first()

        audio.download("/Users/alikaanbuke/Desktop", filename=f"{video_title}.mp3")
        print("Youtube videonuz MP3 formatında indirildi")

