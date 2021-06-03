# data sampling

import random
import plotly.express as px
import plotly.figure_factory as ff 
import pandas as pd
import csv
import statistics
import plotly.graph_objects as go

df = pd.read_csv("hw14.csv")
claps = df["claps"].tolist()

pop_mean = statistics.mean(claps)
print("Population Mean: " + str(pop_mean))

mean_list=[]
for x in range (1,100):
    dataset=[]

    for y in range(1,30):
        rand = random.randint(0,len(claps)-1)
        value = claps[rand]
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    mean_list.append(mean)

sample_mean = statistics.mean(mean_list)
print("Sample Mean: " + str(sample_mean))

graph = ff.create_distplot([mean_list],["sample data"],show_hist=False)
graph.show()





