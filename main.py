import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import sqlite3
import matplotlib.pyplot as plt
import matplotlib
import os

matplotlib.style.use('ggplot')


con = sqlite3.connect("E:\\DLL\\FromC\\reddit-comments-may-2015\\database.sqlite")
data = pd.read_sql_query("SELECT * from May2015 LIMIT 200000", con)
##print data.describe()

data['length'] = data['body'].str.len()
user_activities = data.groupby(by=['author'])['length'].sum()
user_activities2 = data.groupby(by=['author']).size()


plt.figure(1)
plt.xlim(0, 2000)
##plt.ylim(0, 150000)
user_activities.hist(bins=20, range=(0,2000))
plt.title("user activities")
plt.xlabel("number of letters each user typed")
plt.ylabel("Frequency")
plt.savefig('most_types.png')


plt.figure(2)
plt.xlim(0, 20)
user_activities2.hist(bins=20, range=(0,20))
plt.title("user activities")
plt.xlabel("number of post for each user")
plt.ylabel("Frequency")
plt.savefig('most_active.png')

plt.show()

