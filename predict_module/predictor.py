import torch
import torch.nn as nn
from predict_module.features_predictor.predictor import FeaturePredictor
from predict_module.desciption_predictor.predictor import DescriptionPredictor
from predict_module.modification_predictor.predictor import ModificationPredictor


class RoundModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 1)
        self.func = nn.ReLU()

    def forward(self, x):
        res = self.fc1(x)
        res = self.func(res)
        return res


class Predictor:

    def __init__(self):
        self._model = torch.load('../predict_module/models/round_model.pth')
        self._features_predictor = FeaturePredictor()
        self._description_predictor = DescriptionPredictor()
        self._modification_predictor = ModificationPredictor()
        self._price_max_value = 17490370

    def _format_price(self, price):
            price = int(price)
            price_str = str(price)[::-1]
            groups = [price_str[i:i + 3] for i in range(0, len(price_str), 3)]
            formatted_price = ' '.join(groups)
            return f'{formatted_price[::-1]}'

    def predict(self, brand, model, year, breed, milage, milage_history,
                pts, n_owners, condition, engine_capacity, engine_type,
                transmission, drive_unit, equipment, body_type, color,
                steering_wheel, description, modification):

        features_prediction = self._features_predictor.predict(
            brand, model, year, breed, milage, milage_history, pts, n_owners, condition, engine_capacity, engine_type,
            transmission, drive_unit, equipment, body_type, color, steering_wheel
        )
        description_prediction = self._description_predictor.predict(description)
        modification_prediction = self._modification_predictor.predict(modification)
        predict = self._model(torch.FloatTensor([features_prediction, description_prediction, modification_prediction]))
        return self._format_price(predict * self._price_max_value)


