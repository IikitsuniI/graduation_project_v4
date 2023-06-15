from pymongo import MongoClient


client = MongoClient()
collection = client['db_name']['data_processed']


def get_unique_values(field_name):
    unique_values = list()
    for record in collection.find({}, {field_name: 1}):
        value = str(record[field_name]).strip()
        if (value != 'None') and (value not in unique_values):
            unique_values.append(value)
    unique_values.sort()
    return unique_values


def get_related_unique_values(group_by_filed, filed):
    related_unique_values = dict()
    groups = get_unique_values(group_by_filed)
    for group in groups:
        related_unique_values[group] = list()
        for record in collection.find({group_by_filed: group}):
            value = record[filed]
            if (value != 'None') and (value not in related_unique_values[group]):
                related_unique_values[group].append(value)
        related_unique_values[group].sort()
    return related_unique_values


BRANDS = get_unique_values('brand')
MODELS = get_related_unique_values('brand', 'model')
COLORS = get_unique_values('color')
TYPE_BODY = get_unique_values('body_type')
STEERING_WHEEL = get_unique_values('steering_wheel')
PTS = get_unique_values('pts')
CONDITION = get_unique_values('condition')
ENGINE_TYPE = get_unique_values('engine_type')
TRANSMISSION = get_unique_values('transmission')
DRIVE_UNIT = get_unique_values('drive_unit')
N_OWNERS = get_unique_values('n_owners')




#
# COLORS = set()
# for record in collection.find({}, {'color': 1}):
#     COLORS.add(record['color'])
#
# print(COLORS)
