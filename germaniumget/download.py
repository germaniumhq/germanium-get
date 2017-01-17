
from tqdm import tqdm
import requests

def download_url(url, file_name):
    """ Downloads the given URL into the specified file. """
    response = requests.get(url, stream=True)

    with open(file_name, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)

