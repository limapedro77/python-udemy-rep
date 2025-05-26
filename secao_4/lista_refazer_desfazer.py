import os
import sys

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'{tarefa}')
    print()

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f"'{tarefa}' removida da lista de tarefas.")
    tarefas_refazer.append(tarefa)
    print()

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f"'{tarefa}' adicionada na lista de tarefas.")
    tarefas.append(tarefa)
    print()

def adicionar(tarefa, tarefas, tarefas_refazer):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    tarefas.append(tarefa)
    tarefas_refazer.clear()           # limpa histórico de refazer
    print(f"Tarefa adicionada: '{tarefa}'")
    print()

# --- Programa principal ---
tarefas = []
tarefas_refazer = []

while True:
    print('\nComandos: listar, desfazer, refazer, clear, sair')
    escolha = input('Digite uma tarefa ou comando: ').strip().lower()

    if escolha == 'listar':
        listar(tarefas)

    elif escolha == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)

    elif escolha == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)

    elif escolha == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')

    elif escolha == 'sair':
        print('Até mais!')
        sys.exit()

    else:
        adicionar(escolha, tarefas, tarefas_refazer)
        listar(tarefas)
