#!/usr/bin/env python3
import unicodedata


ENTRADA = 'pt_BR.dic'
SAIDA = 'palavras.txt'


def normalizar(txt):
    """Remove acentos e transforma 'A' ou 'ª' em 'a'."""
    norm_txt = unicodedata.normalize('NFKD', txt).lower()
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


def chave(txt):
    """Manter palavras acentuadas após as não acentuadas"""
    codigos = tuple(ord(c) for c in txt)
    return (normalizar(txt), codigos)


palavras = set()
with open(ENTRADA, encoding='latin-1') as entrada:
    for i, linha in enumerate(entrada):
        if i == 0:
            continue  # ignorar primeira linha (contagem)
        linha = linha.strip()
        linha = linha.split('/')[0]
        partes = linha.split('-')
        sufixo = partes[-1]
        if len(sufixo) == 2 and sufixo.upper() == sufixo:
            continue  # ignorrar nomes de cidades
        if linha:  # para evitar palavra vazia
            palavras.add(linha)  # incluir palavra composta
        if len(partes) > 1:
            for palavra in partes:
                if palavra:
                    palavras.add(palavra)  # para evitar palavra vazia

    qt_original = i

msg = '{} palavras na lista original, {} na lista gerada: {} adicionadas'
extra = len(palavras) - qt_original
print(msg.format(qt_original, len(palavras), extra))

palavras = sorted(palavras, key=chave)

with open(SAIDA, 'wt', encoding='utf-8') as saida:
    saida.write('\n'.join(palavras))
    saida.write('\n')

