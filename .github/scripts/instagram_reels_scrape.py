"""
This script automates the extraction and organization of your Instagram saved posts (reels and regular posts):

- Logs into Instagram using credentials from .env or command line.
- Navigates to your 'all-posts' saved group.
- Scrolls to load up to 100 saved posts.
- Extracts post links and hashtags from each post.
- Saves the results to links/reels.md in markdown format.
- After saving, automatically removes (untags) those posts from your saved items.

To run:
    /opt/homebrew/bin/python3.11 .github/scripts/instagram_reels_scrape.py

You can also pass --user and --pass arguments, but .env is preferred for password security.
"""

# This file was renamed from instagram_scrape_mental_health.py
# All logic preserved.

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import getpass
import argparse
from dotenv import load_dotenv
import os
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

parser = argparse.ArgumentParser(description="Scrape Instagram saved group links and hashtags.")
parser.add_argument("--user", default="nonlinear", help="Instagram username")
parser.add_argument("--pass", dest="password", help="Instagram password (use with caution)")
args = parser.parse_args()

# Load .env file
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))

# Get credentials from .env, fallback to CLI args
INSTAGRAM_USER = os.getenv('INSTAGRAM_USER', args.user)
INSTAGRAM_PASS = os.getenv('INSTAGRAM_PASS', args.password) or getpass.getpass("Digite sua senha do Instagram: ")

SAVED_URL = "https://www.instagram.com/nonlinear/saved/"

# Generalization: set output path and count from environment variables

    # Extrai título e tags do primeiro post
    first_title = None
    first_tags = []
    if links:
        browser.get(links[0])
        time.sleep(random.uniform(2.0, 4.0))
        try:
            caption_elem = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"C4VMK")]/span'))
            )
            caption = caption_elem.text
            first_tags = extract_hashtags(caption)
            if caption:
                first_title = caption.split('\n')[0]
        except Exception:
            pass
    if not first_title:
        first_title = "(sem título)"

    tag_str = " ".join([f"#{GROUP_NAME}"] + first_tags)
    results = []
    for link in links:
        results.append(f"- 🚧 [{first_title}]({link}) {tag_str}")

    with open(OUTPUT_FILE, "a") as f:
        for line in results:
            f.write(line + "\n")
    print(f"[7/7] {len(results)} links adicionados em {OUTPUT_FILE}")
    time.sleep(5)

    # Encontrar todos os grupos de salvos
    print("[3/6] Buscando grupos de salvos...")
    group_links = browser.find_elements(By.CSS_SELECTOR, 'a[href^="/nonlinear/saved/"]')
    group_names = []
    group_hrefs = []
    for el in group_links:
        name = el.text.strip()
        href = el.get_attribute("href")
        if name and href and not href.endswith("all-posts/"):
            group_names.append(name)
            group_hrefs.append(href)

    if not group_names:
        print("Nenhum grupo encontrado além de All posts.")
        browser.quit()
        sys.exit(1)


    print("\nGrupos encontrados:")
    for idx, name in enumerate(group_names, 1):
        print(f"  [{idx}] {name}")
    while True:
        try:
            group_idx = int(input("\nDigite o número do grupo desejado: "))
            if 1 <= group_idx <= len(group_names):
                break
            else:
                print("Número inválido.")
        except Exception:
            print("Entrada inválida.")
    GROUP_NAME = group_names[group_idx-1].replace(" ", "-").lower()
    GROUP_URL = group_hrefs[group_idx-1]
    print(f"[4/6] Entrando no grupo: {GROUP_NAME} ({GROUP_URL})")
    browser.get(GROUP_URL)
    time.sleep(5)




    while True:
        try:
            user_count = int(input(f"Quantos links deseja coletar deste grupo? (padrão {SCRAPE_COUNT}): ") or SCRAPE_COUNT)
            if user_count > 0:
                break
            else:
                print("Digite um número positivo.")
        except Exception:
            print("Entrada inválida.")
    print(f"[5/6] Coletando os {user_count} primeiros links do grupo...")
    for _ in range(5):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(1.0, 2.0))

    elements = browser.find_elements(By.CSS_SELECTOR, 'a._a6hd')
    links = []
    for el in elements:
        href = el.get_attribute("href")
        if href and ("/reel/" in href or "/p/" in href):
            links.append(href)
        if len(links) >= user_count:
            break
    print(f"[6/6] {len(links)} links encontrados para processar.")


    def extract_hashtags(text):
        import re
        return re.findall(r"#\w+", text)



    results = []
    first_post_info = None
    for idx, link in enumerate(links, 1):
        print(f"  Processando link {idx}/{len(links)}: {link}")
        browser.get(link)
        time.sleep(random.uniform(2.0, 4.0))
        author = None
        title = None
        hashtags = []
        try:
            # Tenta pegar o máximo de hashtags do post
            caption_elem = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"C4VMK")]/span'))
            )
            caption = caption_elem.text
            hashtags = extract_hashtags(caption)
            # Tenta pegar o autor
            try:
                author_elem = browser.find_element(By.XPATH, '//a[contains(@href, "/") and contains(@class, "notranslate")]')
                author = author_elem.text
            except Exception:
                pass
            # Tenta pegar o título (primeira linha do caption)
            if caption:
                title = caption.split('\n')[0]
        except Exception:
            pass
        tags = " ".join(hashtags + [f"#{GROUP_NAME}"])
        results.append(f"{link} {tags}")
        if idx == 1:
            first_post_info = {
                "link": link,
                "author": author,
                "tags": hashtags,
                "title": title
            }

    if first_post_info:
        print("\n[INFO] Primeiro post:")
        print(f"  Link: {first_post_info['link']}")
        print(f"  Autor: {first_post_info['author']}")
        print(f"  Tags: {first_post_info['tags']}")
        print(f"  Título: {first_post_info['title']}")



    with open(OUTPUT_FILE, "a") as f:
        for line in results:
            f.write(line + "\n")
    print(f"[7/7] {len(results)} links adicionados em {OUTPUT_FILE}")



    print("[8/8] Removendo dos salvos (tentando só os primeiros {SCRAPE_COUNT})...")
    for idx, link in enumerate(links, 1):
        try:
            browser.get(link)
            time.sleep(random.uniform(1.5, 3.0))
            # Tenta encontrar o botão Remove pelo novo seletor
            remove_btn = None
            # 1. Tenta pelo aria-label
            try:
                remove_btn = browser.find_element(By.XPATH, '//button[.//svg[@aria-label="Remove"]]')
            except Exception:
                pass
            # 2. Tenta pelo CSS class (fallback)
            if not remove_btn:
                btns = browser.find_elements(By.CSS_SELECTOR, 'div[role="button"] svg[aria-label="Remove"]')
                if btns:
                    remove_btn = btns[0].find_element(By.XPATH, './../..')
            if remove_btn:
                remove_btn.click()
                print(f"    Removido dos salvos: {link}")
                time.sleep(1)
            else:
                print(f"    Botão 'Remove' não encontrado para: {link}")
        except Exception as e:
            print(f"    Erro ao remover dos salvos para {link}: {e}")
        if idx >= SCRAPE_COUNT:
            break
finally:
    browser.quit()
