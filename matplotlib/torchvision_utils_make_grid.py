import matplotlib.pyplot as plt
import numpy as np
import torch
import torchvision

torch.Size([4, 3, 32, 32])  # 表示四张（3，32，32）的图片，cifar中的图片


# 拼接并显示一个batch的图片
def imshow(img):
    img = img / 2 + 0.5  # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))  # 将【3，32，128】-->【32,128,3】
    plt.show()


four_picture = torch.randint(255, (4, 3, 32, 32))
image_batch = torchvision.utils.make_grid(four_picture, padding=0)
imshow(image_batch)
