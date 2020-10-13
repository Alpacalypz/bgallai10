import random, csv

def jobGetter(dict):
    x=random.uniform(0,float(dict["Total"]))
    for key, value in dict.items():
        x=x-float(value)
        if x<=0:
            return key
    return "Invalid"

if __name__ == "__main__":
    JobClass = {}
    with open("occupations.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            JobClass[row[0]] = row[1]
    JobClass.pop("Job Class")
    print(jobGetter(JobClass))
