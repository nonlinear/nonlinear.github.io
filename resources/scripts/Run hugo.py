import sys
import os
import subprocess
import time
import webbrowser

def start_hugo():
    # Inicia o hugo serve -D em background, redirecionando saída
    proc = subprocess.Popen(
        ["hugo", "serve", "-D"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return proc

def wait_for_server(url, timeout=15):
    try:
        import requests
    except ImportError:
        print("O pacote 'requests' não está instalado. Instale com 'pip install requests'.")
        return False
    for _ in range(timeout):
        try:
            requests.get(url)
            return True
        except Exception:
            time.sleep(1)
    return False

def get_url_from_file(file_path):
    if not file_path:
        return "http://localhost:1313"
    filename = os.path.basename(file_path)
    # Remove extensão .md se existir
    if filename.endswith(".md"):
        filename = filename[:-3] + ".html"
    return f"http://localhost:1313/{filename}"

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else None
    url = get_url_from_file(file_path)

    # Inicia o hugo
    hugo_proc = start_hugo()
    print("Aguardando Hugo iniciar...")

    # Aguarda o servidor responder
    if wait_for_server("http://localhost:1313"):
        print(f"Abrindo {url}")
        webbrowser.open(url)
    else:
        print("Hugo não iniciou a tempo.")

    # O servidor Hugo continua rodando em background
