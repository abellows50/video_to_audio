from pytube import YouTube
import sys

def downloadYouTube(videourl, name):
    try:
        yt = YouTube(videourl)
    except:
        print("Connection Error") #to handle exception
    audiofiles = yt.streams.filter(only_audio=True)
    d_video = audiofiles[1]
    try:
        d_video.download(output_path="./data", filename=name)
    except Exception as e:
        print(e)
    

def processLinks(URL):
    URL = [x.strip() for x in URL]
    toDownload = []
    for url in URL:
        url = url.split(',')
        download = [url[0], url[1]]
        toDownload.append(download)
    return toDownload

def main():
    try:
        URL = sys.argv[1]
        NAME = sys.argv[2]

        downloadYouTube(URL, NAME)
        
    except:
        print("No arguments given")
        with open('links.csv', 'r') as file:
            URL = file.readlines()
        numfiles = len(URL)
        filesProcessed = 0
        toDownload = processLinks(URL)
        for download in toDownload:
            filesProcessed += 1
            print(f"Processing file {filesProcessed} of {numfiles}")
            downloadYouTube(download[0], download[1])
            print(f"File {filesProcessed} of {numfiles} processed!")
  

main()