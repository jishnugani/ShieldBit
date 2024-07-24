import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
import joblib

df = pd.read_csv('phishingemail.csv')

df = df.dropna()

train_data, test_data, train_labels, test_labels = train_test_split(df['Email Text'], df['Email Type'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer(stop_words='english', token_pattern=r'\b\w\w+\b') 


model = make_pipeline(vectorizer, RandomForestClassifier(n_estimators=100)) 
model.fit(train_data, train_labels)

joblib.dump(model, 'model.joblib')


predictions = model.predict(test_data)

accuracy = accuracy_score(test_labels, predictions)
print(f'Accuracy: {accuracy}\n')

classification_rep = classification_report(test_labels, predictions)
print(f'Classification Report:\n{classification_rep}')

new_email = ["Congratulations! You've won a free vacation. Click the link to claim your prize."]
new_prediction = model.predict(new_email)
print(f'New Email Prediction: {new_prediction}')
