

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

class Preprocessing:

    def categorical_column_to_numerical(self, columns):
        encoder = LabelEncoder()
        encoder.fit(columns['Gender'])
        encoded_categorical = encoder.transform(columns['Gender'])
        columns['Gender'] = encoded_categorical

        return columns


    def normalize_numerical_columns(self, columns):
        columns.drop(['CustomerID'], axis=1, inplace=True)
        normalizer = MinMaxScaler()
        normalized_data = normalizer.fit_transform(columns)

        return normalized_data
