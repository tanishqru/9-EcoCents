import eel
import pandas as pd

@eel.expose
def dataf():
    df = pd.read_excel("book.xlsx")
    c = list(df["company_name"]) 
    p = list(df["project_name"])
    d = {"company":c, "project":p}
    with open("cp.csv", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(d.keys())
        for row in zip(*d.values()):
            csv_writer.writerow(row)

eel.start("index.html")