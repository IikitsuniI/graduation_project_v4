from sentence_transformers import SentenceTransformer


class QuantitativeVariableProcessor:

    def __init__(self, data_column):
        self._max_value = self._get_max_value(data_column)
        self._median_value = self._get_median_value(data_column)

    def _get_max_value(self, data_column):
        values = [x for x in data_column if x]
        return max(values)

    def _get_median_value(self, data_column):
        values = sorted([x for x in data_column if x])
        index = len(values) // 2
        return values[index]

    def process(self, value):
        if value:
            return self._median_value / self._max_value
        value = int(value)
        if value > self._max_value:
            value = self._max_value
        return value / self._max_value


class QualitativeVariableProcessor:

    def __init__(self, data_column):
        self._classes = self._collect_classes(data_column)

    def _collect_classes(self, data_column):
        classes = {'None': 0}
        classes_index = 1
        for value in data_column:
            value = str(value).strip()
            if value not in classes:
                classes[value] = classes_index
                classes_index += 1
        return classes

    def process(self, value):
        value = str(value).strip()
        max_value = len(self._classes)
        if value in self._classes: value = self._classes[value]
        else: value = self._classes['None']
        return value / max_value


class TextVariableProcessor:

    def __init__(self):
        self._encoder = SentenceTransformer('all-MiniLM-L6-v2')

    def process(self, value):
        return self._encoder.encode(str(value))