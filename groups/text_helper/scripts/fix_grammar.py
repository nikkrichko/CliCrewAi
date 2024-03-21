
from tasks.text_tasks import FixGrammarTasks
from agents.text_agent import text_Agents
from crewai import Crew

class FixGrammar:
    def __init__(self, llm_model, input_file, output_file):
        self.llm_model = llm_model
        self.input_file = input_file

        self.output_file = output_file

    def _fix_grammar(self, text):

        tasks = FixGrammarTasks()
        agents = text_Agents()

        # Create Agents
        grammatical_agent = agents.GrammarNazi()

        # Create Tasks
        fix_grammar = tasks.fix_grammar_task(grammatical_agent, text)

        # Create Crew responsible for Copy
        crew = Crew(
            agents=[
                grammatical_agent
            ],
            tasks=[
                fix_grammar
            ],
            verbose=True,
            manager_llm=self.llm_model

        )

        fixed_text = crew.kickoff()

        return fixed_text

    def run(self):
        with open(self.input_file, 'r') as file:
            input_text = file.read()

        fixed_text = self._fix_grammar(input_text)
        print(fixed_text)

        with open(self.output_file, 'w') as file:
            file.write(fixed_text)

        return fixed_text
