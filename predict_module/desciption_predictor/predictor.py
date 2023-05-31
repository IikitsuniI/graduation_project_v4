import torch
import torch.nn as nn
from predict_module.desciption_predictor.processor import DescriptionProcessor


class DescriptionModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(384, 1)
        self.func = nn.ReLU()

    def forward(self, x):
        res = self.fc1(x)
        res = self.func(res)
        return res


class DescriptionPredictor:

    def __init__(self):
        self._processor = DescriptionProcessor()
        self._model = torch.load('../predict_module/models/description_model.pth')

    def predict(self, description):
        record = {'description': description}
        input = self._processor.process(record)
        return self._model(input).item()


