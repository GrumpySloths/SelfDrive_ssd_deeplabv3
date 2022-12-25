import torch
import torchvision
import PIL
import numpy as np
import matplotlib.pyplot as plt
from torchvision import transforms as T
from PIL import Image
from torchvision.models.segmentation import DeepLabV3_ResNet50_Weights
import scipy.io
import cv2
from torch.utils.data import Dataset,DataLoader
import os
import utils 
import dataloader_segmentation

device=torch.device("cpu") if not torch.cuda.is_available() else torch.device("cuda:0")
plt.rcParams['figure.figsize'] = (8,6)
os.environ["TORCH_HOME"] ="./" 

weights=DeepLabV3_ResNet50_Weights.DEFAULT
model = torchvision.models.segmentation.deeplabv3_resnet50(weights=weights).to(device)
model.eval()
id_to_name=weights.meta["categories"]

print("开始加载数据")
dataloader=dataloader_segmentation.load_data(4)
print(next(iter(dataloader)).shape[0])
# print("将输入图片转化为语义分割图片")
# utils.output_for_segmentation(dataloader,model,device)

# print("制作gif图片")
# utils.MakeGif_segmentation()
