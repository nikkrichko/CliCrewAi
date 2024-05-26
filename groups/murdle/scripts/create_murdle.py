from agents.text_agent import text_Agents
from crewai import Crew
from tasks.puzzle_task import PuzzleTask
from tasks.text_tasks import FixGrammarTasks
from agents.text_agent import text_Agents
from crewai_tools.tools.file_read_tool.file_read_tool import FileReadTool
import os
class CreateMurdlePuzzle:
    def __init__(self, llm_model, input_file, ):
        self.llm_model = llm_model
        self.input_file = input_file
        # validate temp folder exsist if not create it
        dir_name = "temp"
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        self.initial_json = "temp/MURDLE_initial.json"
        self.clues_json = "temp/MURDLE_clues.json"

    def _create_murdle_puzzle(self, input_text):

        # file_read_tool = FileReadTool(
        #     file_path='Murdle_template.md',
        #     description='A tool to read the Murdle Template file and understand the expected output format.'
        # )

        puzzle_tasks = PuzzleTask()
        gr_tasks = FixGrammarTasks()
        text_agents = text_Agents()

        # Create Agents
        grammatical_agent = text_agents.GrammarNazi()
        puzzle_agent = text_agents.PuzzleCreator()
        # markdown_formater = text_agents.MarkdownFormatter(file_read_tool)

        # Create Tasks


        fix_grammar = gr_tasks.fix_grammar_task(grammatical_agent, input_text)
        # TODO make date and story dependant outPut file
        create_murrdle_json = puzzle_tasks.create_initial_murdle_json_task(puzzle_agent, input_text, self.initial_json)
        create_clues = puzzle_tasks.create_clues_task(puzzle_agent, self.clues_json)

        # Create Crew responsible for Copy
        crew = Crew(
            agents=[
                # grammatical_agent,
                puzzle_agent
            ],
            tasks=[
                # fix_grammar,
                create_murrdle_json,
                create_clues

            ],
            verbose=True,
            manager_llm=self.llm_model

        )

        result_story = crew.kickoff()

        return result_story

    def run(self):
        with open(self.input_file, 'r') as file:
            input_text = file.read()

        murdle_puzzle = self._create_murdle_puzzle(input_text)
        # print(user_story)

        # with open(self.output_file, 'w') as file:
        #     file.write(murdle_puzzle)

        return murdle_puzzle

    def save_markdown(self):
        from groups.murdle.scripts.markdown_generator import MarkdownGenerator

        # json_file_name = "40_MURDLE_clues.json"
        with open(self.clues_json, 'r') as f:
            json_string = f.read().replace('`', '').replace('json', '')

        mg = MarkdownGenerator()

        md_string = mg.convert_to_markdown(json_string)
        # save it to file
        output_md_file = "temp/"+ mg.get_title_string(json_string) + ".md"
        print(f">>>> \n>>>> Murdle Puzzle saved to {output_md_file}")
        with open(output_md_file, 'w') as f:
            f.write(md_string)