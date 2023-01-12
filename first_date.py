# I am going to clean some Excel data

import pandas as pd

csv_file = "transactional-sample.csv"
sheet1 = pd.read_csv(csv_file)
print(sheet1.columns)