from make_question_google_gemini_api.MakeQuestionGoogleGeminiApi import MakeQuestionGoogleGeminiApi
from make_question_google_gemini_api.Config import Config
import os

mqgga = MakeQuestionGoogleGeminiApi()
mqgga.make_question("Which is the Bangladesh capital?")
answer = mqgga.get_results()
print(answer)
