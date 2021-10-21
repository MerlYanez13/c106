import plotly.express as px
import csv
import numpy as np

def getDataSource(path):
    marks=[]
    days=[]
    with open (path) as f:
        df=csv.DictReader(f)
        for row in df:
            marks.append(float(row["Marks In Percentage"]))
            days.append (float(row["Days Present"]))
        #fig=px.scatter(df,y="Marks In Percentage", x="Days Present")
        #fig.show()
    return {"x":marks,"y":days}

def findCorrelation(ds):
    correlation=np.corrcoef(ds["x"],ds["y"])
    print("correlation= ",correlation[0,1])

dataPath="Marks.csv"
ds=getDataSource(dataPath)
findCorrelation(ds)