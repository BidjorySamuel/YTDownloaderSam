"""YTDownloaderSam is a downloader videos, audios, and playlist(audios and videos) on youtube
   Made By 'Samuel Bidjory' """

#---------------------Libraries----------------------------------------#
import customtkinter
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel, CTkFrame, CTkImage, CTkComboBox, CTkProgressBar
from pytube import YouTube, Playlist
import os
from tkinter import messagebox, filedialog, scrolledtext, BooleanVar, simpledialog, ttk
from tkinter import *
import tkinter as tk
import subprocess
from PIL import Image


# Set the appearance mode in light
customtkinter.set_appearance_mode("system")


# Implement a password dialog logic ----------------------------------------------------------------#
#-----------------------------------------START-----------------------------------------------------#
"""current_dir = os.path.dirname(__file__)
path_archive = os.path.join(current_dir, "ytds.txt")#  <--------
#                                                              |
if not os.path.exists(path_archive): #If the path of this file | doesn't exist 
    with open("ytds.txt", 'w') as ytd: # will create one (w=write)
        #creating a password
        pass_input = simpledialog.askstring("Create password", "Create a password", show="\u25CF")
        #encrypt the password
        encrypt = hashlib.sha256(pass_input.encode()).hexdigest()
        # And put it in the ytds.txt file
        password_ = ytd.write(encrypt)

# If the path exist, That just gonna ask you to put your key-password
else:
    with open("ytds.txt", 'r') as ytd_: # open the file ytds.txt
        password = ytd_.read() # read it
        pass_input = simpledialog.askstring("Input", "Your password", show="\u25CF") # ask to put the keypass
        decrypt = hashlib.sha256(pass_input.encode()).hexdigest() # decrypt the password
        if pass_input == "changepass": # If you want to change the password, just write "changepass" in the Entry
            pass_input = simpledialog.askstring("Input", "Your Current password", show="\u25CF") #it will ask to put your current password
            decrypt = hashlib.sha256(pass_input.encode()).hexdigest() # It will decrypt it 
            if decrypt == password: # If the password's correct
                with open("ytds.txt", 'w') as ytd: # It will open the file
                    pass_input = simpledialog.askstring("Input", "Create a new password", show="\u25CF") # ask you to put a new password
                    encrypt = hashlib.sha256(pass_input.encode()).hexdigest() # encrypt the new password
                    password = ytd.write(encrypt) # And write it in the ytds.txt file
            else: #if the password isn't correct 
                messagebox.showerror("Error", "Incorect KeyPass") # a message dialog will apear and say that the password is incorrect
                exit() # And will exit the program
        elif decrypt!= password: #if the password isn't correct 
            messagebox.showerror("Error", "Incorect KeyPass")# a message dialog will apear and say that the password is incorrect
            exit()# And will exit the program

        else: #If the password is correct 
            messagebox.showinfo("Information", "Correct KeyPass") #You'll be able to use the softwar"""

#------------------------------------END OF THIS IMPLEMENTATION------------------------------------------------#



#The path, where the contenus gonna be download
caminho = os.path.expanduser("~/Downloads") # caminho in portugues is path


def downloadvidaudplay():
    """function to download  audio and audio playlists, video and video playlists,respectively"""
    try:
        
        
        caminho_ = filedialog.askdirectory(initialdir=caminho, title="Where do you want to save it?")


        scrolled_text.config(state="normal")


        # Exemple links youtube: video and playlist, respectively
        #https: // www.youtube.com / watch?v = AgVgs1Iwk7I

        #https: // youtube.com / playlist?list = PLO_mu_tXvM9WJzwSas4DLWKMscegsqhK1 & si = 0
        #sbRwDpILIAny6Qm

        
        #if the entry start with the word audio, it gonna install just the audio of the link
        # You have to write it ("audio") manually
        if combo_format.get() == "mp3":
            download_audio(caminho_)
            

        elif combo_format.get() == "mp4":
            download_video(caminho_)

        

        #if the link doesn't exist, do that
        else:
            download_video(caminho_)
        scrolled_text.config(state="disable")
        

        
    except Exception as e:
        scrolled_text.configure(state="normal")
        scrolled_text.insert(tk.END, "Invalid link\n")
        scrolled_text.configure(state="disable")


def download_video(cam):
    global resolution
    
    resolution = combo_quality.get()
    entry = entry_url.get()


    video_download = YouTube(entry)
    title = video_download.title
    stream = video_download.streams.filter(res=resolution).first()

    if stream:
        stream.download(output_path=cam)

    scrolled_text.insert(tk.END, f"{title}.mp4 downloaded sucessfully\n\nPath : {cam}\nResolution : {resolution}\n")
    info_vid()

