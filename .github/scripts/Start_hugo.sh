#!/bin/zsh
# Mata qualquer hugo rodando
echo "🧹 Limpando processos Hugo anteriores..."
pkill -f 'hugo serve'
sleep 1

# Atualiza o repo
echo "🔄 Atualizando repositório..."
git pull

# Inicia hugo em background (bind 0.0.0.0 permite acesso de outros devices)
echo "🚀 Iniciando Hugo server..."
nohup hugo serve -D --bind 0.0.0.0 --baseURL http://$(ipconfig getifaddr en0 || ipconfig getifaddr en1):1313 > hugo.log 2>&1 &

# Aguarda 3 segundos
sleep 3
# Pega o IP local
LOCAL_IP=$(ipconfig getifaddr en0 || ipconfig getifaddr en1)

# Determina qual URL abrir baseado no arquivo passado
OPEN_URL="http://${LOCAL_IP}:1313/"

if [ -n "$1" ]; then
  # Se passou um arquivo como argumento
  FILE_PATH="$1"

  # Remove ./ do início se houver
  FILE_PATH="${FILE_PATH#./}"

  # Se for path absoluto, converte pra relativo
  if [[ "$FILE_PATH" == /* ]]; then
    REPO_ROOT="$(pwd)"
    FILE_PATH="${FILE_PATH#$REPO_ROOT/}"
  fi

  # Verifica se o arquivo está dentro de content/
  if [[ "$FILE_PATH" == content/* ]]; then
    # Remove content/ do início
    RELATIVE_PATH="${FILE_PATH#content/}"

    # Pega só o diretório (se houver)
    DIR_PATH=$(dirname "$RELATIVE_PATH")

    # Pega o nome do arquivo sem extensão
    FILENAME=$(basename "$RELATIVE_PATH" | sed 's/\.[^.]*$//')

    # Se está em um subdiretório (não é root)
    if [ "$DIR_PATH" != "." ]; then
      OPEN_URL="http://${LOCAL_IP}:1313/${DIR_PATH}/${FILENAME}/"
    else
      OPEN_URL="http://${LOCAL_IP}:1313/${FILENAME}/"
    fi
  fi
fi

# Abre o navegador com URL apropriada
open "$OPEN_URL"
# Mostra o URL pra acessar no iPhone
echo "📱 Acesse no iPhone: $OPEN_URL"
