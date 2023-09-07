'''

'''
import contextlib
import os
import queue
import requests
import sys
import threading
import time
#! 不需要关心的文件类型，主要关注HTML和文本文件
FILTERED = [
    ".jpg",
    ".gif",
    ".png",
    ".css"
    ]
#! 攻击目标的URL
TARGET = "http://boodelyboo.com/wordpress"
THREADS = 10

answers = queue.Queue()
web_paths = queue.Queue()

def gather_paths()->None:
    '''gather_path'''
    for root , _  , files in os.walk('.'):
        for fname in files:
            if os.path.splitext(fname)[1] in FILTERED:
                continue
            path = os.path.join(root,fname)
            if path.startswith('.'):
                path = path[1:]
            print(path)
            web_paths.put(path)
            
@contextlib.contextmanager
def chdir(path):
    '''
    On enter,change directory to specified path
    On exit ,change directory to original
    '''
    this_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    except Exception:
        print(Exception)
    finally:
        os.chdir(this_dir)

if __name__ == "__main__":
    with chdir("/home/tim/Downloads/wordpress"):
        gather_paths()
    input("Please return to continue")