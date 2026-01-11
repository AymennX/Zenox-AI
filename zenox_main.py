import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.markdown import Markdown
from rich.prompt import Prompt

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

console = Console()
THEME_COLOR = "cyan"
USER_COLOR = "green"

def print_zenox_logo():
    logo = """
    ███████╗███████╗███╗   ██╗ ██████╗ ██╗  ██╗
    ╚══███╔╝██╔════╝████╗  ██║██╔═══██╗╚██╗██╔╝
      ███╔╝ █████╗  ██╔██╗ ██║██║   ██║ ╚███╔╝ 
     ███╔╝  ██╔══╝  ██║╚██╗██║██║   ██║ ██╔██╗ 
    ███████╗███████╗██║ ╚████║╚██████╔╝██╔╝ ██╗
    ╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
    """
    console.clear()
    console.print(f"[bold {THEME_COLOR}]{logo}[/bold {THEME_COLOR}]", justify="center")
    console.print(f"[bold white on {THEME_COLOR}]   Made By AymennX | Zenox V1.0   [/bold white on {THEME_COLOR}]", justify="center")
    console.print("\n")

def typewriter_effect(text):
    for char in text:
        console.print(f"[dim cyan]{char}[/dim cyan]", end="")
        time.sleep(0.01)
    print()

def stream_ai_response(response_stream):
    full_text = ""
    with Live(console=console, refresh_per_second=12) as live:
        for chunk in response_stream:
            try:
                if chunk.text:
                    full_text += chunk.text
                    panel = Panel(
                        Markdown(full_text),
                        title=f"[bold {THEME_COLOR}]ZENOX AI[/bold {THEME_COLOR}]",
                        border_style=THEME_COLOR,
                        subtitle="[dim]Zenox can do mistakes & Powered by Gemini[/dim]"
                    )
                    live.update(panel)
            except Exception:
                continue
    console.print()

def get_working_model():
    """Finds the best available model for your specific API key."""
    # Preferred order: 3.0 -> 2.5 -> 1.5-flash-latest
    preferred = ['gemini-3-flash-preview', 'gemini-2.5-flash', 'gemini-1.5-flash-latest']
    
    try:
        available = [m.name.split('/')[-1] for m in genai.list_models() 
                     if 'generateContent' in m.supported_generation_methods]
        
        for model in preferred:
            if model in available:
                return model
        return available[0] if available else None
    except Exception:
        return 'gemini-2.5-flash' # Default fallback

def main():
    print_zenox_logo()

    if not API_KEY:
        console.print(Panel("[bold red]ERROR: .env file or GEMINI_API_KEY missing.[/bold red]", border_style="red"))
        return

    typewriter_effect(">> INITIALIZING ZENOX PROTOCOLS")
    
    try:
        genai.configure(api_key=API_KEY)
        model_id = get_working_model()
        model = genai.GenerativeModel(model_id)
        chat = model.start_chat(history=[])
        typewriter_effect(f">> AI MODEL LOADED: {model_id.upper()}")
    except Exception as e:
        console.print(f"[bold red]Critical System Failure: {e}[/bold red]")
        return

    while True:
        try:
            user_input = Prompt.ask(f"[bold {USER_COLOR}]YOU[/bold {USER_COLOR}]")
            
            if user_input.lower() in ["exit", "quit", "shutdown"]:
                console.print(f"[bold {THEME_COLOR}]ZENOX Shutting Down...[/bold {THEME_COLOR}]")
                break

            with console.status(f"[bold {THEME_COLOR}]ZENOX Thinking...[/bold {THEME_COLOR}]", spinner="bouncingBar"):
                response = chat.send_message(user_input, stream=True)
            
            stream_ai_response(response)

        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[bold red]Interface Error: {e}[/bold red]")

if __name__ == "__main__":
    main()
