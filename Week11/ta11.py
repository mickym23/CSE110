with open("hr_system.txt") as hr_sys:

   people_in_company = [] 

   for line in hr_sys:
      data = line.split(" ")
      person = {
         "name": data[0],
         "id": data[1],
         "job_title": data[2],
         "salary": data[3]
      }
      people_in_company.append(person)



   for person in people_in_company:
      print(f'{person["name"]} (ID: {person["id"]}), {person["job_title"]} - ${person["salary"]}')



