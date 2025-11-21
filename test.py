from make_question_google_gemini_api.MakeQuestionGoogleGeminiApi import MakeQuestionGoogleGeminiApi
from make_question_google_gemini_api.Config import Config

config = Config()
mqgga = MakeQuestionGoogleGeminiApi(config)
mqgga.make_question("This is my question")
answer = mqgga.get_answer_text_raw()
print(answer)