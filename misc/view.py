import requests
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm
from concurrent.futures import ThreadPoolExecutor, as_completed

console = Console()
TOOL_API_URL = "https://buf-view-tiktok-ayacte.vercel.app/tiktokview"

def show_banner():
    banner_text = Text("""
""", style="bold magenta")

    info_text = Text()
    info_text.append("📌 TOOL: ", style="bold cyan")
    info_text.append("BUFF VIEW TIKTOK\n", style="bold yellow")
    info_text.append("📦 VERSION: 1.0.5\n", style="bold green")

    console.print(Panel(banner_text, title="🎯 HTT TOOL", border_style="bright_blue"))
    console.print(Panel(info_text, border_style="cyan", title="🧠 Thong Tin"))

def buff_view(tiktok_url, loop_num=None):
    try:
        response = requests.get(TOOL_API_URL, params={'video': tiktok_url}, timeout=60)

        if response.status_code != 200:
            console.print(f"❌ [red]Loi HTTP {response.status_code} tu API[/red]")
            return

        data = response.json()
        result_panel = Panel.fit(
            f"""🔁 Lan: {loop_num if loop_num else 1}
🔗 Link: [bold cyan]{tiktok_url}[/bold cyan]
📹 Video ID: [bold magenta]{data.get('video_id', 'N/A')}[/bold magenta]
✅ Thanh cong: [green]{data.get('sent_success', 0)}[/green]
❌ That bai: [red]{data.get('sent_fail', 0)}[/red]
🕒 Xu ly: [italic yellow]{round(data.get('time_used', 0), 2)} giay[/italic yellow]
🧰 Proxy: [italic]{data.get('proxy_used', 'Khong ro')}[/italic]
⏱️ View se tang dan sau vai phut...
""",
            title=f"🎉 KET QUA [{loop_num if loop_num else 1}]", border_style="bright_magenta"
        )
        console.print(result_panel)

    except requests.exceptions.Timeout:
        console.print("[bold yellow]⏳ Tool processing is taking longer than expected. Views can still increase after a few minutes.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]⚠️ Loi khi goi API: {e}[/bold red]")

def auto_loop_multi(links: list, delay_sec: int, max_workers=5):
    console.print(Panel(f"[bold yellow]🔁 TREO TOOL ĐANG CHAY VOI {len(links)} LINK (Đa luong)[/bold yellow]\n"
                        f"⏱️ delay per iteration: {delay_sec} giay\n"
                        f"🧵 maximum quantity: {max_workers}\n"
                        f"❌ ented [red]Ctrl + C[/red] STOP", title="⚙️ AUTO MULTI-THREAD MODE", border_style="bright_green"))

    loop = 1
    try:
        while True:
            console.print(f"\n[bold blue]🔄 Vong lap #{loop}[/bold blue]")

            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                futures = {executor.submit(buff_view, link, loop): link for link in links}
                for future in as_completed(futures):
                    try:
                        future.result()
                    except Exception as e:
                        console.print(f"[red]⚠️ Error during tool execution: {e}[/red]")

            loop += 1
            time.sleep(delay_sec)
    except KeyboardInterrupt:
        console.print("\n[bold red]🛑 stop on request.[/bold red]")

def load_links_input():
    links = []
    while True:
        link = Prompt.ask("🔗 Link URL (Press Enter to finish)")
        if not link.strip():
            break
        if link.startswith("http"):
            links.append(link.strip())
        else:
            console.print("❌ [red]Invalid link, must start with. http[/red]")
    return links

def load_links_from_file(file_path):
    links = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                clean_link = line.strip()
                if clean_link.startswith("http"):
                    links.append(clean_link)
    except Exception as e:
        console.print(f"[red]⚠️ Cannot read the file: {e}[/red]")
    return links

def main():
    show_banner()

    if Confirm.ask("📁 Load the list of urls from a .txt file?", default=False):
        file_path = Prompt.ask("📄 Enter the file path (one link per line)", default="links.txt")
        links = load_links_from_file(file_path)
    else:
        links = load_links_input()

    if not links:
        console.print("[red]❌ No valid link to hang.[/red]")
        return

    delay = Prompt.ask("⏱️ Enter the delay time between each loop (seconds)", default="60")
    try:
        delay_sec = int(delay)
    except:
        console.print("[red]❌ Invalid delay. Using default 60 seconds.[/red]")
        delay_sec = 60

    workers = Prompt.ask("🧵 Enter the number of concurrent processing threads", default="5")
    try:
        max_workers = int(workers)
    except:
        console.print("[red]❌ Invalid quantity. Using default 5.[/red]")
        max_workers = 5

    auto_loop_multi(links, delay_sec, max_workers)

if __name__ == "__main__":
    main()
