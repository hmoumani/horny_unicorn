import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    @staticmethod
    def __distance_between_points(point1, point2):
        return np.sum(np.abs(point1 - point2))

    def __recalculate_centroids(self, predictions_results):
        clusters_number = predictions_results[np.argsort(predictions_results[:, 0])]
        grouped_arrays = np.split(clusters_number, np.unique(clusters_number[:, 0],
                                                             return_index=True)[1])[1:]
        # print(self.centroids)
        for i, cluser in enumerate(grouped_arrays):
            self.centroids[i] = np.mean(cluser[:, 1:], axis=0)
            # print('ded', np.mean(cluser[:, 1:], axis=0))
            # print(cluser.shape)

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            self.centroids = X[np.random.choice(X.shape[0], size=self.ncentroid)]
            iter_centroids = np.zeros(self.centroids.shape)
            iter_count = 0
            while iter_count < self.max_iter:
                iter_centroids = self.centroids.copy()
                predictions = self.predict(X)
                predictions_results = np.concatenate((predictions, X), axis=1)
                self.__recalculate_centroids(predictions_results)
                iter_count += 1
                if np.all(self.centroids == iter_centroids):
                    break
            return predictions_results
        except Exception as e:
            return print(e, e.__traceback__.tb_lineno)

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        predection_vector = np.zeros((X.shape[0], 1))
        try:
            for i, elem in enumerate(X):
                dist = [self.__distance_between_points(elem, centroid) for centroid in self.centroids]
                # print(dist, np.argmin(dist))
                predection_vector[i] = np.argmin(dist)
            return predection_vector
        except Exception as e:
            return print(e)
# ded [189.35744874  95.94145755   0.80495539]
# ded [195.79102888  77.64479262   0.78798959]
# ded [174.30357777  77.24764978   0.94225128]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=str, help="the file containing the data set")
    parser.add_argument("ncentroid", help="number of centroids", type=str)
    parser.add_argument("max_iter", help="number of max iterations to update the centroids", type=str)
    args = parser.parse_args()

    try:
        args.filepath = args.filepath.replace('filepath=', '', 1)
        args.ncentroid = int(args.ncentroid.replace('ncentroid=', '', 1))
        args.max_iter = int(args.max_iter.replace('max_iter=', '', 1))
        assert args.filepath.endswith(".csv"), "Filepath must be a csv file"
        assert args.ncentroid > 0, "Number of centroids must be greater than 0"
        assert args.max_iter > 0, "Number of max iterations must be greater than 0"
        df = pd.read_csv(args.filepath, index_col=0)
        k_means = KmeansClustering(args.max_iter, args.ncentroid)
        X = df.to_numpy()
        predictions_results = k_means.fit(X)
        if predictions_results is not None and args.ncentroid == 4:
            # fig, axs = plt.subplots(1, 2, figsize=(10, 5))
            fig = plt.figure(figsize=(25, 10))
            # fig2 = plt.figure()
            # ax_count = fig2.add_subplot(111)
            ax_k_means = fig.add_subplot(1, 2, 1, projection='3d')
            ax_count = fig.add_subplot(1, 2, 2)
            clusters_number = predictions_results[np.argsort(predictions_results[:, 0])]
            grouped_arrays = np.split(clusters_number, np.unique(clusters_number[:, 0],
                                                             return_index=True)[1])[1:]
            group_with_color = zip(['red', 'blue', 'yellow', 'green'], grouped_arrays)
            for i, (color, group) in enumerate(group_with_color, 1):
                ax_k_means.scatter(group[:, 1], group[:, 2], group[:, 3], color=color)
                groups_indexs = group[:, 0]
                unique, counts = np.unique(groups_indexs, return_counts=True)
                # create a bar chart of the counts
                ax_count.bar(unique, counts, color=color)
                ax_k_means.scatter(k_means.centroids[:i, 0], k_means.centroids[:i, 1], k_means.centroids[:i, 2], marker='X', c='black', s=100)
            print(k_means.centroids)
        else:

        # if predictions_results is not None and args.ncentroid == 4:
        #     new_arr = np.zeros((predictions_results.shape[0], 2))
        #     # set the first column in the new array to be the same as the old array
        #     new_arr[:, 0] = predictions_results[:, 0]
        #     # calculate the mean of the remaining columns in the old array for each row and set them in the new array
        #     new_arr[:, 1:] = np.mean(predictions_results[:, 1:], axis=1).reshape(-1, 1)
        #     for i in range(4):
        #         plt.scatter(new_arr[:, 0], new_arr[:, 1], c=new_arr[:, 0])
        #     print(new_arr)
        
            groups_indexs = predictions_results[:, 0]
            
            unique, counts = np.unique(groups_indexs, return_counts=True)

            # create a bar chart of the counts
            plt.bar(unique, counts)

        # set labels and title
        # axs[-1].xlabel('Element')
        # axs[-1].ylabel('Count')

        # show the plot

        plt.show()

    except Exception as e:
        print(e)
        exit(1)