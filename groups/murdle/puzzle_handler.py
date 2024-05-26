
from groups.murdle.scripts.create_murdle import CreateMurdlePuzzle
import click

@click.group()
def PuzzleGroup():
    pass



# @click.option('-o', '--output_file', type=click.Path(), help='Output file path')
@PuzzleGroup.command()
@click.option('-i', '--input_file', type=click.Path(exists=True), help='Input file path')
#add true false parameter - save to file or not
@click.option('-s', '--save', type=bool, help='Save to file or not', default=True)
@click.pass_context
def createMurdle(ctx, input_file,save):
    LLM_model = ctx.obj.get('LLM_model')
    # click.echo(f'fixgrammar from TextGroup. Prompt: {prompt}')
    # click.echo(f'Start working on fixing grammar for {input_file}')

    murdle_creator = CreateMurdlePuzzle(LLM_model, input_file)
    murdle_creator.run()
    # if save:
    #     murdle_creator.save_markdown()

