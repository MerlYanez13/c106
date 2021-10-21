import plotly.express as px
import csv
with open ("Icecream.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,y="Ice-cream Sales", x="Temperature")
    fig.show()