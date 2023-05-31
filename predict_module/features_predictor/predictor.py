import torch
import torch.nn as nn
from predict_module.features_predictor.processor import FeaturesProcessor


class FeaturesModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(17, 1)
        self.func = nn.ReLU()

    def forward(self, x):
        res = self.fc1(x)
        res = self.func(res)
        return res


class FeaturePredictor:

    def __init__(self):
        self._processor = FeaturesProcessor()
        self._model = torch.load('../predict_module/models/features_model.pth')

    def predict(self, brand, model, year, breed, milage, milage_history,
                pts, n_owners, condition, engine_capacity, engine_type,
                transmission, drive_unit, equipment, body_type, color,
                steering_wheel):
        record = {
            'brand': brand, 'model': model, 'year': year, 'breed': breed, 'milage': milage,
            'milage_history': milage_history, 'pts': pts, 'n_owners': n_owners, 'condition': condition,
            'engine_capacity': engine_capacity, 'engine_type': engine_type, 'transmission': transmission,
            'drive_unit': drive_unit, 'equipment': equipment, 'body_type': body_type, 'color': color,
            'steering_wheel': steering_wheel}
        input = self._processor.process(record)
        return self._model(input).item()


