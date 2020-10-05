
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from data_handler  import DataHandler
from preprocessing import Preprocessing

class Model:


    def get_data(self):
       data = DataHandler().read_data()

       return data


    def apply_preprocessing(self):
        data = self.get_data()
        data = Preprocessing().categorical_column_to_numerical(data)
        data = Preprocessing().normalize_numerical_columns(data)

        return data


    def determine_optimal_number_of_clusters(self, data):
        wcss_scores = []
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10)
            kmeans.fit(data)
            wcss_scores.append(kmeans.inertia_)

        plt.plot(range(1, 11), wcss_scores)
        plt.title('Elbow Method')
        plt.xlabel('Number of clusters')
        plt.ylabel('wcss score')
        plt.show()


    def clustering(self, data):
        kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=1000, n_init=10)
        prediction = kmeans.fit_predict(data)
        df = DataHandler().read_data()
        df['Clusters'] = prediction

        return df, kmeans


    def plot_clusters(self, data, centers):
        plt.scatter(data[data.Clusters == 0].iloc[:, 1], data[data.Clusters == 0].iloc[:, 4],
        s=5, c='red')
        plt.scatter(data[data.Clusters == 1].iloc[:, 1], data[data.Clusters == 1].iloc[:, 4],
                    s=5, c='green')
        plt.scatter(data[data.Clusters == 2].iloc[:, 1], data[data.Clusters == 2].iloc[:, 4],
                    s=5, c='yellow')
        plt.scatter(data[data.Clusters == 3].iloc[:, 1], data[data.Clusters == 3].iloc[:, 4],
                    s=5, c='purple')

        plt.scatter(centers[:, 0], centers[:, 1], s=100, c="black", marker="*")

        plt.xlabel('Gender')
        plt.ylabel('Spending Score')
        plt.show()






model = Model()
clustered_data, kmeans_model = model.clustering(model.apply_preprocessing())
model.plot_clusters(clustered_data, kmeans_model.cluster_centers_)
