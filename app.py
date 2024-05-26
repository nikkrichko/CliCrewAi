import click
import os
from dotenv import load_dotenv
load_dotenv()
import dotenv
from helper.llm_helper import LLMHelper

from groups.tech_manager.product_owner import SoftDevGroup
from groups.text_helper.text_handler import TextGroup
from groups.murdle.puzzle_handler import PuzzleGroup


@click.group()
@click.option('-ai', '--aimodel', type=str, help='put the model name', default="None")
@click.pass_context
def cli(ctx, aimodel):
    ctx.ensure_object(dict)
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if aimodel == "None":
        aimodel = os.environ.get("OPENAI_MODEL_NAME")
    LLM_model = LLMHelper(model_name=aimodel, openai_api_key=openai_api_key)
    ctx.obj['LLM_model'] = LLM_model.get_llm_model()
    pass

cli.add_command(SoftDevGroup)
cli.add_command(TextGroup)
cli.add_command(PuzzleGroup)

if __name__ == "__main__":
    cli(obj={})