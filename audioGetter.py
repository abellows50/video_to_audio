import requests
HTML = "<html><body>BODY</body></html>"
URL = "http://jewish-music.huji.ac.il/sites/default/files/sounds/Example{number}.mp3 "
html=""
try:
  i = 1
  while True:
    print(i)
    url = f"http://jewish-music.huji.ac.il/sites/default/files/sounds/Example{i}.mp3"
    print(url)
    response = requests.get(url)
    if("Something went wrong..." in response.text):
       i+=1
       continue;
    with open(f"{i}.mp3", "wb") as f:
     f.write(response.content)
    html+=f"<audio controls src='{url}'></audio>"
    i+=1
    if i==30:
      break
except Exception as e:
    print(e)

with open("index.html","w") as f:
  f.write(HTML.replace("BODY",html))