
import  pandas as pd
from matplotlib import pyplot as plt

class Data_layer:

    def read_data(self):
        data = pd.read_csv('data/Mall_Customers.csv')

        return data

    def get_numerical_columns(self):
        data = self.read_data()
        columns = []
        for column in data:
            if data[column].dtype == 'int64' and column != 'CustomerID':
                columns.append(column)

        return columns



    def data_statistics(self):
        data = self.read_data()
        data_size = data.shape
        head = data.head()
        stats = data[self.get_numerical_columns()].describe()
        print('shape of data is:', data_size, '\n')
        print('first five elements are:', '\n', head, '\n')
        print('statistic summary of numerical values are:', '\n', stats)
        a=0


    def gender_pie_plot(self):
        df = self.read_data()
        df["Gender"].value_counts().plot(kind='pie', title='Gender Distribution',
        legend=True, autopct='%1.1f%%')
        plt.show()


    def gender_bar_plot(self):
        df = self.read_data()
        df["Gender"].value_counts().plot(kind='bar', title='Gender Distribution',
        legend=True)
        plt.show()


    def histogram_numerical_columns(self, column_name:str):
        df = self.read_data()
        df.hist(column_name)
        plt.show()


    def boxplot_numerical_columns(self, column_name:str):
        df = self.read_data()
        df.boxplot(column_name)
        plt.show()


    def densityplot_numerical_columns(self, column_name:str):
        df = self.read_data()
        df[column_name].plot.kde()
        plt.show()











dl = Data_layer()
# dl.data_statistics()
# dl.gender_pie_plot()
# dl.gender_bar_plot()

# desired input for three below methods are: 'Annual Income (k$)', 'Age', 'Spending Score (1-100)'
# dl.histogram_numerical_columns("Annual Income (k$)")
# dl.boxplot_numerical_columns('Annual Income (k$)')
# dl.densityplot_numerical_columns("Spending Score (1-100)")