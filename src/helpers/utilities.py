import string
import os
import random
import numpy as np

from config.environment import FILENAME_SIZE, PUBLIC_DIR, WEIGHTS_DIR, NAMES


def random_file_name():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        fileName = ''.join(random.choice(letters) for _ in range(FILENAME_SIZE))    
        fileName = f'{PUBLIC_DIR}/{fileName}'
        if not os.path.exists(fileName):
            return fileName

def load_colors():
    classes = []
    with  open(NAMES, 'r') as f:
        classes = [i.strip() for i in f.readlines()]
    return np.random.uniform(0, 255, size = (len(classes), 3)), classes

def get_model(model_dir):
    model_path = os.path.join(WEIGHTS_DIR, model_dir)
    weights   = os.path.join(model_path, os.listdir(model_path)[0]) 
    return weights

def create_public():
    if not os.path.exists(PUBLIC_DIR):
        os.mkdir(PUBLIC_DIR)