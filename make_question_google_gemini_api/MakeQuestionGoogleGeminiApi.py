from make_question_interface.IMakeQuestion import IMakeQuestion
from make_question_interface.Exceptions.QuestionNotMadeException import QuestionNotMadeException
from make_question_google_gemini_api.Config import Config
from typing import Optional
from make_question_interface.Results import Results
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import time

class MakeQuestionGoogleGeminiApi(IMakeQuestion):
    def __init__(self, config: Optional[Config] = None):
        if config:
            self._config = config
        else:
            api_key = os.environ.get('GOOGLE_API_KEY')
            config: Config = {
                "api_key": api_key
            }
            self._config = config
        self._answer_text_raw = None
        self._question = None
        self._default_model = "models/gemini-2.5-flash"
        self._default_temperature = 0.1

    def make_question(self, question: str) -> str:
        self._question = question

    def get_answer_text_raw(self) -> str:
        self._validate_before_make_question()
        self.get_results()
        return self._answer_text_raw
    
    def get_results(self) -> Results:
        self._validate_before_make_question()
        initial_unix_timestamp_with_ms = time.time()
        llm = ChatGoogleGenerativeAI(
            model=self._default_model,
            temperature=self._default_temperature,
            google_api_key=self._config["api_key"]
        )
        response = llm.invoke(self._question)
        final_unix_timestamp_with_ms = time.time()
        
        print(response)
        
        results = Results(
            self._answer_text_raw,
            initial_unix_timestamp_with_ms,
            final_unix_timestamp_with_ms,
            "MakeQuestionGoogleGeminiApi",
            self._default_model
        )
        return results
    
    def _validate_before_make_question(self):
        if self._question is None:
            raise QuestionNotMadeException("Question has not been made yet.")
