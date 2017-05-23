import requests
from datetime import datetime

def stream_download(url, target_path, verbose=False):
    """ Efficiently download a large file """

    response = requests.get(url, stream=True)
    handle = open(target_path, "wb")
    if verbose:
        print("Beginning streaming download of %s" % url)
        start = datetime.now()
        try:
            content_length = int(response.headers['Content-Length'])
            content_MB = content_length/1048576.0
            print("Total file size: %.2f MB" %  content_MB)
        except KeyError:
            pass # allow Content-Length to be missing
    for chunk in response.iter_content(chunk_size=512):
        if chunk:  # filter out keep-alive new chunks
            handle.write(chunk)
    if verbose:
        print("Download completed in %s" %  (datetime.now()-start) )

