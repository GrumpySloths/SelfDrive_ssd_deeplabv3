import cv2
from torchvision import transforms as T
from PIL import Image
from torch.utils.data import Dataset,DataLoader
import os
import numpy as np
import imageio




def Myloader(path):
    return cv2.imread(path)


def get_data(data_path):
    data = []
    for file in os.listdir(data_path):
        
        image_path = os.path.join(data_path, file)
        data.append(image_path)
    return data


class MyDataset(Dataset):
    def __init__(self, data, transform, loader):
        self.data = data
        self.transform = transform
        self.loader = loader

    def __getitem__(self, item):
        img_path= self.data[item]
        img = self.loader(img_path)
        img = self.transform(img)
        return img

    def __len__(self):
        return len(self.data)


def load_data(batch_size):
    transform=T.Compose([
    T.ToTensor(),
    # T.Resize(520),
    # T.Normalize(mean=NORM_MEAN,std=NORM_STD)
    # transforms.Resize((256,400))
])

    path1 = './data/frame'
    data1 = get_data(path1)

    dataset=MyDataset(data1, transform=transform, loader=Myloader)

    test_data = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0, pin_memory=True)


    return test_data