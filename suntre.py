from rich.console import Console

console = Console()

def cprint(text: str, color: str):
    """Prints text in a specific color."""
    console.print(text, style=f"bold {color}")

cprint(f'\n>>> stake LP | {address_wallet} | {error}', 'red')
