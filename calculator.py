import math
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

def power(x, y):
    return x ** y
def square_root(x):
    return math.sqrt(x)
def modulo(x, y):
    return x % y
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! dividing using zero"
    return x / y

def cleanedoutput(result):
    if isinstance(result, float):
        if result.is_integer():
            return int(result)
        else:
            return round(result, 3)
    return result

history = []

while True:
    console.print(Panel.fit("📊 [bold blue]Select Operation[/bold blue]", style="bold white on black"))
    console.print("1. Addition")
    console.print("2. Subtraction")
    console.print("3. Multiplication")
    console.print("4. Division")
    console.print("5. Show history")
    console.print("6. Scientific Mode")
    console.print("Q. Quit")

    choice = Prompt.ask("[bold green]Enter your choice (1-6 or Q to Quit)[/bold green]")

    if choice == '5':
        if not history:
            console.print("[italic yellow]No history yet[/italic yellow]")
        else:
            console.print("\n📜 [bold cyan]Calculation History:[/bold cyan]")
            for i, item in enumerate(history, 1):
                console.print(f"[bold]{i}.[/bold] {item}")
        continue

    if choice == '6':
        console.print(Panel.fit("🔬 [bold magenta]Scientific Operations[/bold magenta]", style="bold white on black"))
        console.print("a. Power (x ^ y)")
        console.print("b. Square Root (√x)")
        console.print("c. Modulo (x % y)")
        sci_choice = Prompt.ask("[bold green]Enter your choice (a/b/c)[/bold green]")

        try:
            if sci_choice == 'a':
                base = float(Prompt.ask("Enter the base"))
                exponent = float(Prompt.ask("Enter the exponent"))
                result = cleanedoutput(power(base, exponent))
                console.print("[bold cyan]Result:[/bold cyan]", result)
                history.append(f"{base} ^ {exponent} = {result}")
            elif sci_choice == 'b':
                num = float(Prompt.ask("Enter the number"))
                result = cleanedoutput(square_root(num))
                console.print("[bold cyan]Result:[/bold cyan]", result)
                history.append(f"√{num} = {result}")
            elif sci_choice == 'c':
                x = float(Prompt.ask("Enter first number"))
                y = float(Prompt.ask("Enter second number"))
                if y == 0:
                    console.print("[red]Error! Cannot divide by zero in modulo.[/red]")
                    continue
                result = cleanedoutput(modulo(x, y))
                console.print("[bold cyan]Result:[/bold cyan]", result)
                history.append(f"{x} % {y} = {result}")
            else:
                console.print("[red]Invalid scientific choice.[/red]")
        except ValueError:
            console.print("[red]Please enter valid numbers.[/red]")
        continue

    if choice.upper() == "Q":
        console.print("[bold yellow]Thanks for using the calculator![/bold yellow] 👋")
        break

    if choice not in ['1', '2', '3', '4', '5', '6']:
        console.print("[red]Invalid choice! Try again.[/red]")
        continue

    try:
        num1 = float(Prompt.ask("Enter your first number"))
        num2 = float(Prompt.ask("Enter your second number"))
    except ValueError:
        console.print("[red]Please enter valid numbers.[/red]")
        continue

    if choice == '1':
        result = cleanedoutput(add(num1, num2))
        console.print("[bold cyan]Result:[/bold cyan]", result)
        history.append(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = cleanedoutput(subtract(num1, num2))
        console.print("[bold cyan]Result:[/bold cyan]", result)
        history.append(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = cleanedoutput(multiply(num1, num2))
        console.print("[bold cyan]Result:[/bold cyan]", result)
        history.append(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = cleanedoutput(divide(num1, num2))
        console.print("[bold cyan]Result:[/bold cyan]", result)
        history.append(f"{num1} / {num2} = {result}")
