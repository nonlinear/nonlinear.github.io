#!/bin/zsh
hugo
git add -A
echo "Digite a mensagem do commit:"
read MSG
git commit -m "$MSG"
git pull
git push
