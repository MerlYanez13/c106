import plotly.express as px
import csv
import numpy as np

def getDataSource(path):
    Coffee=[]
    Sleep=[]
    with open (path) as f:
        df=csv.DictReader(f)
        for row in df:
            Coffee.append(float(row["Coffee in ml"]))
            Sleep.append (float(row["sleep in hours"]))
        #fig=px.scatter(df,y="Coffee In Percentage", x="Sleep Present")
        #fig.show()
    return {"x":Coffee,"y":Sleep}

def findCorrelation(ds):
    correlation=np.corrcoef(ds["x"],ds["y"])
    print("correlation= ",correlation[0,1])

dataPath="Coffee.csv"
ds=getDataSource(dataPath)
findCorrelation(ds)