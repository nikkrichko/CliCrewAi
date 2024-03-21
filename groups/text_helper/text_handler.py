

from groups.text_helper.scripts.fix_grammar import FixGrammar
import click

@click.group()
def TextGroup():
    pass

@TextGroup.command()
@click.option('-i', '--input_file', type=click.Path(exists=True), help='Input file path')
@click.option('-o', '--output_file', type=click.Path(), help='Output file path')
@click.pass_context
def fixgrammar(ctx, input_file, output_file):
    LLM_model = ctx.obj.get('LLM_model')
    # click.echo(f'fixgrammar from TextGroup. Prompt: {prompt}')
    click.echo(f'Start working on fixing grammar for {input_file}')

    grammar_fixer = FixGrammar(LLM_model, input_file, output_file)
    grammar_fixer.run()
    
    click.echo(f'output result is saved to {output_file}')