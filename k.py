import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


class KMeans(object):
    def __init__(self, file_name, k):
        self.k = k
        self.file_name = file_name

    def load_data(self):
        data_set = np.loadtxt(self.file_name, delimiter=',')
        return data_set
    # plot the features
    def plot_features(self):
        names = ['label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols',
                 'Flavanoids', 'Nonflavanoid phenols',
                 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline ']
        df = pd.read_csv(self.file_name, delimiter=",", header=None, names=names)
        df.hist(bins=50, figsize=(20, 15))
        plt.show()
    # the eclud distance

    def eclud_distance(self, x_, y_):
        return np.sqrt(np.sum((x_-y_)**2))

    # select the random centroids
    def random_centroids(self, data, k):
        m, n = data.shape
        centroids = np.zeros((k, n))
        for i in range(k):
            index = int(np.random.uniform(0, m))
            centroids[i, :] = data[index, :]
        return centroids
    # find the best centroids
    def iter_means(self):
        data = self.load_data()
        m = np.shape(data)[0]
        centroids = self.random_centroids(data, self.k)
        cluster_assment = np.mat(np.zeros((m, 2)))
        flag = True
        while flag:
            flag = False
            for i in range(m):
                min_distance = 100000.0
                min_index = -1
                for j in range(self.k):
                    distance = self.eclud_distance(centroids[j,:], data[i,:])
                    if distance < min_distance:
                        min_distance = distance
                        min_index = j
                if cluster_assment[i, 0] != min_index:
                    flag = True
                    cluster_assment[i, :] = min_index, min_distance**2
            for j in range(self.k):
                cluster = data[np.nonzero(cluster_assment[:, 0].A ==j)[0]]
                centroids[j, :] = np.mean(cluster, axis=0)
        print(centroids)


if __name__ == "__main__":
    file_name = os.getcwd()
    file_name = file_name + '\\wine.data'
    k = 3
    k_means = KMeans(file_name, k)
    k_means.plot_features()
    k_means.iter_means()

