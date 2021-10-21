import plotly.express as px
import csv
with open ("TV.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Size of TV", y="Average Time Spent")
    fig.show()