import eel
import pandas as pd

@eel.export
def dataf():
    df = pd.read_excel("book.xlsx")
    c = list(df["company_name"]) 
    p = list(df["project_name"])
    d = {"company":c, "project":p}
    with open("cp.csv", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(data.keys())
        for row in zip(*data.values()):
            csv_writer.writerow(row)