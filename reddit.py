from get_response import get_json_from_url
import json

def get_posts_by_subreddit(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    json = get_json_from_url(url)
    posts = [ { "title": post["data"]["title"], "url": post["data"]["url"] } for post in json["data"]["children"] if not post["data"]["stickied"]]
    return posts

def get_domain_name(url):
    '''
    Finds the domain of a URL.
    (e.g. domain of 'https://streamable.com/' is 'streamable.com')
    '''
    start = url.find('//')
    if start != -1:
        rest = url[start + 2:]
    else:
        rest = url

    end = rest.find('/')
    if end == -1:
        return rest
    else:
        return rest[:end]

# print(get_domain_name('https://streamable.com/'))
# print(get_domain_name('https://streamable.com/evfxr'))
# print(json.dumps(get_posts_by_subreddit('nba'), sort_keys=True, indent=4, separators=(',', ': ')))