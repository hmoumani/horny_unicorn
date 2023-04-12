from FileLoader import FileLoader

def proportion_by_sport(df, year, sport, gender):
    unique_df = df.drop_duplicates(subset=['Name', 'Year'])
    selected_year_df = unique_df[unique_df['Year'] == year]
    selected_gender_df = selected_year_df[selected_year_df['Sex'] == gender]
    selected_sport_df = selected_gender_df[selected_gender_df['Sport'] == sport]
    return round(len(selected_sport_df) / len(selected_gender_df) * 100, 1)


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../athlete_events.csv')
    print("")

    print(proportion_by_sport(data, 2004, 'Tennis', 'F'), end = "\n\n")
    # output is "0.01935"

    print(proportion_by_sport(data, 2008, 'Hockey', 'F'), end = "\n\n")
    # output is  "0.04127"

    print(proportion_by_sport(data, 1964, 'Biathlon', 'M'), end = "\n\n")
    # output is "0.00916"

