from pyspark.ml import PipelineModel
import re
import nltk
from kafka import KafkaConsumer
from json import loads
from pymongo import MongoClient
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

client = MongoClient('localhost', 27017)
db = client['bda_project'] 
collection = db['tweets'] 

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

spark = SparkSession.builder \
    .appName("classify tweets") \
    .getOrCreate()

pipeline = PipelineModel.load("logistic_regression_model.pkl")

def clean_text(text):
    if text is not None:
        text = re.sub(r'https?://\S+|www\.\S+|\.com\S+|youtu\.be/\S+', '', text)
        
        text = re.sub(r'(@|#)\w+', '', text)
        
        text = text.lower()
        
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    else:
        return ''
    
class_index_mapping = { 0: "Negative", 1: "Positive", 2: "Neutral", 3: "Irrelevant" }

consumer = KafkaConsumer(
    'numtest',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    tweet = message.value[-1] 
    preprocessed_tweet = clean_text(tweet)
    reprocessed_tweet)
   
    data = [(preprocessed_tweet,),]  
    data = spark.createDataFrame(data, ["Text"])
    processed_validation = pipeline.transform(data)
    prediction = processed_validation.collect()[0][6]

    print("-> Tweet:", tweet)
    print("-> preprocessed_tweet : ", preprocessed_tweet)
    print("-> Predicted Sentiment:", prediction)
    print("-> Predicted Sentiment classname:", class_index_mapping[int(prediction)])
    
    tweet_doc = {
        "tweet": tweet,
        "prediction": class_index_mapping[int(prediction)]
    }


    collection.insert_one(tweet_doc)

    print("/"*50)