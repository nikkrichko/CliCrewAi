from langchain.chat_models.openai import ChatOpenAI

class LLMHelper():
    def __init__(self, model_name, openai_api_key):
        self.model_name = model_name
        self.openai_api_key = openai_api_key
        self.llm_model =ChatOpenAI(
        model=self.model_name,
        openai_api_key=self.openai_api_key
        )
        pass

    def get_llm_model(self):
        return self.llm_model