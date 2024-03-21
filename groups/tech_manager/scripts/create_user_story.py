from agents.text_agent import text_Agents
from crewai import Crew
from tasks.software_development_tasks import SoftwareDevTasks
from tasks.text_tasks import FixGrammarTasks
from agents.software_managment import SoftwareManagmentAgents


class CreateUserStory:
    def __init__(self, llm_model, input_file, output_file):
        self.llm_model = llm_model
        self.input_file = input_file
        self.output_file = output_file

    def _create_user_story(self, input_text):
        tasks = SoftwareDevTasks()
        gr_tasks = FixGrammarTasks()
        agents = SoftwareManagmentAgents()

        # Create Agents
        grammatical_agent = text_Agents().GrammarNazi()
        product_owner_agent = agents.productOwner()
        # scrum_master_agent = agents.scrumMaster()
        # content_formatter = agents.content_formatter()

        # Create Tasks
        fix_grammar = gr_tasks.fix_grammar_task(grammatical_agent, input_text)
        create_user_story = tasks.create_user_story(product_owner_agent)
        # format_content = tasks.task_format_content(content_formatter, create_user_story)

        # Create Crew responsible for Copy
        crew = Crew(
            agents=[
                grammatical_agent,
                product_owner_agent
            ],
            tasks=[
                fix_grammar,
                create_user_story
            ],
            verbose=True,
            manager_llm=self.llm_model

        )

        result_story = crew.kickoff()

        return result_story

    def run(self):
        with open(self.input_file, 'r') as file:
            input_text = file.read()

        user_story = self._create_user_story(input_text)
        # print(user_story)

        with open(self.output_file, 'w') as file:
            file.write(user_story)

        return user_story