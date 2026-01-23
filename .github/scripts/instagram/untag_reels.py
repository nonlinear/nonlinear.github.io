"""
Remove posts from Instagram saved collection and update markdown file.

This script:
- Reads markdown file with Instagram post links
- Finds posts marked with #untag
- Logs into Instagram and visits each post
- Clicks the "Remove" button to unsave the post
- Removes #untag tag from markdown file after successful removal

Dependencies:
    - undetected-chromedriver
    - selenium
    - python-dotenv

TO USE:
    python3.11 .github/scripts/instagram/untag_reels.py
"""

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import os
import re
import random
import tempfile
from dotenv import load_dotenv

# Import shared login function
from login import login_to_instagram

def extract_url(line):
    """Extract Instagram URL from markdown line."""
    m = re.search(r'(https://www\.instagram\.com/[\w\-/]+)', line)
    return m.group(1) if m else None

def remove_untag_from_line(line):
    """Remove #untag from a line."""
    return re.sub(r'\s*#untag\b', '', line).strip()

def untag_post(browser, url):
    """
    Visit Instagram post and click the Remove/Unsave button.

    Returns:
        bool: True if successfully untagged, False otherwise
    """
    try:
        browser.get(url)
        time.sleep(random.uniform(2.0, 3.0))

        # Wait for page to load
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "svg"))
        )

        # Find the Remove button (SVG with aria-label="Remove")
        try:
            remove_button = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'svg[aria-label="Remove"]'))
            )

            # Click the button (click parent if needed)
            parent = remove_button.find_element(By.XPATH, '..')
            parent.click()

            print(f"    ✓ Clicked Remove button")

            # Wait a moment for the action to process
            time.sleep(1.5)

            # Confirmation: check if button changed to "Save" (meaning it was removed)
            try:
                WebDriverWait(browser, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'svg[aria-label="Save"]'))
                )
                print(f"    ✓ Confirmed: Post removed from saved")
                return True
            except TimeoutException:
                print(f"    ⚠ Could not confirm removal (Save button not found)")
                # Still return True since we clicked Remove
                return True

        except (TimeoutException, NoSuchElementException):
            print(f"    ✗ Remove button not found (post may already be unsaved)")
            return False

    except Exception as e:
        print(f"    ✗ Error: {e}")
        return False

# Main execution
if __name__ == "__main__":
    # Load environment
    load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))

    # Ask for file path
    workspace_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    default_file = os.getenv('IG_SCRAPE_OUTPUT_PATH') or os.path.join(workspace_root, "links/reels.md")
    file_path = input(f"Enter file path to process (default: {default_file}): ").strip() or default_file

    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        exit(1)

    # Read file
    with open(file_path, 'r') as f:
        lines = [line.rstrip() for line in f]

    # Filter lines that need untagging
    lines_to_untag = []
    for idx, line in enumerate(lines):
        if line.strip() and '#untag' in line:
            url = extract_url(line)
            if url:
                lines_to_untag.append((idx, line, url))

    if not lines_to_untag:
        print("No posts need untagging. All posts processed!")
        exit(0)

    print(f"\nFound {len(lines_to_untag)} posts to untag:")
    for idx, line, url in lines_to_untag[:5]:
        print(f"  - {url}")
    if len(lines_to_untag) > 5:
        print(f"  ... and {len(lines_to_untag) - 5} more")

    # Ask how many to process
    default_count = min(10, len(lines_to_untag))
    while True:
        try:
            how_many = input(f"\nHow many posts to untag? (default {default_count}, max {len(lines_to_untag)}): ").strip()
            how_many = int(how_many) if how_many else default_count
            if 1 <= how_many <= len(lines_to_untag):
                break
            else:
                print(f"Please enter a number between 1 and {len(lines_to_untag)}")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Limit to requested count
    lines_to_untag = lines_to_untag[:how_many]

    # Login to Instagram
    browser = login_to_instagram()

    try:
        # Process each post
        removed_count = 0
        for current_idx, (idx, old_line, url) in enumerate(lines_to_untag, 1):
            print(f"\n[{current_idx}/{len(lines_to_untag)}] Processing: {url}")

            if untag_post(browser, url):
                # Remove #untag from line
                new_line = remove_untag_from_line(old_line)
                lines[idx] = new_line
                removed_count += 1
            else:
                print(f"  ⚠ Keeping #untag tag (removal failed)")

        # Save updated file (safe file writing)
        temp_fd, temp_path = tempfile.mkstemp(suffix='.md', text=True)
        try:
            with os.fdopen(temp_fd, 'w') as f:
                for line in lines:
                    f.write(line + '\n')
            os.replace(temp_path, file_path)
            print(f"\n✓ Untag complete! Removed {removed_count}/{len(lines_to_untag)} posts from Instagram.")
            print(f"  Saved to: {file_path}")
        except Exception as e:
            os.unlink(temp_path)
            print(f"\n✗ Error saving file: {e}")
            raise

    finally:
        browser.quit()
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

    # Salva arquivo atualizado (safely)
    import tempfile
    temp_fd, temp_path = tempfile.mkstemp(suffix='.md', text=True)
    try:
        with os.fdopen(temp_fd, 'w') as f:
            for line in updated_lines:
                f.write(line + '\n')
        os.replace(temp_path, LINKS_FILE)
    except Exception as e:
        os.unlink(temp_path)
        print(f"Erro ao salvar arquivo: {e}")
        raise
finally:
    browser.quit()
print("Processo de untag finalizado.")
