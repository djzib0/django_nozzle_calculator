def translate_type_name(name):
    polish_names = {'Complete st. st. inside': 'wnętrze nierdzewne',
                    'St. st. ring inside': 'pierścień kawitacyjny nierdzewny',
                    'Complete steel': 'wnętrze ze stali zwykłej',
                    'St. st. ring and outlet': 'pierścień kawitacyjny i wylot ze stali nierdzewnej'}
    return polish_names[name]


def possible_year(start_year, end_year):
    p_year = []
    new_tuple = ()
    for year in range(end_year, start_year, -1):
        new_tuple = str(year), year
        p_year.append(new_tuple)
    return p_year


def calculate_nozzle_welding_material_and_hours(nozzle):
    """Calculates welding material and welding hours, baed on dimensions of Nozzle model"""
    test_result = round(nozzle.diameter / 100)
    return test_result


