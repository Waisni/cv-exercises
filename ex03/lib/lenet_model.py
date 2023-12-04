import torch.nn as nn
from torch import Tensor as T
import torch.nn.functional as F


class LeNet(nn.Module):
    def __init__(self):
        super().__init__()
        # see model description in exercise pdf
        # generate the model
        
        # The first convolutional layer takes 3 input channels (RGB) and outputs 6 channels.
        # The second convolutional layer takes 6 input channels and outputs 16 channels.
        # The third linear layer takes 16 * 5 * 5 inputs and outputs 120 channels.
        # The fourth linear layer takes 120 inputs and outputs 84 channels.
        # The fifth linear layer takes 84 inputs and outputs 10 channels.
        self.conv1 = nn.Conv2d(3, 6, kernel_size=5, stride=1)
        self.conv2 = nn.Conv2d(6, 16, kernel_size=5, stride=1)
        self.fc1 = nn.Linear(16*5*5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.out = nn.Linear(84, 10)
        

    def forward(self, x):
        
        # Perform the forward pass of the model 
        x = self.conv1(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=2, stride=2)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, kernel_size=2, stride=2)
        x = x.view(-1, 16*5*5)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.out(x)
        
        return x