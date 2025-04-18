from EmotionDetection import emotion_detector
import json
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        test_string = "I am glad this happened"
        e = emotion_detector(test_string)
        edic = json.loads(e)
        #print(edic)
        #print(edic['dominant_emotion']) 
        self.assertEqual(edic['dominant_emotion'],'joy')

    def test_anger(self):
        test_string = "I am really mad about this"
        e = emotion_detector(test_string)
        edic = json.loads(e)
        #print(edic)
        #print(edic['dominant_emotion']) 
        self.assertEqual(edic['dominant_emotion'],'anger')

    def test_disgust(self):
        test_string = "I feel disgusted just hearing about this"
        e = emotion_detector(test_string)
        edic = json.loads(e)
        #print(edic)
        #print(edic['dominant_emotion']) 
        self.assertEqual(edic['dominant_emotion'],'disgust')

    def test_sadness(self):
        test_string = "I am so sad about this"
        e = emotion_detector(test_string)
        edic = json.loads(e)
        #print(edic)
        #print(edic['dominant_emotion']) 
        self.assertEqual(edic['dominant_emotion'],'sadness')
        
    def test_fear(self):
        test_string = "I am really afraid that this will happen"
        e = emotion_detector(test_string)
        edic = json.loads(e)
        #print(edic)
        #print(edic['dominant_emotion']) 
        self.assertEqual(edic['dominant_emotion'],'fear')

if __name__ == '__main__':
    unittest.main()

     
