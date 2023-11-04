import eel


eel.init("")


@eel.expose
def dataf():
    import csv
    import pandas as pd
    df = pd.read_excel("book.xlsx")
    c = list(df["company_name"]) 
    p = list(df["project_name"])
    d = {"company":c, "project":p}
    with open("cp.csv", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(d.keys())
        for row in zip(*d.values()):
            csv_writer.writerow(row)

def uniquerefergen():
    import csv
    import pandas as pd
    df = pd.read_excel("user.xlsx")
    referal_id = list(df["refer_id"])
    return referal_id
eel.start("index.html")