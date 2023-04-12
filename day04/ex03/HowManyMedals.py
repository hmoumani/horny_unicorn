from FileLoader import FileLoader

def how_many_medals(df, name):
    selected_name_df = df[df['Name'] == name]
    result = {}
    group_by_year = selected_name_df.groupby('Year')
    for group in group_by_year:
        result[group[0]] = {}
        result[group[0]]['G'] = len(group[1][group[1]['Medal'] == 'Gold'])
        result[group[0]]['S'] = len(group[1][group[1]['Medal'] == 'Silver'])
        result[group[0]]['B'] = len(group[1][group[1]['Medal'] == 'Bronze'])
    return result

if __name__ == "__main__":
    data = FileLoader().load('../athlete_events.csv')
    print(how_many_medals(data, 'Gary Abraham'))
    #  the output is: "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}"

    print(how_many_medals(data, 'Yekaterina Konstantinovna Abramova'))
    #  the output is "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}"

    print(how_many_medals(data, 'Kristin Otto'))
    #  the output is: "{1988: {'G': 6, 'S': 0, 'B': 0}}"