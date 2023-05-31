import torch
import pickle
from predict_module.processors import TextVariableProcessor


class ModificationProcessor:

    def __init__(self):
        self._processor = TextVariableProcessor()

    def process(self, processed_record):
        vector = self._processor.process(processed_record['modification'])
        return torch.FloatTensor(vector)
