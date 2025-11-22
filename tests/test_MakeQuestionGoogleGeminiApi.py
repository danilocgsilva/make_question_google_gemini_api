from make_question_interface.Exceptions.QuestionNotMadeException import QuestionNotMadeException
import unittest
from make_question_google_gemini_api.MakeQuestionGoogleGeminiApi import MakeQuestionGoogleGeminiApi
from make_question_google_gemini_api.Config import Config

class test_MakeQuestionGoogleGeminiApi(unittest.TestCase):
    def setUp(self):
        self.make_question_instance = MakeQuestionGoogleGeminiApi(Config(api_key='dummy_key'))
    
    def test_get_answer_without_making_question(self):
        with self.assertRaises(QuestionNotMadeException) as context:
            self.make_question_instance.get_answer_text_raw()
        self.assertTrue('Question has not been made yet.' in str(context.exception))
        
    def test_get_results_without_making_question(self):
        with self.assertRaises(QuestionNotMadeException) as context:
            self.make_question_instance.get_results()
        self.assertTrue('Question has not been made yet.' in str(context.exception))