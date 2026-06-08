import pandas as pd 
import os 

data = {
    'Name' : ['Dhruv','Dax','Prit','Meet','Krish'],
    'Age' : [21,20,22,18,26],
    'City' : ['Surat','Bharuch','Ahembdabad','Baroda','Dang']
}

df = pd.DataFrame(data)
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
file_path  = os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)
print(f"file is saved at {file_path}")

