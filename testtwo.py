import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 400, 90]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 