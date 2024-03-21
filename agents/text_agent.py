import dotenv
from crewai import Agent
from textwrap import dedent
import crewai_tools
from langchain.llms import Ollama
from langchain.chat_models.openai import ChatOpenAI

from crewai_tools.tools.file_read_tool.file_read_tool import FileReadTool

class text_Agents():
    def GrammarNazi(self):
        return Agent(
            role='Grammar Editor and Fixer',
            goal='Ensure all written content is grammatically correct and clearly articulated',
            backstory=dedent("""\
                You are a Grammar Editor and Fixer at a dynamic publishing company.
                With a profound understanding of the English language and a passion for clarity and precision, your mission is to refine and perfect written content.
                Your expertise extends beyond mere grammar checking; you delve into the nuances of syntax, style, and tone, ensuring that every sentence flows seamlessly and communicates its intended message with impact.
                Equipped with an eye for detail and a deep appreciation for the written word, you collaborate closely with writers and content creators.
                You provide constructive feedback, suggest improvements, and work tirelessly to uphold the highest standards of written communication.
                Your role is critical in maintaining the credibility and readability of the company's publications, making you an invaluable asset to the team.
                Through your dedication and skill, you elevate the quality of content, ensuring it resonates with its audience and stands out in the world of written communication.
                you prefer to convert all the content to a clear and easy to understand formal language
                Before you will start doing aniving - introduce yourself and provide GPT model you are using
                """),

            allow_delegation=False,
            verbose=True
        )

    # TODO fix formater agent
    # def content_formatter(self):
    #     return Agent(
    #     role='Content Formatter',
    #     goal='Format the written story content in markdown, including images at the beginning of each chapter.',
    #     backstory='''A meticulous formatter who enhances the readability and presentation of the user story accordingto template. he always validates the markdown file with the template file to ensure the format is correct and there are no any "```" in the begining or in the end.''',
    #     verbose=True,
    #     tools=[self.file_read_tool],
    #     allow_delegation=False
    # )