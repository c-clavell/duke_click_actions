

from locale import strcoll
from sys import intern
from tkinter import N
import click



def addx(number):
    d=0
    d=d
    return number+2

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your firstname", help="The person to greet.", type=str)
@click.option("--age", prompt="Your age", help="age int.",type=int)
def hello1(count, name, age):
    """Simple program that greets NAME for a total of COUNT times."""
    addx(age)
    x=2
    for _ in range(count):
        click.echo(f"Hello, {name}  age={age}!")


@click.command()
@click.argument('str1', type=str)
@click.argument('int1', type=int)
@click.argument('float1', type=float)
@click.option("--verb", "-ve")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello2(str1, int1, float1, verb, name):
    if verb:
        click.echo("hello:", verb)
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f'str1 = {str1}')
    click.echo(f"int1 float= {int1} {float1}")
    click.echo(name)



if __name__ == '__main__':
    hello1()

    #hello2()

    
