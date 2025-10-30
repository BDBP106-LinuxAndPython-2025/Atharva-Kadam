"""(8) Read in the file diabetes.csv, and after obtaining the pandas dataframe, do the following:
(i) Print all the column names"""
import pandas as pd
a=pd.read_csv("diabetes.csv")
print("The columns of the csv file are:",a.columns)


"""(ii) Print the first 10 rows"""
b=pd.read_csv("diabetes.csv")
print("The first 10 rows are:",b.head(10))



"""(iii) Print the mean of the BloodPressure column values"""
c=pd.read_csv("diabetes.csv")
print("The mean of the BloodPressure values are: ",c["BloodPressure"].mean())



"""(iv) Print the first 4 rows of columns 3,4,5"""
d=pd.read_csv("diabetes.csv")
print("The first 4 rows of columns 3,4,5 are: \n",d.iloc[:4,3:6])



"""(v) Add another column ’NormalizedBP’ using (max-min) normalization to the dataframe
as: BP[i] -min(BP) / (max(BP) - min(BP))."""
e=pd.read_csv("diabetes.csv")
e["NormalizedBP"]=(e["BloodPressure"] - e["BloodPressure"].min())/(e["BloodPressure"].max() - e["BloodPressure"].min())
print("NormalizedBP:\n",e[["BloodPressure","NormalizedBP"]].head(6))



"""(vi) Write a function categorize_age(age) that returns ”Youth”, ”Adult” or ”Se-
nior” based on the age brackets (1-18, 19-50, ¿50). Create a new column in the
dataframe with this function called age category."""
def categorize_age(age):
    if age<=18:
        return "Youth"
    if 19 <=age <=50:
        return "Adult"
    else:
        return "Senior"

f=pd.read_csv("diabetes.csv")
f["Age Category"]=f["Age"].apply(categorize_age)
print(f[["Age","Age Category"]])

