import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class MyPlotLib:
    def __init__(self) -> None:
        pass

    @staticmethod
    def __get_figures(count):
        if count <= 4:
            num_rows = 1
            num_cols = count
        else:
            num_rows = int(count / 4) + (count % 4 > 0)
            num_cols = 4
        fig, axs = plt.subplots(num_rows, num_cols, figsize=(16, 8))
        return fig, axs

    @staticmethod
    def histogram(data, features):
        try:
            if not features:
                return None
            features = list(set(features))
            data = data[features].dropna().select_dtypes(include=[np.number])
            fig, axs = MyPlotLib.__get_figures(len(features))
            if len(features) > 1:
                for i, feature in enumerate(features):
                    sns.histplot(data=data, x=feature, ax=(axs[i // 4, i % 4] if len(features) > 4 else axs[i]))
                    (axs[i // 4, i % 4] if len(features) > 4 else axs[i]).legend([feature], fontsize="x-small")
            else:
                sns.histplot(data=data, x=features[0], ax=axs)
                axs.legend(features, fontsize="x-small")
            plt.show()
        except Exception:
            return None

    @staticmethod
    def density(data, features):
        try:
            if not features:
                return None
            features = list(set(features))
            data = data[features].dropna().select_dtypes(include=[np.number])
            for i, feature in enumerate(features):
                sns.kdeplot(data=data, x=feature)
                plt.legend(features, fontsize="x-small")
            plt.show()
        except Exception:
            return None

    @staticmethod
    def pair_plot(data, features):
        try:
            if not features:
                return None
            features = list(set(features))
            data = data[features].dropna().select_dtypes(include=[np.number])
            sns.pairplot(data=data, vars=features)
            plt.show()
        except Exception:
            return None

    @staticmethod
    def box_plot(data, features):
        try:
            if not features:
                return None
            features = list(set(features))
            data = data[features].dropna().select_dtypes(include=[np.number])
            sns.boxplot(data=data, orient="v")
            plt.legend(features, fontsize="x-small")
            plt.show()
        except Exception:
            return None

if __name__ == "__main__":
    mpl = MyPlotLib()
    features = []
    data = pd.read_csv("../athlete_events.csv")
    mpl.histogram(data, features)
    mpl.density(data, features)
    mpl.pair_plot(data, features)
    mpl.box_plot(data, features)
    
    features = ["Height"]
    data = pd.read_csv("../athlete_events.csv")
    mpl.histogram(data, features)
    mpl.density(data, features)
    mpl.pair_plot(data, features)
    mpl.box_plot(data, features)
    
    features = ["Height", "Weight"]
    data = pd.read_csv("../athlete_events.csv")
    mpl.histogram(data, features)
    mpl.density(data, features)
    mpl.pair_plot(data, features)
    mpl.box_plot(data, features)
    
    features = ["Height", "Weight", "Age"]
    data = pd.read_csv("../athlete_events.csv")
    mpl.histogram(data, features)
    mpl.density(data, features)
    mpl.pair_plot(data, features)
    mpl.box_plot(data, features)
    
