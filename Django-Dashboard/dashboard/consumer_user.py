from pyspark.ml import PipelineModel
from pyspark.sql import SparkSession
import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')

spark = SparkSession.builder \
    .appName("classify tweets") \
    .getOrCreate()


pipeline = PipelineModel.load("logistic_regression_model.pkl")

def clean_text(text):
    if text is not None:
        text = re.sub(r'https?://\S+|www\.\S+|S+\.com\S+|youtu\.be/\S+', '', text)
        
        text = re.sub(r'(@|#)\w+', '', text)
        
        text = text.lower()
        
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    else:
        return ''
    
class_index_mapping = { 0: "Negative", 1: "Positive", 2: "Neutral", 3: "Irrelevant" }


def classify_text(text: str) :
    preprocessed_tweet = clean_text(text)
    data = [(preprocessed_tweet,),]  
    data = spark.createDataFrame(data, ["Text"])
    processed_validation = pipeline.transform(data)
    prediction = processed_validation.collect()[0][6]

    print("-> Tweet : ", text)
    print("-> preprocessed_tweet : ", preprocessed_tweet)
    print("-> Predicted Sentiment : ", prediction)
    print("-> Predicted Sentiment classname : ", class_index_mapping[int(prediction)])

    print("/"*50)

    return class_index_mapping[int(prediction)]