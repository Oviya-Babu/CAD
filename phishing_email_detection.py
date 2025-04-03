import pandas as pd
import numpy as np
import joblib
import os

from imblearn.over_sampling import RandomOverSampler

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import LabelEncoder



file_path = "Phishing_Email.csv"
data = pd.read_csv(file_path)



data = data.dropna()



label_encoder = LabelEncoder()
data["Email Type"] = label_encoder.fit_transform(data["Email Type"])



X_texts = data["Email Text"].tolist()  
y_labels = data["Email Type"].values



oversampler = RandomOverSampler(random_state=42)
X_resampled, y_resampled = oversampler.fit_resample(
    np.array(X_texts, dtype=object).reshape(-1, 1), y_labels
)
X_resampled = X_resampled.ravel().tolist()  



X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.4, random_state=42
)



phishing_detector = Pipeline([
    ("vectorizer", TfidfVectorizer(stop_words='english', max_features=10000, ngram_range=(1, 2))),
    ("classifier", RandomForestClassifier(n_estimators=200, random_state=42))
])



phishing_detector.fit(X_train, y_train)



model_filename = os.path.join(os.getcwd(), "phishing_email_model.pkl")
joblib.dump(phishing_detector, model_filename)


print("Model training complete. Saved as:", model_filename)
