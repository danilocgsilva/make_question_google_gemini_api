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
        
    def get_implementation_alias(self) -> str:
        return "MakeQuestionGoogleGeminiApi"

    def make_question(self, question: str) -> str:
        self._question = question

    def get_answer_text_raw(self) -> str:
        self._validate_before_make_question()
        results = self.get_results()
        return results.response_content
    
    def get_results(self) -> Results:
        self._validate_before_make_question()
        initial_unix_timestamp_with_ms = time.time()
        llm = ChatGoogleGenerativeAI(
            model=self._default_model,
            temperature=self._default_temperature,
            google_api_key=self._config["api_key"]
        )
        raw_response = llm.invoke(self._question)
        final_unix_timestamp_with_ms = time.time()
        
        return Results(
            raw_answer=raw_response,
            timestamp_start=initial_unix_timestamp_with_ms,
            timestamp_end=final_unix_timestamp_with_ms,
            implementation_name=self.get_implementation_alias(),
            model_name=self._default_model,
            parameters={},
            response_content=raw_response.content,
            raw_answer_dict=self.response_to_dict(raw_response)
        )
        
    def response_to_dict(self, raw_response) -> dict:
        return {
            "content": raw_response.content,
            "additional_kwargs": raw_response.additional_kwargs,
            "response_metadata": raw_response.response_metadata,
            "id": raw_response.id,
            "usage_metadata": raw_response.usage_metadata
        }
    
    def _validate_before_make_question(self):
        if self._question is None:
            raise QuestionNotMadeException("Question has not been made yet.")
