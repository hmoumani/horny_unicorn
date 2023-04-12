import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class Komparator:
    def __init__(self, df) -> None:
        self.df = df
    
    def compare_box_plots(self, categorical_var, numerical_var):
        sns.boxplot(x=categorical_var, y=numerical_var, data=self.df)
        plt.show()
        
    def density(self, categorical_var, numerical_var):
        sns.kdeplot(x=numerical_var, hue=categorical_var, data=self.df)
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        sns.histplot(x=numerical_var, hue=categorical_var, data=self.df)
        plt.show()


if __name__ == "__main__":
    data = pd.read_csv("../athlete_events.csv")
    kmp = Komparator(data)
    kmp.density('Medal', 'Weight')
