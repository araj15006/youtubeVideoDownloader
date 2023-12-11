from pytube import YouTube
from pytube import Playlist

# Single video download function
def ytVideoDownloader():
    url = str(input("Paste URL here:\n"))
    try:
        print("Please wait while we get available resolutions...")

        video = YouTube(url)
        title = video.title
        res = video.streams.all()
        resList = list(enumerate(res))

        for i in resList:
            print(i)

        option = int(input("Select any option\n"))
        res[option].download()
        print("Your video has been downloaded")

    except:
        print("Unable to get information or check your internet connection")


# Playlist downloading function   
def ytPlaylistDownload():
    url = str(input("Paste URL here:\n"))
    try:
        playlist = Playlist(url)
        print(f"Downloading Playlist: {playlist.title}")
        video_urls = playlist.video_urls
        res = ["360p", "720p", "1080p"]

        for i, item in enumerate(res):
            print(f"{i}.{item}")

        user_res = int(input("Select resolution: "))   

        i = 1
        for video_url in video_urls:
            video = YouTube(video_url)
            print(f"Downloading: {video.title}")
            stream = video.streams.filter(res=f"{res[user_res]}").first() 
            if stream:
                stream.download()
                print(f"Video number {i} Downloaded")
            else:
                print(f"Video number {i} not Downloaded")  
            i += 1

        print("Your playlist has been downloaded")    
    except:
        print("Unable to get information or check your internet connection.")

# Function calls        
if __name__ == "__main__":
    var = str(input("Press 1 for video\nPress 2 for playlist\n"))
    if var == "1":
       ytVideoDownloader()
    elif var == "2":
        ytPlaylistDownload()
    else:
        print("Invalid option")
