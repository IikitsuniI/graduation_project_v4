import torch
import pickle
from predict_module.processors import QualitativeVariableProcessor, QuantitativeVariableProcessor


class FeaturesProcessor:

    def __init__(self):
        data, processed_records = pickle.load(open('data.pickle', 'rb'))
        self._data = data

    def feature_process(self, processed_record):
        vector = []
        vector.append(QualitativeVariableProcessor(self._data['brand']).process(processed_record['brand']))
        vector.append(QualitativeVariableProcessor(self._data['model']).process(processed_record['model']))
        vector.append(QuantitativeVariableProcessor(self._data['year']).process(processed_record['year']))
        vector.append(QualitativeVariableProcessor(self._data['breed']).process(processed_record['breed']))
        vector.append(QuantitativeVariableProcessor(self._data['milage']).process(processed_record['milage']))
        vector.append(QualitativeVariableProcessor(self._data['milage_history']).process(processed_record['milage_history']))
        vector.append(QualitativeVariableProcessor(self._data['pts']).process(processed_record['pts']))
        vector.append(QualitativeVariableProcessor(self._data['n_owners']).process(processed_record['n_owners']))
        vector.append(QualitativeVariableProcessor(self._data['condition']).process(processed_record['condition']))
        vector.append(QuantitativeVariableProcessor(self._data['engine_capacity']).process(processed_record['engine_capacity']))
        vector.append(QualitativeVariableProcessor(self._data['engine_type']).process(processed_record['engine_type']))
        vector.append(QualitativeVariableProcessor(self._data['transmission']).process(processed_record['transmission']))
        vector.append(QualitativeVariableProcessor(self._data['drive_unit']).process(processed_record['drive_unit']))
        vector.append(QualitativeVariableProcessor(self._data['equipment']).process(processed_record['equipment']))
        vector.append(QualitativeVariableProcessor(self._data['body_type']).process(processed_record['body_type']))
        vector.append(QualitativeVariableProcessor(self._data['color']).process(processed_record['color']))
        vector.append(QualitativeVariableProcessor(self._data['steering_wheel']).process(processed_record['steering_wheel']))
        return torch.FloatTensor(vector)