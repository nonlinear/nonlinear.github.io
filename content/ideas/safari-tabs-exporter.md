# Safari Tabs Exporter - Guia Definitivo

## O que faz:

1. Captura todas as tabs abertas no Safari do iPhone/iPad
2. Formata como markdown: `- [título](url)`
3. Salva arquivo em iCloud Drive → Shortcuts/safari-tabs-export.md
4. Apaga todas as tabs do Safari
5. Mostra notificação de conclusão

---

## IMPORTANTE: Realidade do iOS 15+

⚠️ **Não dá pra criar shortcuts programaticamente desde iOS 15 (2021)**

- Apple assina todos os arquivos `.shortcut`
- Arquivos não-assinados são rejeitados
- Único jeito: **criar manualmente no iPhone/iPad**

---

## Criar no iPhone/iPad - Passo a Passo EXATO

### 1. Abre **Shortcuts** (ícone roxo/azul com símbolos)

### 2. Toca **+** (canto superior direito)

### 3. Toca **Add Action** (botão azul no meio da tela)

---

## Ações - Busca EXATA (use Ctrl+F na lista abaixo)

**DICA:** Quando buscar, digite EXATAMENTE como aparece. Se não achar, tenta os sinônimos.

### Ação 1: Get Safari Web Pages

**Busca:** `safari` ou `web pages` ou `get safari`
**Nome exato:** "Get current Safari web page" ou "Get Current Safari Web Page" ou "Safari Web Page"
**Aparece em:** Apps → Safari
**O que fazer:**

- Toca na ação
- Se aparecer opções, escolhe **"Safari Web Pages"** ou **"All Tabs"**

### Ação 2: Set Variable

**Busca:** `set variable` ou `variable`
**N Ação 3: Get Device Details (Device Name)
**Busca:** `device` ou `device name`
**Nome exato:** "Get Device Details"
**Aparece em:** Device → Device Information
**O que fazer:\*\*

- Toca na ação
- Toca em "Detail" (palavra azul na ação)
- Escolhe: **"Device Name"**

### Ação 4: Set Variable

**Variável:** `DeviceName`

### Ação 5: Current Date

**Busca:** `date` ou `current date`
**Nome exato:** "Current Date"
**Aparece em:** Calendar

### Ação 6: Format Date

**Busca:** `format date` ou `format`
**Nome exato:** "Format Date"
**Aparece em:** Calendar
**O que fazer:**

- Toca na ação
- Toca em "Date Format" (palavra azul)
- Escolhe: **"Custom"**
- No campo de formato, digita: `yyyy-MM-dd HH:mm`
  Ação 8: Repeat with Each
  **Busca:** `repeat` ou `repeat each` ou `loop`
  **Nome exato:** "Repeat with Each"
  **Aparece em:** Scripting → Control Flow
  **O que fazer:**
- Toca na ação
- Toca onde diz "Input" ou "Repeat Item" (palavra azul)
- Escolhe variável: **"AllTabs"** (pode estar como "Safari Web Pages" ou "Get Safari Web Pages")
- Se não aparecer variável, toca "Select Magic Variable" e escolhe a ação 1ar tabs)

- Busca: "Count"
- Conta: `AllTabs`

#### Ação 11: Set Variable

- Nome: `TabCount`

#### Ação 12: Repeat (loop)

- Busca: "Repeat"
- Repeat `TabCount` times

#### Ação 13: Get Item from List (dentro do Repeat)

- Busca: "Get Item from List"
- Get item **at index** `Repeat Index` from `TabTitles`

#### Ação 14: Set Variable

Ação 9: Get Details (Page Title)
**Busca:** `get details` ou `details` ou `name`
**Nome exato:** "Get Details of Safari Web Page"
**Aparece em:** Web → Safari
**O que fazer:**

- Toca na ação
- Toca em "Detail" (palavra azul)
- Escolhe: **"Page Title"** ou **"Name"**

### Ação 10: Set Variable

**Variável:** `PageTitle`

### Ação 11: Get Details (URL)

**Mesma ação anterior**
**O que fazer:**

- Adiciona novamente "Get Details of Safari Web Page"
- Toca em "Detail"
- Escolhe: **"Page URL"** ou **"URL"**

### Ação 12: Set Variable

**Variável:** `PageURL`

### Ação 13: Text (formatar linha markdown)

**Busca:** `text`
**Nome exato:** "Text"
**Aparece em:** Scripting → Text
**O que fazer:**

- Toca na ação
- No campo de texto, digita: `- [`
- Toca no campo → aparece menu → **"Select Variable"**
- Escolhe: **"PageTitle"**
- Continua digitando: `](`
- Select Variable novamente
- Escolhe: **"PageURL"**
- Fecha: `)`
- Resultado final: `- [PageTitle](PageURL)` (com variáveis em azul)

### Ação 14: Add to Variable

