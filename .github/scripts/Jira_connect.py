import os
import requests
import json
from datetime import datetime

# Configurações do usuário
ATLASSIAN_EMAIL = os.getenv("ATLASSIAN_EMAIL", "nfrota@wiley.com")
ATLASSIAN_API_TOKEN = os.getenv("ATLASSIAN_API_TOKEN")
ATLASSIAN_BASE_URL = os.getenv("ATLASSIAN_BASE_URL", "https://wiley-global.atlassian.net")
OUTPUT_DIR = "./wiley/jira"

# Função para autenticação
def get_auth_headers():
    return {
        "Authorization": f"Basic {requests.auth._basic_auth_str(ATLASSIAN_EMAIL, ATLASSIAN_API_TOKEN)}",
        "Content-Type": "application/json"
    }

# Função para buscar issues de todos os projetos
def fetch_issues():
    url = f"{ATLASSIAN_BASE_URL}/rest/api/3/search/jql"
    payload = {
        "jql": "(due >= startOfMonth() OR created >= -180d) ORDER BY due ASC",
        "maxResults": 1000
    }
    print(f"Payload: {payload}")  # Debugging: Print the payload
    response = requests.post(url, headers=get_auth_headers(), json=payload)
    print(f"Response Status: {response.status_code}")  # Debugging: Print the status code
    print(f"Response Content: {response.text}")  # Debugging: Print the response content
    response.raise_for_status()
    return response.json()["issues"]

# Função para gerar o relatório em JSON
def generate_json_report(issues):
    report = []
    for issue in issues:
        fields = issue["fields"]
        report.append({
            "title": fields["summary"],
            "description": fields.get("description", "Sem descrição"),
            "status": fields["status"]["name"],
            "labels": fields.get("labels", []),
            "client": fields.get("customfield_12345", "N/A"),  # Substitua customfield_12345 pelo campo correto
            "product": fields.get("customfield_67890", "N/A"),  # Substitua customfield_67890 pelo campo correto
            "technology": fields.get("customfield_11223", "N/A"),  # Substitua customfield_11223 pelo campo correto
            "link": f"{ATLASSIAN_BASE_URL}/browse/{issue['key']}"
        })
    return report

# Função para salvar o relatório
def save_report(report):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Salvar uma cópia no log
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"{OUTPUT_DIR}/{timestamp}.json"
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=4)

# Função principal
def main():
    print("Buscando issues do Jira...")
    issues = fetch_issues()
    print(f"Encontradas {len(issues)} issues.")

    print("Gerando relatório em JSON...")
    report = generate_json_report(issues)

    print("Salvando relatório...")
    save_report(report)
    print(f"Relatório salvo em: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
