# load csv modul
import csv

# import csv into list of dicts
import_list = []
with open("python-portfolio-project-starter-files/insurance.csv") as insurance_file:
    fields = ["age", "sex", "bmi", "children", "smoker", "region", "charges"]
    data_reader = csv.DictReader(insurance_file, fields)
    for row in data_reader:
        import_list.append(row)
