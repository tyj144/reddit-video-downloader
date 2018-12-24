from get_html import get_html_from_url
import bs4
from video_dl import download_file
import sys
import re, string

def main():
    if (len(sys.argv) == 2):
        print('''
     _                                  _     _                _ _
 ___| |_ _ __ ___  __ _ _ __ ___   __ _| |__ | | ___        __| | |
/ __| __| '__/ _ \/ _` | '_ ` _ \ / _` | '_ \| |/ _ \_____ / _` | |
\__ \ |_| | |  __/ (_| | | | | | | (_| | |_) | |  __/_____| (_| | |
|___/\__|_|  \___|\__,_|_| |_| |_|\__,_|_.__/|_|\___|      \__,_|_|
        ''')
        url = sys.argv[1]
        download_from_url(url)
    else:
        print('Usage: http.py <url>')

def get_name_from_url(url):
    name = ''
    for i in range(len(url) - 1, 0, -1):
        if url[i] == '/':
            return re.sub(r'\W+', '', name)
        else:
            name = url[i] + name
    return re.sub(r'\W+', '', url)


def download_from_url(url):
    html = get_html_from_url(url)

    soup = bs4.BeautifulSoup(html, 'html.parser')
    video_tag = soup.find('video')

    src = 'https:' + video_tag.attrs['src']

    name = get_name_from_url(url)
    print('name', name)

    download_file(name, src)

if __name__ == "__main__":
    main()