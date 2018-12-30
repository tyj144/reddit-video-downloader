from reddit import *
from streamable_dl import download_from_url
import sys

def main():
    if len(sys.argv) == 2:
        print('''
              _     _ _ _           _     _
 _ __ ___  __| | __| (_) |_  __   _(_) __| | ___  ___
| '__/ _ \/ _` |/ _` | | __| \ \ / / |/ _` |/ _ \/ _ \
| | |  __/ (_| | (_| | | |_   \ V /| | (_| |  __/ (_) |
|_|  \___|\__,_|\__,_|_|\__|   \_/ |_|\__,_|\___|\___/

     _                     _                 _
  __| | _____      ___ __ | | ___   __ _  __| | ___ _ __
 / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
| (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |
 \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|
        ''')
        posts = get_posts_by_subreddit(sys.argv[1])
        videos = [ post for post in posts if get_domain_name(post['url']) == 'streamable.com' ]
        for video in videos:
            download_from_url(video['url'], name=video['title'])
        print(json.dumps(videos, sort_keys=True, indent=4, separators=(',', ': ')))
    else:
        print('Usage: python http.py <subreddit_name>')

if __name__ == "__main__":
    main()