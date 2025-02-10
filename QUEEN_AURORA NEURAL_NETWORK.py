import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import matplotlib.pyplot as plt
Define Queen of Aurora class
class QueenOfAurora(nn.Module):
    def __init__(self):
        super(QueenOfAurora, self).__init__()
        # Expanded Architecture:
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5) # Input Layer: 28x28 images -> 24x24 feature maps
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5) # Hidden Layer: 24x24 feature maps -> 20x20 feature maps
        self.fc1 = nn.Linear(320, 128) # Flatten -> Hidden Layer: 320 units -> 128 units
        self.fc2 = nn.Linear(128, 10) # Output Layer: 128 units -> 10 units
    def forward(self, x):
        x = torch.relu(self.conv1(x)) # Activation function for conv layer
        x = torch.relu(self.conv2(x)) # Activation function for conv layer
        x = x.view(-1, 320) # Flatten
        x = torch.relu(self.fc1(x)) # Activation function for hidden layer
        x = self.fc2(x)
        return x
Initialize Queen of Aurora model
model = QueenOfAurora()
Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
Training loop (assuming dataset is loaded into trainloader)
for epoch in range(10):
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
    print('Epoch %d, Loss: %.3f' % (epoch+1, loss.item()))
print('Finished Training')
