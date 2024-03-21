import dotenv
from crewai import Agent
from textwrap import dedent
import crewai_tools
from langchain.llms import Ollama
from langchain.chat_models.openai import ChatOpenAI

from crewai_tools.tools.file_read_tool.file_read_tool import FileReadTool

class general_agents():
    def profSynapse(self):
        return Agent(
            role='Knowledgeable conductor of expert agents with',
            goal='Ensure that agent works properly and provide the best possible output',
            backstory=dedent("""\
                        Your job is to assist me in accomplishing my goals by first aligning with my needs, then summoning an expert agent perfectly suited to the task by uttering the incantation
                        """),

            allow_delegation=False,
            verbose=True
        )