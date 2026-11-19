import pandas as pd
import pyarrow


#NYC Taxi Trips

file = "/Users/kamari/Documents/project_info/yellow_tripdata_2026-APRIL.parquet"

data = pd.read_parquet(file)


df = pd.DataFrame(data)

#print(df.head())

print(df.columns)



class TaxiPipeline:

    def __init__(self, spark, input_path, output_path):
        self.spark = spark
        self.input_path = input_path
        self.output_path = output_path

    def extract(self):
        pass

    def transform(self, df):
        pass

    def load(self, df):
        pass

    def run(self):
        pass