def download_audio(cam):
    
    entry = entry_url.get()
    if "playlist" in entry:
        audio_playlist = Playlist(entry)
        for audio in audio_playlist.videos:

            down = audio.streams.filter(only_audio=True)
            down.get_audio_only().download(output_path=cam)
            title = audio_playlist.title
            scrolled_text.insert(tk.END, f"{title}.mp3 downloaded sucessfully\n\nPath : {cam}\nResolution : {resolution}")
            info_vid()
    else:
        audio_download = YouTube(entry)
        title = audio_download.title
        down = audio_download.streams.filter(only_audio=True)
        down.get_audio_only().download(output_path=cam)
        scrolled_text.insert(tk.END, f"{title}.mp3 Downloaded Sucessfully\n\nPath : {cam}\nResolution : {resolution}")
        info_vid()


def download_playlist_vid(cam):
    entry = entry_url.get()
    playlist_download = Playlist(entry)
    
    for video in playlist_download.videos:
        title = video.title
        
        stream = video.streams.filter(res=resolution).first()
        if stream:
            stream.download(output_path=cam)
        scrolled_text.insert(tk.END, f"{title}.mp4 downloaded sucessfully\n\nPath : {cam}\nResolution : {resolution}")

# Function to paste copied links
def past_text():
    clip_get = janela.clipboard_get()
    entry_url.delete(0, tk.END)
    entry_url.insert(0, clip_get)

# Function to show informations for the content downloaded like (title, author, etc...)
def info_vid():
    scrolled_textt.configure(state="normal")
    entry = entry_url.get()
    youtube = YouTube(entry)
    text = f"INFO\n\n- title: {youtube.title}\n- author: {youtube.author}\n- publish date: {youtube.publish_date}\n- age restricted: {youtube.age_restricted}\n- channel id: {youtube.channel_id}\n\n"
    scrolled_textt.insert(tk.END, f"{text}\n")
    scrolled_textt.configure(state="disabled")


def restart_program():
    import sys
    python = sys.executable
    os.execl(python, python, *sys.argv)


janela = CTk() # Janela in portugues is the same thing as root in this context


janela.title("YTDSAM")

current_dir = os.path.dirname("download.ico")
ico_path = os.path.join(current_dir, "download.ico")

janela.iconbitmap(ico_path)


# got the width and height of the monitor
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcul the position of the app
pos_x = (largura_tela - 400) // 2
pos_y = (altura_tela - 600) // 2

janela.geometry(f"800x600+{pos_x}+{pos_y}")
janela.resizable(False, False)


#_------------------------IMAGES FOR ELEMENTS-----------------------------#
# The image for download button
imagem_download = Image.open("images\download_direto.png")
imagem_download_convert = CTkImage(light_image=imagem_download)

# The image for paste button
imagem_paste = Image.open("images\pasta.png")
imagem_paste_convert = CTkImage(light_image=imagem_paste)
#_--------------------------------------------------------------------#

frame_func = CTkFrame(janela, width=377, height=200)
frame_func.place(x=10, y=5)

frame_thumb = CTkFrame(janela,width=377, height=200)
frame_thumb.place(x=410, y=5)

scrolled_textt = scrolledtext.ScrolledText(frame_thumb, width=40, height=10, bg="#798686", border=2, state='disable')
scrolled_textt.place(x=20, y=10)


button_pas = CTkButton(frame_func,text="", width=10, command=past_text, image=imagem_paste_convert, fg_color="green")
button_pas.place(x=330, y=168)

entry_url = CTkEntry(frame_func, width=270,placeholder_text="Paste the link of the video, playlist, audios")
entry_url.place(x=10, y=10)

button = CTkButton(frame_func,text="", width=50, command=downloadvidaudplay, image=imagem_download_convert)
button.place(x=300, y=10)

scrolled_text = scrolledtext.ScrolledText(janela, width=44, height=10, bg="#798686", border=2, state='disable')
scrolled_text.place(x=20, y=390)



var=BooleanVar(value=False)


lista_values = ["mp4","mp3"]
combo_format = CTkComboBox(frame_func,  values=lista_values, width=70)
combo_format.place(x=10, y=50)

label_warning = CTkLabel(frame_func, text="", font=("Arial", 14))
label_warning.place(x=10, y=110)



qualities_video = ["2160p","1440p","1080p","720p", "480p","360p","240p","144p"]
combo_quality = CTkComboBox(frame_func,  values=qualities_video, width=70)
combo_quality.place(x=210, y=50)


entry_url.bind("<Return>", lambda envent:downloadvidaudplay())
janela.bind("<Control-q>", lambda event: quit())
janela.bind("<Control-r>", lambda event: restart_program())




if __name__=="__main__":
    janela.mainloop()