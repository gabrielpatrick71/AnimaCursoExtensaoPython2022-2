from pytube import YouTube
from pytube.cli import on_progress

link = input("Insira  o link do vídeo! ")
yt = YouTube(link, on_progress_callback = on_progress)
print("Vídeo: ", yt.title)
print("Iniciando o download, aguarde alguns instates....")

ys = yt.streams.get_highest_resolution()
ys.download(output_path ="C:\youtube")