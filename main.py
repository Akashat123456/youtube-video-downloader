import yt_dlp
import os
from tkinter import Tk, filedialog


root = Tk()
root.withdraw()                
root.attributes('-topmost', True)


url = input("Enter YouTube video URL: ")

user_format_choice =  input("Preferred format (mp3 or mp4): ").strip().lower()




print("Please choose a folder to save the file...")
save_path = filedialog.askdirectory(title="Select Folder to Save Download")

if not save_path:
    print("❌ No folder selected. Exiting.")
    exit()


if user_format_choice == 'mp4':
    download_resolution = input('please choose downloading resolution (720por 1080p): ')

    ydl_opts = {
        'format': f'bestvideo[height={download_resolution}]+bestaudio/best',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'postprocessor_args': [
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-strict', 'experimental'
        ]
    }

elif user_format_choice == 'mp3':
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }]
    }

else:
    print("Invalid format! Choose either mp3 or mp4.")
    exit()

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])