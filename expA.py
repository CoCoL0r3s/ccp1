import csv

with open("python-portfolio-project-starter-files/insurance.csv") as insurance_file:
    fields = ["age", "sex", "bmi", "children", "smoker", "region", "charges"]
    data_reader = csv.DictReader(insurance_file, fields)
    print(list(data_reader))