def translate_type_name(name):
    polish_names = {'Complete st. st. inside': 'wnętrze nierdzewne',
                    'St. st. ring inside': 'pierścień kawitacyjny nierdzewny',
                    'Complete steel': 'wnętrze ze stali zwykłej',
                    'St. st. ring and outlet': 'pierścień kawitacyjny i wylot ze stali nierdzewnej'}
    return polish_names[name]


def count_total_calculation_hours(obj):
    print('test')



def possible_year(start_year, end_year):
    p_year = []
    new_tuple = ()
    for year in range(end_year, start_year, -1):
        new_tuple = str(year), year
        p_year.append(new_tuple)
    return p_year