**Busca:** `add variable` ou `add to`
**Nome exato:** "Add to Variable"
**Aparece em:** Scripting → Variables
**O que fazer:**

- Toca na ação
- Se pedir nome de variável, cria nova: `MarkdownList`
- A ação vai acumular cada linha markdown

### Ação 15: End Repeat

**Já aparece automaticamente** depois do "Repeat with Each"

- Se não aparecer, busca `end repeat` e adiciona

#### Ação 23: Text (montar nota completa)

- Escreve:
  Ação 16: Text (montar arquivo final)
  **O que fazer:**
- Adiciona outra ação "Text"
- No campo, digita: `# `
- Select Variable → **"DeviceName"**
- Continua: `Safari Tabs -`
- Select Variable → **"Timestamp"**
- **Enter** (quebra linha) **duas vezes**
- Select Variable → **"MarkdownList"**
- Resultado:

  ```
  # DeviceName Safari Tabs - Timestamp

  MarkdownList
  ```

### Ação 17: Save File

**Busca:** `save file` ou `save`
**Nome exato:** "Save File"
**Aparece em:** Documents → Files
**O que fazer:**

- Toca na ação
- **Ask Where to Save:** OFF (desliga)
- **Service:** iCloud Drive (se pedir)
- **File Path:** toca e digita: `Shortcuts/safari-tabs-export.md`
- **Overwrite if Exists:** ON (liga)

### Ação 18: Close All Tabs with Safari

**Busca:** `close tabs` ou `close all`
**Nome exato:** "Close All Tabs with Safari" ou "Close Safari Tabs"
**Aparece em:** Apps → Safari
**O que fazer:**

- Só adiciona, sem configurar nada

### Ação 19: Show Notification

\*\*BFinalizar

### 1. Nomeia o Shortcut

- Toca nos 3 pontinhos **⋯** (canto superior direito)
- Toca no nome (em cima)
- Digita: **Safari Tabs Exporter**
- Done

### 2. Escolhe ícone e cor (opcional)

- Ainda nas configurações (⋯)
- Toca no ícone
- Escolhe ícone de Safari ou Tabs
- Escolhe cor (azul ou laranja combina)

### 3. Configurações extras (opcional)

- **Show in Share Sheet:** OFF (deixa desligado)
- **Show in Widget:** ON (se quiser)
- **Pin to Top:** ON (facilita achar)

### 4. Done!

---

## Como usar:

### No iPhone/iPad:

1. Abre o app **Shortcuts**
2. Toca no shortcut **Safari Tabs Exporter**
3. Aguarda notificação
4. Pronto! Arquivo salvo em iCloud Drive

### Via Siri:

"Hey Siri, Safari Tabs Exporter"

### No Mac (após criar):

```bash
# Ler o arquivo exportado
cat "/Users/nfrota/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/safari-tabs-export.md"

# Ou processar automaticamente
python3 process_tabs.py
```

---

## Troubleshooting

### "Não acho a ação X"

- Tenta os sinônimos listados
- Scroll até o fim da lista (algumas ações ficam longe)
- Verifica se digitou EXATAMENTE como aparece
- Versões antigas do iOS podem ter nomes diferentes

### "Ação não funciona"

- Verifica se escolheu a variável certa (texto azul)
- Confirm que "Repeat with Each" tá fechado com "End Repeat"
- Testa com poucas tabs primeiro (2-3)

### "Arquivo não aparece no Mac"

- Aguarda 10-30 segundos (sync do iCloud)
- Verifica se iCloud Drive tá ativo: Settings → iCloud → iCloud Drive
- Caminho: `~/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/`

### "Não apaga as tabs"

- Normal se tiver muitas (Safari limita)
- Roda novamente ou fecha manualmente

---

## Alternativas

### Versão SUPER simplificada (5 ações):

1. Get Safari Web Pages
2. Get Details → Page Title
3. Get Details → URL
4. Text: `- [Title](URL)` (com variáveis)
5. Copy to Clipboard

**Usa:** Universal Clipboard sincroniza pro Mac automaticamente

### Versão com Notes (em vez de arquivo):

Substitui "Save File" por:

- **Create Note** (ação do Notes app)
- **Show Compose Sheet:** OFF
- Nota sincroniza via iCloud Notes

---

## Recursos

- **URL Scheme para rodar do Mac:**

  ```
  open "shortcuts://run-shortcut?name=Safari%20Tabs%20Exporter"
  ```

- **Documentação oficial:**
  - https://support.apple.com/guide/shortcuts/welcome/ios
  - https://support.apple.com/guide/shortcuts/use-variables-apd5b0f84c34/ios

- **Comunidade:**
  - r/shortcuts: https://reddit.com/r/shortcuts
  - RoutineHub: https://routinehub.co/ri Tabs to Markdown"\*\* que alguém já criou:

https://www.icloud.com/shortcuts/

(busca por "safari tabs markdown" na galeria de shortcuts)
