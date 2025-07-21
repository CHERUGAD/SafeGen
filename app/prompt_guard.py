# app/prompt_guard.py

from sentence_transformers import SentenceTransformer
import joblib 

class PromptGuard:
    def __init__(self):
        self.encoder = SentenceTransformer("models/encoder")
        self.classifier = joblib.load("models/classifier/safety_classifier.pkl")
        self.banned_keywords = [
            "bomb", "blast", "explosive", "kill", "murder", "suicide", "hack", "terrorist",
            "assassinate", "poison", "weapon", "gun", "drugs", "nuke", "hostage", ""
        ]

    def contains_banned_keywords(self, prompt: str) -> bool:
        lowered = prompt.lower()
        return any(bad_word in lowered for bad_word in self.banned_keywords)

    def check_prompt(self, prompt: str) -> str:
        if self.contains_banned_keywords(prompt):
            return "restricted"
        embedding = self.encoder.encode([prompt], convert_to_numpy=True)
        prediction = self.classifier.predict(embedding)[0]
        return "safe" if prediction == 1 else "restricted"
