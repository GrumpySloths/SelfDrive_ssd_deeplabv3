import torch
import PIL
import numpy as np
import torchvision
from torchvision.models.detection import SSD300_VGG16_Weights
import os
from torchvision import transforms 
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import utils
import dataloader_ssd

device=torch.device("cpu") if not torch.cuda.is_available() else torch.device("cuda:0")
print("using device:",device)
weights=SSD300_VGG16_Weights.DEFAULT
model = torchvision.models.detection.ssd300_vgg16(weights=weights).to(device)
model.eval()
id_to_name=weights.meta["categories"]

MyTransform=transforms.Compose([
    transforms.ToTensor(),
])
print("开始加载数据")
dataloader=dataloader_ssd.load_data(1)
print("将输入图片转化为语义分割图片")
utils.savefig_ssd(dataloader,model,device,id_to_name)
print("制作gif图片")
utils.MakeGif_segmentation()
