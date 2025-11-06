""" (3) Create a base class, CDataProcessor with two properties- samples and features- and
 a method PrintDatasetInfo(). The two properties are initialized using the number of
 rows and columns of a Pandas dataframe that is passed to the constructor during object
 creation. The PrintDatasetInfo() method should print the number of samples and
 features.
 Derive a new class, CCSVProcessor from the CDataProcessor class. This derived
 class should have two properties- filename and dfData- The filename is initialized
 to path of the CSV file specified during object creation. The dfData is initialized to
 empty dataframe. The CCSVProcessor class should contain two methods- LoadData()
 and ConvertToJSON()- LoadData should load the CSV data into a dfData property of
 this class (use Pandas read csv method). It should also invoke its parent class __init__
method passing the dfData, so that, parent’s samples and features are populated cor
rectly. ConvertToJSON() should create a new JSON file using the dfData (use Pandas
 to json method)
 Derive a new class, CJSONProcessor from the CDataProcessor class. This derived
 class should have two properties- filename and dfData- The filename is initialized
 to path of the JSON file specified during object createion. The dfData is initialized to
 empty dataframe. The CJSONProcessor class should contain a method- LoadData()
LoadData should load the JSON data into a dfData property of this class (use Pandas
 read json method). It should also invoke its parent class __init__ method passing the
 dfData, so that, parent’s samples and features are populated correctly.
 a. Create an instance object of CCSVProcessor using the file titanic.csv. Load the
 data and invoke PrintDatasetInfo() to print the number of samples and features
 in this dataset.
 b. Createanobject of CCSVProcessor using the file ODI-Batting_Cricket_Analytics.csv.
 This file is copied in my Google drive code folder. Load the data and invoke
 ConvertToJSON() method to create a new ODI-Batting_Cricket_Analytics.JSON file.
 c. Createanobject of CJSONProcessor(), load the data and invoke PrintDatasetInfo()
 to print the number of features and columns of this dataset"""
import pandas as pd
class CDataProcessor:
    def __init__(self,df):
        self.samples=df.shape[0]
        self.features=df.shape[1]

    def printdatasetinfo(self):
        print("Samples: ",self.samples)
        print("Features: ",self.features)

class CCSVProcessor(CDataProcessor):
    def __init__(self,filename):
        self.filename=filename
        self.dfdata=pd.DataFrame()

    def LoadData(self):
        self.dfdata=pd.read_csv(self.filename)
        super().__init__(self.dfdata)
        print("csv data loaded")

    def ConvertToJSON(self,newfile_name):
        self.dfdata.to_json(newfile_name)
        print(f"File converted to JSON: {newfile_name}")


class CJSONProcessor(CDataProcessor):
    def __init__(self,filename):
        self.filename=filename
        self.dfdata=pd.DataFrame()

    def LoadData(self):
        self.dfdata=pd.read_json(self.filename)
        super().__init__(self.dfdata)
        print("JSON File loaded")

instance1=CCSVProcessor("titanic.csv")
instance1.LoadData()
instance1.printdatasetinfo()

instance2=CCSVProcessor("ODI_Cricket_Analytics.csv")
instance2.LoadData()
instance2.ConvertToJSON("ODI_Cricket_Analytics.json")
print(instance2)

output=CJSONProcessor("ODI_Cricket_Analytics.json")
output.LoadData()
output.printdatasetinfo()