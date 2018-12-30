import requests

def download_file(name, url):
    import os
    if not os.path.exists('videos'):
        os.makedirs('videos')
    name = 'videos/' + name + ".mp4"
    print("Downloading to '%s' from '%s'" % (name, url))
    r = requests.get(url)
    with open(name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=255): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
        print("Done")