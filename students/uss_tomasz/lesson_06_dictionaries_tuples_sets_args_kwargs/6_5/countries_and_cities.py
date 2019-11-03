country_with_cities = {'Poland': ['Cracow', 'Warsaw', 'Swidnica', 'Sieradz'],
                       'Russia': ['Moskow', 'Peterburg'],
                       'Italy': ['Rome', 'Torino', 'Milano']}
cities_to_find = ['Moskow',
                  'Warsaw',
                  'Rome']
transformated_cities_list = {}
for country in country_with_cities:
    for city in country_with_cities[country]:
        transformated_cities_list[city] = country
for city in cities_to_find:
    print(city, 'is located in', transformated_cities_list[city])
