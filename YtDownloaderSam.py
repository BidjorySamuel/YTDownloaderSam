"""YTDownloaderSam is a downloader videos, audios, and playlist(audios and videos) on youtube
   Made By 'Samuel Bidjory' """

#---------------------Libraries----------------------------------------#
import customtkinter
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, DoubleVar
from pytube import YouTube, Playlist
import os
from tkinter import messagebox
from tkinter import *

# Set the appearance mode in light
customtkinter.set_appearance_mode("light")

red  = "#FF0000"

green = "#00FF00"


#The path, where the contenus gonna be download
caminho = os.path.expanduser("~/Downloads")


def downloadvidaudplay():
    """function to download  audio and audio playlists, video and video playlists,respectively"""
    try:

        entry = entry_url.get()


        # Exemple links youtube: video and playlist, respectively
        #https: // www.youtube.com / watch?v = AgVgs1Iwk7I

        #https: // youtube.com / playlist?list = PLO_mu_tXvM9WJzwSas4DLWKMscegsqhK1 & si = 0
        #sbRwDpILIAny6Qm

        
        #if the entry start with the word audio, it gonna install just the audio of the link
        # You have to write it ("audio") manually
        if entry.startswith("audio"):
            download_audio()
            

        #if the caracters "watch?v" in the entry, it gonna install the video of the link
        elif "watch?v" in entry:
            download_video()
        
        #if the caracters "playlist?list" in the entry, it gonna install the playlist of the link
        elif "playlist?list" in entry:
            download_playlist_vid()
        
        #if the link doesn't exist, it gonna tell you that
        else:
            label.configure(text="Invalid Link")

        
    except Exception as e:
        messagebox.showerror("Error", "Invalid Link")


def download_video():
    entry = entry_url.get()


    video_download = YouTube(entry)
    video_download.streams.get_highest_resolution().download(output_path=caminho)
    
    label.configure(text="Video Downloaded Sucessfully")
    messagebox.showinfo("Information", "find this content in the download folder")



def download_audio():
    entry = entry_url.get()
    if "playlist" in entry:
        audio_playlist = Playlist(entry)
        for audio in audio_playlist.videos:

            down = audio.streams.filter(only_audio=True)
            down.get_audio_only().download(output_path=caminho)
            label.configure(text="Playlist Audio Downloaded Sucessfully")
    else:
        audio_download = YouTube(entry)
        down = audio_download.streams.filter(only_audio=True)
        down.get_audio_only().download(output_path=caminho)
        label.configure(text="Audio Downloaded Sucessfully")
        messagebox.showinfo("Information", "find this content in the download folder")


def download_playlist_vid():
    entry = entry_url.get()
    playlist_download = Playlist(entry)

    for video in playlist_download.videos:

        video.streams.get_highest_resolution().download(output_path=caminho)
        label.configure(text="PLaylist Downloaded Sucessfully")
    messagebox.showinfo("Information", "find this content in the download folder")




janela = CTk()

janela.title("YTDSAM")



janela.geometry("500x200")
janela.resizable(False, False)

label = CTkLabel(janela, text="Download contents", font=("Arial", 15, "bold"))
label.pack()
entry_url = CTkEntry(janela, width=400,placeholder_text="Paste the link of the video, playlist, audios")
entry_url.pack(pady=15)

button = CTkButton(janela,text="Download", width=400, command=downloadvidaudplay)
button.pack(pady=15)

lista = {"mp3": "audio", "mp4":""}

listbox = Listbox(janela, dict=lista)
listbox.pack(pady=10)

entry_url.bind("<Return>", lambda envent:downloadvidaudplay())




if __name__=="__main__":
    janela.mainloop()