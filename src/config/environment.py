import os
from dotenv import load_dotenv
load_dotenv()

port = int(os.getenv('port', 8000))
prodcution = os.getenv('production').lower() == 'true'
filename_size = int(os.getenv('file_name_size'))
public_dir    = os.getenv('public_dir')
models_dir    = os.getenv('models_dir')
model_cfg = os.getenv('modelcfg')
names = os.getenv('names_file')
GPU_USE = os.getenv('GPU', 'False').lower() == 'true'