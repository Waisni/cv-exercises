import torch
from PIL import Image
import numpy as np


class horizontal_flip(torch.nn.Module):
    """
    Flip the image along the second dimension with a probability of p
    """

    def __init__(self, p):
        super().__init__()
        self.p = p

    def forward(self, img):
        # convert the image to numpy
        # draw a random number
        # flip the image in the second dimension 
        # if this number is smaller than self.p
        x = img.numpy()
        r = np.random.rand(1)[0]
        if r < self.p:
            x = np.flip(x, axis=1)
        return torch.from_numpy(x.copy())


class random_resize_crop(torch.nn.Module):
    """
    simplified version of resize crop, which keeps the aspect ratio of the image.
    """

    def __init__(self, size, scale):
        """ initialize this transform
        Args:
            size (int): size of the image
            scale (tuple(int)): upper and lower bound for resizing image"""
        super().__init__()
        self.size = size
        self.scale = scale

    def _uniform_rand(self, low, high):
        return np.random.rand(1)[0] * (low - high) + high

    def forward(self, img):
        #Perform a random resize crop
        # convert the image to numpy
        # draw a random number for the scale
        # scale the image
        # draw a random number for the position
        # crop the image
        # convert the image back to a tensor
        x = img.numpy()
        h, w = x.shape[1:]
        scale = self._uniform_rand(self.scale[0], self.scale[1])
        new_h, new_w = int(h * scale), int(w * scale)
        x = np.resize(x, (3, new_h, new_w))
        h, w = x.shape[1:]
        top, left = 0, 0
        if int(self.size * scale) < h and int(self.size * scale) < w:
            top = np.random.randint(0, h - self.size)
            left = np.random.randint(0, w - self.size)
        x = x[:, top:top + self.size, left:left + self.size]
        return torch.from_numpy(x.copy())
