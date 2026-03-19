import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion(self):
        result = emotion_detector("I am happy")
        self.assertIn("joy", result)

if __name__ == "__main__":
    unittest.main()