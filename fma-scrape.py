import urllib.request, urllib.error, urllib.parse
import sys

def get_da_pages(genre, pages):
    urls = []
    for x in range(1, pages+1):
        urls.append("https://freemusicarchive.org/genre/%s?sort=track_date_published&d=1&page=%d" % (genre, x))
    for y in range(0, len(urls)):
        req = urllib.request.Request(urls[y], headers={'User-Agent' : "Magic Browser"})
        response = urllib.request.urlopen(req)
        webContent = response.read()
        f = open(genre, 'ab')
        f.write(webContent)
        f.close

if __name__ == "__main__":
    get_da_pages(sys.argv[1].capitalize(), int(sys.argv[2]))
