from yt_dlp import YoutubeDL
import sys

def downloadYouTube(videourl,directory):
    dl_ops = {
      'outtmpl': directory + '%(title)s.%(ext)s',
    }
    print(f"downloading {videourl}")
    try:
        with YoutubeDL(dl_ops) as ydl:
            ydl.download([videourl])
            
    except Exception as e:
        print(e) #to handle exception
    
    

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