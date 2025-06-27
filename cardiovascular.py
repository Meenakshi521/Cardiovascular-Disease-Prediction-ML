import pickle as pk
import pandas as pd 

cardio_model=pk.load(open('cardiovascular_Model-2.pkl','rb'))
gc_encoder=pk.load(open('glucose and  cholesterol encoder-2.pkl','rb'))

Age=input("enter your age:")
Gender=input("enter your gender:")
Smoke=input("enter your smoke:")
Physical_activity=input("enter your physical activity:")
Alcohol_intake=input("enter your alcohol intake:")
Cholesterol=input("enter your cholesterol:")
Glucose=input("enter your glucose:")


columns=['age', 'gender', 'smoke', 'physical activity','alcohol intake','cholesterol','glucose']
row=[[Age,Gender,Smoke,Physical_activity,Alcohol_intake,Cholesterol,Glucose]]
data=pd.DataFrame(row,columns=columns)

data_arr=gc_encoder.transform(data[['glucose','cholesterol']]).toarray()
temp_data=pd.DataFrame(data_arr,columns=['above normal G', 'normal G', 'well above normal G','above normal C', 'normal C', 'well above normal C'],dtype='int')

data['gender'] = data['gender'].map({'male':0,'female':1})
data['smoke'] = data['smoke'].map({'yes':1,'no':0})
data['alcohol intake'] = data['alcohol intake'].map({'yes':1,'no':0})
data['physical activity'] = data['physical activity'].map({'yes':1,'no':0})


data.drop(['cholesterol','glucose'],axis=1,inplace=True)
data=pd.concat([data,temp_data],axis=1)

cardio_predicted=cardio_model.predict(data)
print("THE PREDICTED CARDIO VALUE IS :",cardio_predicted)