import os
import uvicorn
import shutil
from typing import List
from fastapi import FastAPI, Form, UploadFile, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from opencv import apiImage, apiVideo, livevideo
from helpers.utilities import random_file_name

from config.environment import public_dir, models_dir ,GPU_USE, port, prodcution


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

app.mount("/public", StaticFiles(directory=public_dir), name="public")

@app.get('/')
def get():
    return {'meesage': "Object Detection"}

@app.get('/gpu')
def useGPU():
    return {'gpu': GPU_USE}

@app.get('/models')
def getModels():
    models = os.listdir(models_dir)
    return {'models': models}

@app.post('/image')
async def file(file: UploadFile, model: str= Form(''), confidence: float = Form(0)):
    confidence = confidence / 100
    ext = file.filename.split('.')[-1]
    fileName = random_file_name()
    fileName = f'{fileName}.{ext}'
    with open(f'{fileName}', 'wb') as f:
        shutil.copyfileobj(file.file, f)
    apiImage(path= fileName, model= model,confidence = confidence)
    return {'filename':fileName}

@app.post('/video')
async def file(file: UploadFile, model: str= Form(''), confidence: float = Form(0)):
    confidence /= 100
    ext = file.filename.split('.')[-1]
    fileName = random_file_name()
    fileName = f'{fileName}.{ext}'
    with open(f'{fileName}', 'wb') as f:
        shutil.copyfileobj(file.file, f)
    fileName1 = random_file_name()
    videoPath = apiVideo(fileName,fileName1, model, confidence)
    return {'filename':videoPath}

@app.post('/uploads')
async def file(files: List[UploadFile]):
    savedFiles = []
    for file in files:
        ext = file.filename.split('.')[-1]
        fileName = random_file_name()
        fileName = f'{fileName}.{ext}'
        savedFiles.append(fileName)
        with open(f'{fileName}', 'wb') as f:
            shutil.copyfileobj(file.file, f)
    return {'filename':savedFiles}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await livevideo(websocket)

if __name__ == '__main__':
    uvicorn.run("main:app", host = '0.0.0.0', port = port, reload = not prodcution)