
country = ''
code = ''
year = ''
life_exp = 0

country_str = 'country'
code_str = 'code'
year_str = 'year'
life_str = 'life'

def displayMenu():
    option = input("--- QUERY MENU ---\n"
        "1. Year\n"
        "2. Country\n"
        "3. Quit\n"
        "------------\n"
        "Insert the number of the option you choose: ")
    return option

def displayData():

    all_data = open('./life-expectancy.csv')
    
    max_val = 0                     # Starts with lowest value
    min_val = 1000                  # Starts with highest value
    lowest = {}
    highest = {}

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
    
    print(f'The overall min life expectancy is: {highest[life_str]} from {highest[country_str]} ({highest[code_str]}) in {highest[year_str]}\n'
        f'The overall max life expectancy is: {lowest[life_str]} from {lowest[country_str]} ({lowest[code_str]}) in {lowest[year_str]}\n')
    

def yearQuery(year_input):

    all_data = open('./life-expectancy.csv')

    year_life_total = 0
    year_life_avg = 0
    year_life_expentancy_values = []
    y_max_val = 0                   # Starts with lowest value
    y_min_val = 1000                # Starts with highest value
    year_lowest = {}
    year_highest = {}
        
    first_data = True
    for data in all_data:
        if first_data:
            first_data = False
        else:
            country, code, year, life_exp = data.split(',')
            life_exp = float(life_exp)

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

    print(f'\n-- For the year {year_input}:\n'
        f'The average life expectancy across all countries was {year_life_avg:.2f}\n'
        f'The max life expectancy was in {year_highest[country_str]} ({year_highest[code_str]}) with {year_highest[life_str]}\n'
        f'The min life expectancy was in {year_lowest[country_str]} ({year_lowest[code_str]}) with {year_lowest[life_str]}\n')
    input('Press enter to continue...')

def countryQuery(country_input):

    all_data = open('./life-expectancy.csv') 

    country_life_total = 0
    country_life_avg = 0
    country_life_expentancy_values = []
    c_max_val = 0                   # Starts with lowest value
    c_min_val = 1000                # Starts with highest value
    country_lowest = {}
    country_highest = {}
    
    first_data = True
    for data in all_data:
        if first_data:
            first_data = False
        else:
            country, code, year, life_exp = data.split(',')
            life_exp = float(life_exp)

            if country_input == country:
                country_life_total += life_exp
                country_life_expentancy_values.append(life_exp)     
                if c_min_val > life_exp:
                    c_min_val = life_exp
                    country_lowest['country'] = country
                    country_lowest['code'] = code
                    country_lowest['year'] = year
                    country_lowest['life'] = life_exp
                elif c_max_val < life_exp:
                    c_max_val = life_exp
                    country_highest['country'] = country
                    country_highest['code'] = code
                    country_highest['year'] = year
                    country_highest['life'] = life_exp
    
    country_life_avg = country_life_total / len(country_life_expentancy_values)

    print(f'\n-- For {country_input} ({country_highest[code_str]}):\n'
        f'The average life expectancy in {country_input} over the years was {country_life_avg:.2f}\n'
        f'The max life expectancy was in {country_highest[year_str]} with {country_highest[life_str]}\n'
        f'The min life expectancy was in {country_lowest[year_str]} with {country_lowest[life_str]}\n')
    input('Press enter to continue...')

if __name__ == '__main__':

    print("\n-- Life Expectancies Spanish Flu Over Years --\n")
    
    displayData()

    while True:
        option = displayMenu()

        if option == '1':
            year_input = input("Enter the year of interest: ")
            yearQuery(year_input)
        elif option == '2':
            country_input = input("Enter the country of interest: ")
            countryQuery(country_input.capitalize())
        elif option == '3':
            break
        else:
            print(f'No option assigned to: {option}')

