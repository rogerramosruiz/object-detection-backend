import string
import os
import random
import numpy as np

from config.environment import filename_size, public_dir, models_dir, names


def random_file_name():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        fileName = ''.join(random.choice(letters) for _ in range(filename_size))    
        fileName = f'{public_dir}/{fileName}'
        if not os.path.exists(fileName):
            return fileName

def load_colors():
    classes = []
    with  open(names, 'r') as f:
        classes = [i.strip() for i in f.readlines()]
    return np.random.uniform(0, 255, size = (len(classes), 3)), classes

def get_model(model_dir):
    modelPath = os.path.join(models_dir, model_dir)
    weights   = os.path.join(modelPath, os.listdir(modelPath)[0]) 
    return weights