import pandas as pd 
from pandas_profiling import ProfileReport
df = pd.read_csv('poke.csv')
print(df)

#Generate the report
profile = ProfileReport(df)
profile.to_file("poke.html")