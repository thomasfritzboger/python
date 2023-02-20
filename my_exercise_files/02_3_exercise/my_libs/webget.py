import os
import urllib.request as req
from urllib.parse import urlparse

def download(url, to=None):
    if to:
        filename = to
    else:
        filename = os.path.basename(urlparse(url).path)

    if not os.path.isfile(filename):
        req.urlretrieve(url, filename)
        print(f"File saved as {filename}")
    else:
        print(f"{filename} already exists")
