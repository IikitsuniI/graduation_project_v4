import torch
import pickle
from predict_module.processors import TextVariableProcessor


class DescriptionProcessor:

    def __init__(self):
        self._processor = TextVariableProcessor()

    def process(self, processed_record):
        vector = self._processor.process(processed_record['description'])
        return torch.FloatTensor(vector)