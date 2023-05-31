import torch
import pickle
from parsing_module.utils.collection_updater.updater import Updater
from predict_module.processors import QualitativeVariableProcessor, QuantitativeVariableProcessor


class FeaturesProcessor:

    def __init__(self):
        data, processed_records = pickle.load(open('../predict_module/data/data.pickle', 'rb'))
        self._brand_processor = QualitativeVariableProcessor(data['brand'])
        self._model_processor = QualitativeVariableProcessor(data['model'])
        self._year_processor = QuantitativeVariableProcessor(data['year'])
        self._breed_processor = QualitativeVariableProcessor(data['breed'])
        self._milage_processor = QuantitativeVariableProcessor(data['milage'])
        self._milage_history_processor = QualitativeVariableProcessor(data['milage_history'])
        self._pts_processor = QualitativeVariableProcessor(data['pts'])
        self._n_owners_processor = QualitativeVariableProcessor(data['n_owners'])
        self._condition_processor = QualitativeVariableProcessor(data['condition'])
        self._engine_capacity_processor = QuantitativeVariableProcessor(data['engine_capacity'])
        self._engine_type_processor = QualitativeVariableProcessor(data['engine_type'])
        self._transmission_processor = QualitativeVariableProcessor(data['transmission'])
        self._drive_unit_processor = QualitativeVariableProcessor(data['drive_unit'])
        self._equipment_processor = QualitativeVariableProcessor(data['equipment'])
        self._body_type_processor = QualitativeVariableProcessor(data['body_type'])
        self._color_processor = QualitativeVariableProcessor(data['color'])
        self._steering_wheel_processor = QualitativeVariableProcessor(data['steering_wheel'])

    def process(self, record):
        vector = []
        vector.append(self._brand_processor.process(record['brand']))
        vector.append(self._model_processor.process(record['model']))
        vector.append(self._year_processor.process(record['year']))
        vector.append(self._breed_processor.process(record['breed']))
        vector.append(self._milage_processor.process(record['milage']))
        vector.append(self._milage_history_processor.process(record['milage_history']))
        vector.append(self._pts_processor.process(record['pts']))
        vector.append(self._n_owners_processor.process(record['n_owners']))
        vector.append(self._condition_processor.process(record['condition']))
        vector.append(self._engine_capacity_processor.process(record['engine_capacity']))

        vector.append(self._engine_type_processor.process(record['engine_type']))
        vector.append(self._transmission_processor.process(record['transmission']))
        vector.append(self._drive_unit_processor.process(record['drive_unit']))
        vector.append(self._equipment_processor.process(record['equipment']))
        vector.append(self._body_type_processor.process(record['body_type']))
        vector.append(self._color_processor.process(record['color']))
        vector.append(self._steering_wheel_processor.process(record['steering_wheel']))
        return torch.FloatTensor(vector)