
import os
import json


class MarkdownGenerator:
    def __init__(self):
        pass
        # self.json_file = json_file
        # # validate loders exist of output file exist if not create them
        # dir_name = os.path.dirname(output_file)
        #
        # # If directory does not exist, create it
        # if not os.path.exists(dir_name):
        #     os.makedirs(dir_name)
        # self.output_file = output_file

    def _get_table_title_string(self, input_dict):
        return "| " + " | ".join(input_dict.keys()) + " |"

    def _get_table_string_desription(self, input_dict, field_name):
        res_strint = "| " + ' | '.join([value.get(field_name) for value in input_dict.values()]) + " |\n"
        return res_strint

    def _get_table_string_attributes(self, input_dict, field_name):
        res_strint = "| " + ' | '.join([", ".join(value.get(field_name)) for value in input_dict.values()]) + " |\n"
        return res_strint

    def _get_solution_table(self, input_dict, markdown_output):
        markdown_output.append("## Solution\n\n")
        killer = [suspect for suspect, swl in input_dict['SWL'].items() if swl['is_killer']][0]
        killer_data = input_dict['SWL'][killer]
        markdown_output.append(f"| {killer} |  {killer_data['weapon']} | {killer_data['location']} | killer |\n")
        markdown_output.append("| -- | -- | -- | -- |\n")
        for suspect, swl in input_dict['SWL'].items():
            if suspect != killer:
                markdown_output.append(
                    f"| {suspect} |  {swl['weapon']} | {swl['location']} | {'killer' if swl['is_killer'] else ''} |\n")

    def _get_clue_table(self, data, markdown_output):
        len_col = len(data['Suspects']) + len(data['Locations']) + 1
        cols = list(data['Suspects'].keys()) + list(data['Locations'].keys())
        rows = list(data['Weapons'].keys()) + list(data['Locations'].keys())
        table_col_row_title = "| | " + " | ".join(cols) + " |"
        table_col_row_string = "\n" + "| -- " * len_col + "|\n"
        for row in rows:
            table_col_row_string += f"| {row} | " + " | " * (len_col - 1) + "\n"
        markdown_output.append(table_col_row_title)
        markdown_output.append(table_col_row_string)

    def _get_table_with_title(self, input_dict, markdown_output, title: str = None):
        markdown_output.append(f"## {title.upper()}.\n\n")

        suspect_table_title = self._get_table_title_string(input_dict[title])
        markdown_output.append(suspect_table_title + "\n")
        markdown_output.append("| ---------  " * len(input_dict[title]) + "|\n")
        suspect_description = self._get_table_string_desription(input_dict[title], 'description')
        suspect_attrributes = self._get_table_string_attributes(input_dict[title], 'attributes')
        markdown_output.append(suspect_description)
        markdown_output.append(suspect_attrributes)
        markdown_output.append("\n\n")

    def get_title_string(self, json_str):
        data = json.loads(json_str)
        return data['Scenario']['name'].replace(" ", "_")

    def convert_to_markdown(self, json_str):

        data = json.loads(json_str)

        markdown_output = []

        # Murdle title
        markdown_output.append(f"# {data['Scenario']['name']}\n")

        # Scenario description
        markdown_output.append(f"{data['Scenario']['Description']}\n\n")

        self._get_table_with_title(data, markdown_output, 'Suspects')
        self._get_table_with_title(data, markdown_output, 'Weapons')
        self._get_table_with_title(data, markdown_output, 'Locations')

        markdown_output.append("\n\n---\n\n## CLUES\n")
        for i, clue in enumerate(data['clues'], 1):
            markdown_output.append(f"{clue}\n")

        markdown_output.append("\n\nMURDLE CLUE TABLE\n\n")

        self._get_clue_table(data, markdown_output)

        markdown_output.append("\n\n---\n\n")

        self._get_solution_table(data, markdown_output)

        return ''.join(markdown_output)