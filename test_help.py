lowest = 100.00
highest = 1.00
lowest_country = ''
highest_country = ''
highest_year = ''
lowest_year = ''
year_average = float()
user_average_lower = 100
user_average_higher = 0
user_country_lower = ''
user_country_higher = ''

user_entry = input('Year of Interest:  ')

with open('life-expectancy.csv') as life_expectancy_file:
    
    headers = next(life_expectancy_file)
    
    for line in life_expectancy_file:

        line = line.strip()

        parts = line.split(",")

        names = parts[0]
        abreviations = parts[1]
        years = parts[2]
        average = float(parts[3])

        if average > highest:
            highest = average
            highest_country = names
            highest_year = years
        
        if average < lowest:
            lowest = average
            lowest_country = names
            lowest_year = names


        if user_entry != '0':

            while years == user_entry:

                year_average = sum(average) / len(average)

                if average > user_average_higher:
                    user_average_higher = average
                    user_country_higher = names
        
                if average < user_average_lower:
                    user_average_lower = average
                    user_country_lower = names
            
    print(f"The overall lowest Life Expectancy:{lowest_year} in {lowest_country}, {lowest}")
    print(f"The overall highest Life Expectancy:{highest_year}in {highest_country}, {highest}")

    print()

    print(f'For the year {user_entry}:')
    print(f"The overall life expectancy across all countries is: {year_average:.2f}")
    print(f'The lowest life expectancy was in {user_country_lower} at {user_average_lower} years')
    print(f'The highest life expectancy was in {user_country_higher} at {user_average_higher} years.')