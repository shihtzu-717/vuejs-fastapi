import os
import shutil
from typing import List
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware  # NEW

IMAGE_DIR='../input_test'
SERVER_IMG_URL=os.path.join('http://localhost:8080', 'img')

app = FastAPI()
image_list =[]
# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/')
async def create_file(iou_thresh: str = Form(), thresh: str = Form(), model_name: str = Form(), image_list: List[UploadFile] = File()):
    print(model_name, iou_thresh, thresh, image_list)
    return {
        "model_name": model_name,
        "iou_thresh": iou_thresh,
        "thresh": thresh,
        "image_list": image_list
    }

@app.get('/')
async def get_inference():
    global image_list
    print(image_list)
    return image_list