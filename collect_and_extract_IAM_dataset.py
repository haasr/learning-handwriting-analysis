import stow
import tarfile
from tqdm import tqdm
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import os

def download_and_unzip(url, extract_to='Datasets', chunk_size=1024*1024):
    http_response = urlopen(url)

    data = b''
    iterations = http_response.length // chunk_size + 1
    for _ in tqdm(range(iterations)):
        data += http_response.read(chunk_size)

    zipfile = ZipFile(BytesIO(data))
    zipfile.extractall(path=extract_to)

os.makedirs('Datasets/IAM_Words')
dataset_path = stow.join('Datasets', 'IAM_Words')
download_and_unzip('https://git.io/J0fjL', extract_to='Datasets')

file = tarfile.open(stow.join(dataset_path, "words.tgz"))
file.extractall(stow.join(dataset_path, "words"))