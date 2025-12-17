
# NOVA VERSÃO: SSH, progresso, atualização da própria lista
import os
import re
from pathlib import Path
from dotenv import load_dotenv
import paramiko
from tqdm import tqdm

load_dotenv()
REMOTE_HOST = os.getenv("REMOTE_HOST")
REMOTE_USER = os.getenv("REMOTE_USER")
REMOTE_PATH = os.getenv("REMOTE_PATH", "/serve/media/comics")
SSH_KEY = os.getenv("SSH_KEY")  # opcional

LISTA_PATH = Path(__file__).parent / "missing_comics.md"

def extract_numbers(files):
    numbers = set()
    for f in files:
        match = re.search(r"(\d+)", f)
        if match:
            numbers.add(int(match.group(1)))
    return numbers

def get_remote_listing():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(REMOTE_HOST, username=REMOTE_USER, key_filename=SSH_KEY if SSH_KEY else None)
    sftp = ssh.open_sftp()
    try:
        folders = sftp.listdir(REMOTE_PATH)
        remote_dict = {}
        for folder in tqdm(folders, desc="Lendo pastas remotas"):
            folder_path = f"{REMOTE_PATH}/{folder}"
            try:
                files = sftp.listdir(folder_path)
                remote_dict[folder] = extract_numbers(files)
            except Exception:
                continue
        return remote_dict
    finally:
        sftp.close()
        ssh.close()

def get_missing_list():
    if not LISTA_PATH.exists():
        return {}
    missing = {}
    with open(LISTA_PATH, "r") as f:
        for line in f:
            m = re.match(r"- (.+?): missing ([\d, ]+)", line)
            if m:
                folder = m.group(1)
                nums = set(int(x) for x in m.group(2).replace(",", " ").split())
                missing[folder] = nums
    return missing

def write_missing_list(missing):
    with open(LISTA_PATH, "w") as f:
        f.write("# Gaps in Comics Collections\n\n")
        for folder, nums in sorted(missing.items()):
            if nums:
                gaps_str = ", ".join(str(n) for n in sorted(nums))
                f.write(f"- {folder}: missing {gaps_str}\n")

def main():
    print("Conectando ao NAS e lendo arquivos...")
    remote = get_remote_listing()
    missing = get_missing_list()
    updated = {}
    for folder, nums in tqdm(missing.items(), desc="Verificando gaps existentes"):
        if folder in remote:
            still_missing = nums - remote[folder]
            if still_missing:
                updated[folder] = still_missing
        else:
            updated[folder] = nums
    for folder, files in tqdm(remote.items(), desc="Procurando novos gaps"):
        if not files:
            continue
        min_n, max_n = min(files), max(files)
        expected = set(range(min_n, max_n + 1))
        gaps = expected - files
        if gaps:
            if folder in updated:
                updated[folder] = updated[folder] | gaps
            else:
                updated[folder] = gaps
    write_missing_list(updated)
    print(f"Atualização concluída. Veja o arquivo: {LISTA_PATH}")

if __name__ == "__main__":
    main()
