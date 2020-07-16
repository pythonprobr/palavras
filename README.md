# Palavras PT-BR

O arquivo `palavras.txt` neste repositório contém mais de 320.000 palavras do idioma português brasileiro.

A fonte principal é a lista de palavras do corretor ortográfico LibreOffice, obtida aqui:

https://cgit.freedesktop.org/libreoffice/dictionaries/plain/pt_BR/pt_BR.dic

O arquivo original foi processado pelo programa `converter.py` para:

1. converter a codificação de Latin-1 para UTF-8

2. remover os códigos alfabéticos apensados a algumas palavras, após uma `/`

3. remover nomes de cidades (ex. "Carnaubal-CE")

4. acrescentar em linhas separadas as palavras que formam termos compostos (ex. casa-forte)

5. reordenar tudo alfabeticamente

O motivo do passo 4 é que a palavra "casa" não tem uma entrada individual no arquivo original! Se alguém souber o motivo, cadastre um *issue* explicando em que parte do código-fonte do corretor ortográfico do LibreOffice está a informação de que "casa" é uma palavra.

# Atualização 16/07/2020

Mais de 250 mil palavras foram adicionadas ao arquivo.  
Elas são provenientes do dicionário de palavras do linux, que pode ser conferido no arquivo `/usr/share/dict/brazilian` (distribuição baseada no Ubuntu 18.04).  
Assim, palavras com hífen e palavras comuns faltantes no arquivo original agora foram preenchidas.  
A estratégia de mescla dos dois arquivos foi feita com um script em python da seguinte forma:  
  
1. Para cada palavra do arquivo `brazilian`, foi checado se a palavra existia no arquivo `palavras.txt`.

2. Se a palavra não existia, foi acrescentada ao fim da lista.  

3. Ao final, a lista toda foi ordenada alfabeticamente.  
