from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, df) -> None:
        self.df = df
    
    def when(self, location):
        return self.df[self.df['City'] == location]['Year'].unique().tolist()
    
    def where(self, year):
        return self.df[self.df['Year'] == year]['City'].unique().tolist()
    

if __name__ == '__main__':
    from FileLoader import FileLoader
    loader = FileLoader()
    data = loader.load('../athlete_events.csv')
    # Output
    # Loading dataset of dimensions 271116 x 15
    from SpatioTemporalData import SpatioTemporalData
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    # Output
    ['Athina']
    print(sp.where(2016))
    # Output
    ['Rio de Janeiro']
    print(sp.when('Athina'))
    # Output
    [2004, 1906, 1896]
    print(sp.when('Paris'))
    # Output
    [1900, 1924]
    
    print(sp.where(2000))
    # output is: ['Sydney']

    print(sp.where(1980))
    # output is: ['Lake Placid', 'Moskva'] If a single of these locations is returned it's ok.

    print(sp.when('London'))
    # output is: [2012, 1948, 1908]
