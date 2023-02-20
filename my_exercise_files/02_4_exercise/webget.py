import os
import urllib.request as req
from urllib.parse import urlparse

def download(url, to=None):
    if to:
        filename = to
    else:
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            filename = "default_file.dat"

    if not os.path.isfile(filename):
        req.urlretrieve(url, filename)
        print(f"File saved as {filename}")
    else:
        print(f"{filename} already exists")


"""
def download(url, to=None):
    if to:
        filename = to
    else:
        path = urlparse(url).path
        filename = os.path.split(path)[-1]
        if not filename:
            filename = "default_file.dat"

    if not os.path.isfile(filename):
        req.urlretrieve(url, filename)
        print(f"File saved as {filename}")
    else:
        print(f"{filename} already exists")

"""


""" 
def download(url, to=None):
    if to:
        filename = to
    else:
        with req.urlopen(url) as response:
            content_type = response.info().get("Content-Type")
            ext = content_type.split("/")[-1]
            path = urlparse(url).path
            filename = os.path.split(path)[-1]
            if not filename:
                filename = "default_file.dat"

    if not os.path.isfile(filename):
        req.urlretrieve(url, filename)
        print(f"File saved as {filename}")
    else:
        print(f"{filename} already exists")
"""  