from make_question_interface.IMakeQuestion import IMakeQuestion
from make_question_interface.Exceptions.QuestionNotMadeException import QuestionNotMadeException
from make_question_google_gemini_api.Config import Config

class MakeQuestionGoogleGeminiApi(IMakeQuestion):
    def __init__(self, config: Config):
        self._config = config
        self._answer_text_raw = None

    def make_question(self, question: str) -> str:
        self._answer_text_raw = "This is the answer"

    def get_answer_text_raw(self) -> str:
        if self._answer_text_raw is None:
            raise QuestionNotMadeException("Question has not been made yet.")
        return self._answer_text_raw
