import os
import uvicorn
import shutil
from typing import List
from fastapi import FastAPI, Form, UploadFile, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from opencv import api_image, api_video, live_video
from helpers.utilities import random_file_name, create_public

from config.environment import PUBLIC_DIR, WEIGHTS_DIR ,GPU_USE, PORT, PRODUCTION

# craete public directory if it dosen't exists
create_public()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

app.mount("/public", StaticFiles(directory=PUBLIC_DIR), name="public")

@app.get('/')
def get():
    return {'meesage': "Object Detection"}

@app.get('/gpu')
def use_GPU():
    return {'gpu': GPU_USE}

@app.get('/models')
def get_weights():
    weights = os.listdir(WEIGHTS_DIR)
    return {'models': weights}

@app.post('/image')
async def image(file: UploadFile, model: str= Form(''), confidence: float = Form(0)):
    confidence = confidence / 100
    ext = file.filename.split('.')[-1]
    file_name = random_file_name()
    file_name = f'{file_name}.{ext}'
    with open(f'{file_name}', 'wb') as f:
        shutil.copyfileobj(file.file, f)
    api_image(path= file_name, model= model,confidence = confidence)
    return {'filename':file_name}

@app.post('/video')
async def video(file: UploadFile, model: str= Form(''), confidence: float = Form(0)):
    confidence /= 100
    ext = file.filename.split('.')[-1]
    file_name = random_file_name()
    file_name = f'{file_name}.{ext}'
    with open(f'{file_name}', 'wb') as f:
        shutil.copyfileobj(file.file, f)
    file_name1 = random_file_name()
    video_path = api_video(file_name,file_name1, model, confidence)
    return {'filename':video_path}

@app.post('/uploads')
async def file_upload(files: List[UploadFile]):
    saved_files = []
    for file in files:
        ext = file.filename.split('.')[-1]
        file_name = random_file_name()
        file_name = f'{file_name}.{ext}'
        saved_files.append(file_name)
        with open(f'{file_name}', 'wb') as f:
            shutil.copyfileobj(file.file, f)
    return {'filename':saved_files}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await live_video(websocket)

if __name__ == '__main__':
    uvicorn.run("main:app", host = '0.0.0.0', port = PORT, reload = not PRODUCTION)