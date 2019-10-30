COUNTRY_WITH_CITIES = {'Poland': ['Cracow', 'Warsaw', 'Swidnica', 'Sieradz'],
                       'Russia': ['Moskow', 'Peterburg'],
                       'Italy': ['Rome', 'Torino', 'Milano']}
CITIES_TO_FIND = ['Moskow',
                  'Warsaw',
                  'Rome']
TRANSFORMATED_CITIES_LIST = {}
for country in COUNTRY_WITH_CITIES:
    for city in COUNTRY_WITH_CITIES[country]:
        TRANSFORMATED_CITIES_LIST[city] = country
for city in CITIES_TO_FIND:
    print(city, 'is located in', TRANSFORMATED_CITIES_LIST[city])
