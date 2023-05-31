import torch
import torch.nn as nn
from predict_module.modification_predictor.processor import ModificationProcessor


class ModificationModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(384, 1)
        self.func = nn.ReLU()

    def forward(self, x):
        res = self.fc1(x)
        res = self.func(res)
        return res


class ModificationPredictor:

    def __init__(self):
        self._processor = ModificationProcessor()
        self._model = torch.load('../predict_module/models/modification_model.pth')

    def predict(self, modification):
        record = {'modification': modification}
        input = self._processor.process(record)
        return self._model(input).item()


