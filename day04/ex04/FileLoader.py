import pandas as pd

class FileLoader:
    def load(self, path):
        try:
            df = pd.read_csv(path)
            print("Loading dataset of dimensions {} x {}".format(df.shape[0], df.shape[1]))
            return df
        except Exception:
            return None
        
    def display(self, df, n):
        try:
            if isinstance(n, int) == False:
                return
            if n < 0:
                print(df.tail(-n))
            else:
                print(df.head(n))
        except Exception:
            return None
            
if __name__ == "__main__":
    file_loader = FileLoader()
    df = file_loader.load("../athlete_events.csv")
    file_loader.display(df, 3)
    file_loader.display(df, -3)
    file_loader.display(df, 0)
    file_loader.display(df, "lol")
