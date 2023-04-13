# Object detection backend

## Table of Contents

- [Stack](#stack)
- [Fronted](#fronted)
- [Clone repo](#clone-repo)
- [Set Up](#set-up)
  - [Build OpenCV with Cuda and cuDNN in docker](#build-opencv-with-cuda-and-cudnn-in-docker)
  - [Model directory](#model-directory)
  - [.env file](#env-file)
- [Run](#run)

## Stack

<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" height="70"> <img src="https://upload.wikimedia.org/wikipedia/commons/5/53/OpenCV_Logo_with_text.png" height="70"> <img src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png" height="70"> <img src="https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/logo-and-brand/01-nvidia-logo-vert-500x200-2c50-d.png" height="70">



## Fronted

https://github.com/rogerramosruiz/object-detection-frontend

## Clone repo

```bash
git clone https://github.com/rogerramosruiz/object-detection-backend.git
cd  object-detection-backend
```
## Other branches
- main
    - Run it with python 
- docker
    - Run it in a docker container

## Set up

### Build OpenCV with Cuda and cuDNN in docker

https://github.com/rogerramosruiz/docker-opencv-gpu


### Model directory

Model directory should have:
- Model configuration file
- File with the names of the classes (obj.names)
- Weights directory containing:
    - irectories with the name of the weights and inside the weight file

e.g
```
└───object-detection-backend
    └───model
        │   obj.names
        │   yolov4.cfg
        │
        └───weights
            ├───v1
            │       yolov4-v1_final.weights
            │
            ├───v2
            │       yolov4-v2_final.weights
            │
            ├───v3
            │       yolov4-v3_best.weights
            │
            └───v4
                    yolov4-v4_10000.weights
```

### .env file

Rename .envsample file

Windows

```powershell
move .envsample .env
```

Linux

```powershell
mv .envsample .env
```

Edit .env varaibles 


## Run

```bash
docker-compose up -d
```