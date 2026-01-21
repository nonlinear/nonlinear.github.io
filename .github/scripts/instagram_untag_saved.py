"""
Script para desmarcar (untag) posts salvos do Instagram a partir de uma lista de links em um arquivo markdown.

- Lê links do arquivo especificado (ex: links/reels.md)
- Para cada link, abre no Instagram, tenta clicar no botão Remove (untag)
- Se conseguir, remove o marcador 🚧 da linha
- Se não conseguir, mantém 🚧
- Atualiza o arquivo ao final

Requisitos:
- Faça login manualmente no Instagram (browser visível)
- O caminho do arquivo de links pode ser definido por IG_SCRAPE_OUTPUT_PATH no .env

"""
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

# Carrega .env
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))
LINKS_FILE = os.getenv('IG_SCRAPE_OUTPUT_PATH') or os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "links/reels.md")

# Lê links do arquivo
with open(LINKS_FILE, 'r') as f:
    lines = [line.strip() for line in f if line.strip()]


# Marca linhas que precisam de untag e prepara para enriquecer com título/tags
import re
def extract_url(line):
    m = re.search(r'(https://www.instagram.com/[\w\-/]+)', line)
    return m.group(1) if m else None

def extract_hashtags(text):
    return re.findall(r"#\w+", text)

def extract_title(text):
    if not text:
        return None
    return text.split('\n')[0].strip()

new_lines = []
for line in lines:
    if not line.startswith('-'):
        # Adiciona 🚧 se não tiver
        if '🚧' not in line:
            line = f'- 🚧 {line}'
    new_lines.append(line)

print(f"Arquivo {LINKS_FILE} preparado para enriquecer com título e tags.")

# Abre browser visível para login manual
visible_options = uc.ChromeOptions()
visible_options.add_argument("--disable-gpu")
visible_options.add_argument("--window-size=1920,1080")
visible_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
browser = uc.Chrome(options=visible_options)

try:
    print("Abra o navegador e faça login manualmente no Instagram. Depois pressione Enter aqui para continuar...")
    browser.get("https://www.instagram.com/accounts/login/")
    input()


    # Para cada linha com 🚧, extrai título e tags (NÃO faz untag)
    updated_lines = []
    for line in new_lines:
        if '🚧' in line:
            link = extract_url(line)
            if not link:
                updated_lines.append(line)
                continue
            print(f"Processando: {link}")
            browser.get(link)
            time.sleep(2.5)
            title = None
            hashtags = []
            try:
                # Extrai caption
                caption_elem = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"C4VMK")]/span'))
                )
                caption = caption_elem.text
                hashtags = extract_hashtags(caption)
                title = extract_title(caption)
            except Exception as e:
                print(f"  Não foi possível extrair caption: {e}")
            # Atualiza linha para formato: - 🚧 [TITLE](LINK) #group #tags
            group_tags = ' '.join([t for t in line.split() if t.startswith('#')])
            tag_str = ' '.join(hashtags)
            if title:
                updated_line = f'- 🚧 [{title}]({link}) {group_tags} {tag_str}'.strip()
            else:
                updated_line = f'- 🚧 {link} {group_tags} {tag_str}'.strip()
            updated_lines.append(updated_line)
        else:
            updated_lines.append(line)
    # Salva arquivo atualizado
    with open(LINKS_FILE, 'w') as f:
        for line in updated_lines:
            f.write(line + '\n')
finally:
    browser.quit()
print("Processo de untag finalizado.")
