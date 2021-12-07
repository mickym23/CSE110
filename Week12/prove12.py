import operator
with open("life-expectancy.csv") as full_sheet:

   data = []
   next(full_sheet)

   for line in full_sheet:
      info = line.split(",")
      country = {
         "entity": info[0],
         "code": info[1],
         "year": info[2],
         "life_exp": info[3].strip()
      }
      data.append(country)

   # Create sorted array copy (based on life_exp) and grab the highest and lowest life expectancies
   max_life_list = data.copy()
   sorted_dic = sorted(max_life_list, key=operator.itemgetter("life_exp"), reverse=True)

   # Highest value
   highest = sorted_dic[0]

   # Lowest value
   lowest = sorted_dic[len(max_life_list) - 1]

   print()

   print(f'The overall max life expectancy is: {highest["life_exp"]} from {highest["entity"]} in {highest["year"]}')
   print(f'The overall min life expectancy is: {lowest["life_exp"]} from {lowest["entity"]} in {lowest["year"]}')

   print()

   while True:
      area_of_interest = int(input('Enter year (1) or country (2) of interest: '))

      if (area_of_interest == 1):
         country_year_input = int(input('Enter the year of interest: '))
         print()
            
         # Add to array for specific year
         filtered_by_year = []

         for value in data:
            year = value["year"]
            if int(year) == country_year_input:
               filtered_by_year.append(value)
            
         # Add all years and determine average
         total_years = 0
         for value in filtered_by_year:
            total_years += float(value["life_exp"])
         average = total_years / len(filtered_by_year)

         # Create sorted array copy (based on life_exp) and grab the highest and lowest life expectancies
         filtered_max_life_list = filtered_by_year.copy()
         filtered_sorted_dic = sorted(filtered_max_life_list, key=operator.itemgetter("life_exp"), reverse=True)

         # Highest value
         filtered_highest = filtered_sorted_dic[0]

         # Lowest value
         filtered_lowest = filtered_sorted_dic[len(filtered_max_life_list) - 1]


         print(f'\nFor the year {country_year_input}:')
         print(f'The average life expectancy across all countries was {round(average, 2)}')
         print(f'The max life expectancy in {filtered_highest["entity"]} with {filtered_highest["life_exp"]}')
         print(f'The min life expectancy in {filtered_lowest["entity"]} with {filtered_lowest["life_exp"]}')
         break

      # Country
      if (area_of_interest == 2):

         country_input = input('Enter the country of interest: ')
         
         # Add to array for specific country
         filtered_by_country = []
         for value in data:
            country = value["entity"]
            if country_input == country:
               filtered_by_country.append(value)
            
         # Add all years and determine average
         total_years = 0
         for value in filtered_by_country:
            total_years += float(value["life_exp"])
         average = total_years / len(filtered_by_country)

         # Create sorted array copy (based on life_exp) and grab the highest and lowest life expectancies
         filtered_max_life_list = filtered_by_country.copy()
         filtered_sorted_dic = sorted(filtered_max_life_list, key=operator.itemgetter("life_exp"), reverse=True)

         # Highest value
         filtered_highest = filtered_sorted_dic[0]

         # Lowest value
         filtered_lowest = filtered_sorted_dic[len(filtered_max_life_list) - 1]


         print(f'\nFor the country, {country_input}:')
         print(f'The average life expectancy across in {country_input} was {round(average, 2)}')
         print(f'The max life expectancy in {filtered_highest["entity"]} was {filtered_highest["life_exp"]} in {filtered_highest["year"]}')
         print(f'The min life expectancy in {filtered_lowest["entity"]} was {filtered_lowest["life_exp"]} in {filtered_lowest["year"]}')
         break
   
      print('Invalid input, please try again!')


