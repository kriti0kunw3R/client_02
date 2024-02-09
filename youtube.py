from tkinter import *
import pytube

# Create the main window
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("500x300")

# Create a label for the video URL
label_url = Label(root, text="YouTube Video URL:")
label_url.grid(row=0, column=0)

# Create an entry for the video URL
entry_url = Entry(root)
entry_url.grid(row=0, column=1)

# Create a button to download the video
button_download = Button(root, text="Download", command=lambda: download_video(entry_url.get()))
button_download.grid(row=1, column=1)

# Create a label to show the download status
label_status = Label(root, text="")
label_status.grid(row=2, column=0)

# Define the function to download the video
def download_video(url):
    # Create a YouTube object
    youtube = pytube.YouTube(url)

    # Get the highest quality stream
    stream = youtube.streams.get_highest_resolution()

    # Download the video
    stream.download()

    # Update the download status label
    label_status.config(text="Download complete!")

# Start the main loop
root.mainloop()