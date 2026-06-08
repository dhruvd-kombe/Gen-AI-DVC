import pandas as pd 
import os 

data = {
    'Name' : ['Dhruv','Dax','Prit','Meet','Krish'],
    'Age' : [21,20,22,18,26],
    'City' : ['Surat','Bharuch','Ahembdabad','Baroda','Dang']
}

df = pd.DataFrame(data)

new_row = {'Name' : 'Sakshi' , 'Age' : 20 , 'City' : 'Surat'}
df.loc[len(df.index)] = new_row

new_row1 = {'Name' : 'Sakshi1' , 'Age' : 30 , 'City' : 'Tapi'}
df.loc[len(df.index)] = new_row1
new_row2 = {'Name' : 'Sakshi2' , 'Age' : 40 , 'City' : 'Vapi'}
df.loc[len(df.index)] = new_row2

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
file_path  = os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)
print(f"file is saved at {file_path}")

