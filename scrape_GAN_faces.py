import sys
import urllib.request
opener = urllib.request.build_opener()
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:10.0.1) Gecko/20100101 Firefox/10.0.1',
}
opener.addheaders = headers.items()

start = int(sys.argv[1])
end = int(sys.argv[2])

def scrape_img(save_path):
    response = opener.open("https://thispersondoesnotexist.com/image")
    K =  response.read()
    with open(save_path,'wb') as F:
        F.write(K)

for i in range(start,end):
    print(i)
    file_name = 'scraper/image_%s.jpg'%i
    scrape_img(file_name)

