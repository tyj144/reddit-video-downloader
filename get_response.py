import httplib2
import sys
import json

def main():
    if (len(sys.argv) == 2):
        print(get_html_from_url(sys.argv[1]))
    else:
        print('Usage: http.py <url>')

h = httplib2.Http('.cache')
def get_html_from_url(url):
    # get HTTP response and content from the URL
    # cache's max age is 3.65 days
    response, content = h.request(url, headers={ 'cache-control': 'max-age=315360, public' })

    # content is returned in byte format, turn it into a string
    html = content.decode('utf-8')

    return html

def get_json_from_url(url):
    # get HTTP response and content from the URL
    # cache's max age is 3.65 days
    response, content = h.request(url, headers={ 'cache-control': 'max-age=315360, public' })

    json_text = content.decode('utf-8')
    # content is returned in byte format, turn it into a string
    json_data = json.loads(json_text)

    return json_data


if __name__ == "__main__":
    main()