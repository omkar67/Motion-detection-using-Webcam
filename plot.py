from bokeh.models import Tooltip
from test import df
import pandas as pd 
from bokeh.plotting import figure,output_file,show
from bokeh.models import HoverTool,ColumnDataSource

df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])
df["start_string"]=df["Start"].dt.strftime("%Y-%m-%D %H-%M-%S ")#converting date time to strings
df["end_string"]=df["End"].dt.strftime("%Y-%m-%D %H-%M-%S ")##converting date time to strings

cds=ColumnDataSource(df)


p=figure(width=1280,height=720,x_axis_type="datetime",title="Motion Detection")

hover=HoverTool(tooltips=[("Start","@start_string"),("End","@end_string")])
p.add_tools(hover)

p.yaxis.minor_tick_line_color=None
p.ygrid[0]
p.quad(left='Start',right="End",top=1,bottom=0,color="#9BD3DD",source=cds)

output_file=("Graph.html")
show(p)
