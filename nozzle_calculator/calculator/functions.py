def translate_type_name(name):
    polish_names = {'Complete st. st. inside': 'wnętrze nierdzewne',
                    'St. st. ring inside': 'pierścień kawitacyjny nierdzewny',
                    'Complete steel': 'wnętrze ze stali zwykłej',
                    'St. st. ring and outlet': 'pierścień kawitacyjny i wylot ze stali nierdzewnej'}
    return polish_names[name]