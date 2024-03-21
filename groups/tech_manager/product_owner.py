

from groups.tech_manager.scripts.create_user_story import CreateUserStory
import click

@click.group()
def SoftDevGroup():
    pass

@SoftDevGroup.command()
@click.option('-i', '--input_file', type=click.Path(exists=True), help='Input file path')
@click.option('-o', '--output_file', type=click.Path(), help='Output file path')
@click.pass_context
def uscreate(ctx, input_file, output_file):
    LLM_model = ctx.obj.get('LLM_model')

    click.echo(f'Start working on Creating user story for {input_file}\n\n')

    create_story = CreateUserStory(LLM_model, input_file, output_file)
    create_story.run()

    click.echo(f'\n\nOutput result is saved to {output_file}')