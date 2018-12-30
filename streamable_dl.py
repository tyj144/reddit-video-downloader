from get_response import get_html_from_url
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


def download_from_url(url, name=None):
    html = get_html_from_url(url)

    soup = bs4.BeautifulSoup(html, 'html.parser')
    video_tag = soup.find('video')

    src = 'https:' + video_tag.attrs['src']

    if name == None:
        name = get_name_from_url(url)
    else:
        name = get_valid_filename(name)

    download_file(name, src)

def get_valid_filename(s):
    """
    (from Django)
    Return the given string converted to a string that can be used for a clean
    filename. Remove leading and trailing spaces; convert other spaces to
    underscores; and remove anything that is not an alphanumeric, dash,
    underscore, or dot.
    >>> get_valid_filename("john's portrait in 2004.jpg")
    'johns_portrait_in_2004.jpg'
    """
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)

if __name__ == "__main__":
    main()