#%% Running Pandas and numpy
import pandas as pd
import numpy as np
one_d_array= np.random.rand(3)
my_first_series = pd.Series(one_d_array)
my_first_series
two_d_array = np.random.rand(3,2)
my_first_dataframe = pd.DataFrame(two_d_array)
my_first_dataframe
#%% Arry Demos of numpy and pandas
print(one_d_array)

array_arrange = np.arange(10,30,2)
array_arrange

pd.Series(array_arrange).dtype
# array_arrange.reshape(3,4)
# ValueError: cannot reshape array of size 10 into shape (3,4)
pd.DataFrame(array_arrange.reshape(2,5))
np.ones((3,3),dtype=np.str)
np.zeros((3,3),dtype = np.float_)
#%% Test for detreminant for a matrix
test_array = np.array([[6,1,1],[4,-2,5],[2,8,7]])
np.linalg.det(test_array)
#%% changing index of a series
test_array = np.array([12345,234,1234])
series = pd.Series(test_array,index=['First','second','Third'])
series[0]
series["First"]
series["second"]
#%% Data Frame Demo
test_array = np.array([[6,1,1],[4,-2,5],[2,8,7]])
df = pd.DataFrame(test_array)
type(df[0])
type(df)
#%% Reading CSV Data from panda
import os
_PATH = os.path.join('.',
'python',
'MyFirstFlaskApi',
'Data Analysis',
'Data')
CSV_PATH = os.path.join(str(_PATH),'artwork_data.csv')
CSV_PATH
os.path.abspath(os.path.curdir)
if os.path.exists(CSV_PATH):
    print('path Exists')
else:
    print("Path DOesNot Exist!")
usr_cols = ['id','artist','title','medium',
'year','acquisitionYear',
'height','width','units']

df = pd.read_csv(CSV_PATH,
index_col='id',usecols = usr_cols)
#Save Dataframe to pickel
df.to_pickle(os.path.join(str(_PATH),'data_frame.pickle'))

#%% dataframes from a json file
#Sample to make dataframe from a set of tuples
import json
data = [('Monday','working')
,('sunday','Non-working')]

df = pd.DataFrame.from_records(data,columns=
["days","IsWorking"])
df

columns_to_use = ['id','all_artists','title','medium',
'acquisitionYear',
'height','width','units']
# End of Sample
def get_records_from_file(file_path,user_cols):
    with open(file_path) as artwork_file:
        content = json.load(artwork_file)
        record=[]
        for field in user_cols:
            record.append(content[field])
    return tuple(record)
Path = os.path.join(_PATH,"artworks",
"a","000","a00001-1035.json")

sample_record = get_records_from_file(Path,
columns_to_use)
sample_record
df_fromjson = pd.DataFrame.from_records([sample_record]
,columns=columns_to_use)
df_fromjson

#%% To get all the records from the json
all_records = []
Path = os.path.join(_PATH,"artworks")
for root,dirs,jsonfiles in os.walk(Path):
   for _jsonfile in (file for file in jsonfiles if file.endswith('json')):
        record = get_records_from_file(os.path.join(root,_jsonfile),columns_to_use)
        all_records.append(record)
        break
print(all_records)
df_from_alljson  = pd.DataFrame.from_records(all_records,index='id',columns=columns_to_use)
df_from_alljson
_pickle_json_save_path = os.path.join(_PATH,'data_frame_json.pickle')
df_from_alljson.to_pickle(_pickle_json_save_path)
#%%Reading data from data pickle
pickel_csv_save_path = os.path.join(_PATH,'data_frame.pickle')
df = pd.read_pickle(pickel_csv_save_path)

#df.artist Not a recommeneded way of getting data

artists = df['artist']
unique_artists = pd.unique(artists)
len(unique_artists)
df
#One way
s= df['artist'].value_counts()
s['Bacon, Francis']

#another way
value_francis_bacon = df['artist']=='Bacon, Francis'
value_francis_bacon.value_counts()
#%%usage of iloc and loc
#Demo loc 1
df.loc[1035,'artist']
#demo iloc1
df.iloc[0,0]
#demo iloc2
df.iloc[0:2,0:2].iloc[0:1,0:1]
#demo iloc3
df.iloc[0,:]


#%% usage of width and height to find the maximum area in dataset

#int(df['height']) * int(df['width'])
# df['height'].sort_values().head()

pd.to_numeric(df['width'],errors='coerce').sort_values().tail()


#%%
