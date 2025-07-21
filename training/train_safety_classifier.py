# training/train_safety_classifier.py

from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
import joblib
import numpy as np
import os

# Example training data
X_text = ["this is safe", "this is harmful", "harmless message", "offensive words"]
y = [1, 0, 1, 0]  # 1 = safe, 0 = unsafe

# Load sentence transformer and encode
encoder = SentenceTransformer("all-MiniLM-L6-v2")
X_embeddings = encoder.encode(X_text, convert_to_numpy=True)

# Train classifier on embeddings
clf = LogisticRegression()
clf.fit(X_embeddings, y)

# Save classifier
os.makedirs("models/classifier", exist_ok=True)
joblib.dump(clf, "models/classifier/safety_classifier.pkl")

# Save encoder for reuse in PromptGuard
os.makedirs("models/encoder", exist_ok=True)
encoder.save("models/encoder")

print("Classifier and encoder saved.")
