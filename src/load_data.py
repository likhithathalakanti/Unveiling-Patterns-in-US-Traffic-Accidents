import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Load data
def load_data(file_path):
    spark = SparkSession.builder.appName("USAccidentsAnalysis").getOrCreate()
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    return df
