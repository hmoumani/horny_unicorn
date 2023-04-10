from FileLoader import FileLoader

def youngest_fellah(df, year):
    df = df[df['Year'] == year]
    male_min = df[df['Sex'] == 'M']['Age'].min()
    female_min = df[df['Sex'] == 'F']['Age'].min()
    return {"f": female_min, "m": male_min}
    
if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("../athlete_events.csv")
    print(youngest_fellah(data, 1992))
    # output is: "{'f': 12.0, 'm': 11.0}"

    print(youngest_fellah(data, 2004))
    # output is: "{'f': 13.0, 'm': 14.0}"

    print(youngest_fellah(data, 2010))
    # output is: "{'f': 15.0, 'm': 15.0}"

    print(youngest_fellah(data, 2003))
    # output is: "{'f': nan, 'm': nan}"
