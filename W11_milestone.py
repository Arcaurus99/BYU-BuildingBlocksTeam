
country = ''
code = ''
year = ''
life_exp = 0

country_str = 'country'
code_str = 'code'
year_str = 'year'
life_str = 'life'

def mapReducer(year_input):

    max_val = 0                     # Starts with lowest value
    min_val = 1000                  # Starts with highest value
    lowest = {}
    highest = {}

    year_life_total = 0
    year_life_avg = 0
    year_life_expentancy_values = []
    y_max_val = 0                   # Starts with lowest value
    y_min_val = 1000                # Starts with highest value
    year_lowest = {}
    year_highest = {}
    
    with open('./life-expectancy.csv') as all_data:
        first_data = True
        for data in all_data:
            if first_data:
                first_data = False
            else:
                country, code, year, life_exp = data.split(',')
                life_exp = float(life_exp)

                if min_val > life_exp:
                    min_val = life_exp
                    lowest['country'] = country
                    lowest['code'] = code
                    lowest['year'] = year
                    lowest['life'] = life_exp
                elif max_val < life_exp:
                    max_val = life_exp
                    highest['country'] = country
                    highest['code'] = code
                    highest['year'] = year
                    highest['life'] = life_exp
                
                if year_input == year:
                    year_life_total += life_exp
                    year_life_expentancy_values.append(life_exp)                
                    if y_min_val > life_exp:
                        y_min_val = life_exp
                        year_lowest['country'] = country
                        year_lowest['code'] = code
                        year_lowest['year'] = year
                        year_lowest['life'] = life_exp
                    elif y_max_val < life_exp:
                        y_max_val = life_exp
                        year_highest['country'] = country
                        year_highest['code'] = code
                        year_highest['year'] = year
                        year_highest['life'] = life_exp

    year_life_avg = year_life_total / len(year_life_expentancy_values)

    print(f'\n-- Life Expectancies Spanish Flu --\n'
        f'\nThe overall min life expectancy is: {highest[life_str]} from {highest[country_str]} in {highest[year_str]}\n'
        f'The overall max life expectancy is: {lowest[life_str]} from {lowest[country_str]} in {lowest[year_str]}\n'
        '\n'
        f'For the year {year_input}:\n'
        f'The average life expectancy across all countries was {year_life_avg:.2f}\n'
        f'The max life expectancy was in {year_highest[country_str]} with {year_highest[life_str]}\n'
        f'The min life expectancy was in {year_lowest[country_str]} with {year_lowest[life_str]}\n')

if __name__ == '__main__':
    year_input = input("\nEnter the year of interest: ")
    mapReducer(year_input)
