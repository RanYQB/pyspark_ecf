from flask import Flask

## import findspark 
## findspark.init()

## import pyspark 
## from pyspark.sql import SparkSession

## from flask import Flask, jsonify, redirect, url_for , render_template

## spark = SparkSession.builder \
   ## .appName("GoldenLine Pyspark") \
   ## .config("") \
   ## .config("") \
   ##  .config("spark.ui.enable", "true") \
   ## .getOrCreate()

app = Flask(__name__)

## @app.route('/data')
## def pyspark_app():
   ## data = [("Hello",)]
   ## df = spark.createDataFrame(data, ["message"])
   ## df.show()
   ## json_data = df.toJSON().collect()
   ## return jsonify(json_data)


@app.route('/')
def index():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)

