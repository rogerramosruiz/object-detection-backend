import os
from dotenv import load_dotenv
load_dotenv()

PORT          = int(os.getenv('PORT', 8000))
PRODUCTION    = os.getenv('PRODUCTION').lower() == 'true'
FILENAME_SIZE = int(os.getenv('FILE_NAME_SIZE'))
PUBLIC_DIR    = os.getenv('PUBLIC_DIR')
WEIGHTS_DIR   = os.getenv('WEIGHTS_DIR')
MODEL_CFG     = os.getenv('MODEL_CFG')
NAMES         = os.getenv('NAMES_FILE')
GPU_USE       = os.getenv('GPU', 'False').lower() == 'true'