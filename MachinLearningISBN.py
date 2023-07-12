from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
import numpy as np
import sqlite3

connection = sqlite3.connect(r"C:\Users\Josh\COUNTER-5-Report-Tool\all_data\search\search.db")
cursor = connection.cursor()

cursor.execute("SELECT title, most_probable_major FROM TR WHERE most_probable_major is not NULL")
# Training data
#print(cursor.fetchmany(1000))
training_data = cursor.fetchmany(2000)  # Fetch all rows returned by the query
# Preparing the data for training
X_train = [data[0] for data in training_data]
y_train = [data[1] for data in training_data]

# Creating a pipeline for text classification
vectorizer = TfidfVectorizer()
classifier = SVC(kernel='linear')

pipeline = make_pipeline(vectorizer, classifier)

# Training the text classifier
pipeline.fit(X_train, y_train)

# Function to predict the related option for a given string
def predict_related_option(title):
    predicted_option = pipeline.predict([title])
    return predicted_option[0]

# Example usage
def UpdateRows():
    batch_size = 999

    count = 0
    # cursor.execute("Select Title from TR where most_probable_major = 'Unorganized'")
   #while  ((len(cursor.fetchall()))>1):
    while True:
        cursor.execute("Select Title from TR where most_probable_major is NULL or most_probable_major = 'Unsorted' ")

        count+=1
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break

        for row in rows:

            title = row[0]
            predictedTitle = predict_related_option(title)
            print(title)
            print(predictedTitle)
            update_query = r'UPDATE TR SET most_probable_major = "' + predictedTitle.replace('"', '""') + '" WHERE title = "' + title.replace('"', '""').replace("'", "'") + '"'
            print(update_query)
            cursor.execute(update_query)

        connection.commit()

        break
        #cursor.execute("Select Title from TR where most_probable_major = 'Unorganized'")

UpdateRows()