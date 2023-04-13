from FileLoader import FileLoader
import pandas as pd

def how_many_medals_by_country(df, country):
    try:
        team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey',
                    'Rowing', 'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens',
                    'Rugby', 'Lacrosse', 'Polo']
        df = df[df['Team'] == country]
        rows_with_sport_teams = df[df['Sport'].isin(team_sports)]
        rows_with_sport_teams.drop_duplicates(['Year', 'Medal', 'Event'])

        desired_data = pd.concat([rows_with_sport_teams.drop_duplicates(['Year', 'Medal', 'Event']), df[~df['Sport'].isin(team_sports)]])
        result = {}
        grouped_by_year = desired_data.groupby('Year')
        for group in grouped_by_year:
            result[group[0]] = {
                'G': len(group[1][group[1].Medal == 'Gold']),
                'S': len(group[1][group[1].Medal == 'Silver']),
                'B': len(group[1][group[1].Medal == 'Bronze']),
            }
        return result
    except Exception:
        return {}

if __name__ == "__main__":  
    loader = FileLoader()
    df = loader.load('../athlete_events.csv')
    print(how_many_medals_by_country(df, 'Morocco'))
    print(how_many_medals_by_country(df, "United States") == {1896: {'G': 11, 'S': 7, 'B': 2}, 1900: {'G': 18, 'S': 14, 'B': 13}, 1904: {'G': 65, 'S': 68, 'B': 66}, 1906: {'G': 12, 'S': 6, 'B': 6}, 1908: {'G': 34, 'S': 16, 'B': 15}, 1912: {'G': 46, 'S': 25, 'B': 36}, 1920: {'G': 87, 'S': 41, 'B': 35}, 1924: {'G': 65, 'S': 41, 'B': 36}, 1928: {'G': 39, 'S': 22, 'B': 18}, 1932: {'G': 60, 'S': 57, 'B': 43}, 1936: {'G': 30, 'S': 29, 'B': 28}, 1948: {'G': 57, 'S': 34, 'B': 30}, 1952: {'G': 55, 'S': 38, 'B': 25}, 1956: {'G': 39, 'S': 57, 'B': 21}, 1960: {'G': 83, 'S': 27, 'B': 19}, 1964: {'G': 75, 'S': 36, 'B': 28}, 1968: {'G': 86, 'S': 36, 'B': 35}, 1972: {'G': 70, 'S': 58, 'B': 33}, 1976: {'G': 62, 'S': 46, 'B': 30}, 1980: {'G': 24, 'S': 4, 'B': 2}, 1984: {'G': 143, 'S': 75, 'B': 33}, 1988: {'G': 66, 'S': 48, 'B': 36}, 1992: {'G': 79, 'S': 46, 'B': 52}, 1994: {'G': 6, 'S': 8, 'B': 5}, 1996: {'G': 98, 'S': 41, 'B': 28}, 1998: {'G': 25, 'S': 2, 'B': 3}, 2000: {'G': 69, 'S': 34, 'B': 48}, 2002: {'G': 9, 'S': 52, 'B': 9}, 2004: {'G': 65, 'S': 66, 'B': 38}, 2006: {'G': 9, 'S': 7, 'B': 32}, 2008: {'G': 64, 'S': 61, 'B': 47}, 2010: {'G': 8, 'S': 61, 'B': 20}, 2012: {'G': 82, 'S': 44, 'B': 38}, 2014: {'G': 8, 'S': 28, 'B': 16}, 2016: {'G': 95, 'S': 52, 'B': 45}})
