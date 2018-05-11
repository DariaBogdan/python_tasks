import argparse
from io import BytesIO
from multiprocessing.pool import ThreadPool
import os
from PIL import Image
import requests
import threading
import time


def file_processing(arg):
    """Download image by url, resize it and save.

    :param arg: tuple of int and string -- number of url and url.
    :return: None
    """
    row_num, url = arg
    global errors
    global bytes_downloaded

    try:
        response = requests.get(url.strip())
        with lock:
            bytes_downloaded += len(response.content)
        img = Image.open(BytesIO(response.content))
        img.thumbnail(size)
        img.save(os.path.join(args.dir, str(row_num).zfill(filename_length)+'.jpeg'), "JPEG")
        print(f'done img #{row_num}')
    except Exception as e:
        print(f'error img #{row_num}: {e}')
        with lock:
            errors += 1


parser = argparse.ArgumentParser(description='Downloads, resize and saves jpeg files')
parser.add_argument('urls', type=str, help='path to file with list of urls to download')
parser.add_argument('--threads', type=int, default=1, help='number of threads')
parser.add_argument('--size', type=str, default='100x100', help='width of the future thumbnail')
parser.add_argument('--dir', type=str, default='.', help='directory to save thumbnails')
args = parser.parse_args()

if not os.path.exists(args.urls):
    raise FileNotFoundError(f'No such file: {args.urls}')

size = tuple([int(x) for x in args.size.split('x')])

if not os.path.exists(args.dir):
    os.makedirs(args.dir)

with open(args.urls) as input_file:
    urls = input_file.readlines()

# define global variables
time0 = time.time()  # measuring time of executing program
errors = 0  # global counter
bytes_downloaded = 0  # global counter
filename_length = len(str(len(urls)))  # needs to make beautiful file names
lock = threading.Lock()

# make multithreading
pool = ThreadPool(args.threads)
results = pool.map(file_processing, enumerate(urls))
pool.close()
pool.join()

# print statistics
print("STATISTICS".center(40, "="))
print(f'files downloaded: {len(urls) - errors}\n'
      f'errors occurred: {errors}\n'
      f'bytes downloaded: {bytes_downloaded} ({round(bytes_downloaded / 1024 / 1024, 2)} MB)\n'
      f'time elapsed: {round(time.time() - time0, 2)} sec')