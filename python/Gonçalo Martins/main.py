from pysondb import getDb
import sys, subprocess

ficheiro = getDb('Calendario.json')


def clear_screen():
    sistema_operativo = sys.platform
    if sistema_operativo == 'win32':
        subprocess.run('cls', shell=True)
    elif sistema_operativo == 'linux' or sistema_operativo == 'darwin':
        subprocess.run('clear', shell=True)


def criar_task():
    tasklist = {}  # {'anos': {'data': '15', 'descricao': 'festa de anos'},'festa': {'data': '15', 'descricao': 'festa de anos'}}
    return tasklist


def ask_input(prompt):
    return input('prompt').lower()


def descricao_evento(nome, tasklist):
    descricao = input('Qual a descricao que deseja?')
    tasklist[nome]['Descricao'] = descricao


def data_evento(nome, tasklist):
    data = input('Qual a data que deseja')
    tasklist[nome]['Data'] = data


def verify_input_continuar_sair():
    while True:
        user_input = input('Deseja continuar ou sair').lower()
        if user_input == 'continuar':
            pass
        elif user_input == 'sair':
            pass
        else:
            print('Input incorrecto tente outra vez')


def adicionar_evento(Tasklist):
    while True:
        nome = ask_input('Digite o nome do evento que deseja')
        if nome in Tasklist:
            repetido = ask_input('já existe um evento com esse nome, gostaria de editar ou cancelar')
            if repetido == 'editar':
                editar_evento_existente(Tasklist, nome)
            elif repetido == 'sair':
                return
        elif nome not in Tasklist:
            Tasklist[nome] = {}
            data_evento(nome, Tasklist)
            descricao_evento(nome, Tasklist)
            clear_screen()
            print("Evento adicionado com sucesso")
            return Tasklist




def editar_evento_existente(tasklist, nome):
    data_evento(nome, tasklist)
    descricao_evento(nome, tasklist)
    return tasklist


def editar_evento(Tasklist):
    while True:
        print(Tasklist.keys())
        nome = ask_input('Qual o evento que gostaria de editar')
        if nome not in Tasklist:
            while True:
                input = ask_input('Gostaria de continuar ou sair?')
                if input == 'sair':
                    return
                if input == 'continuar':
                    break
                else:
                    print('input incorreto')
        else:


def remover_evento(Tasklist):
    while True:
        print(Tasklist.keys())
        inpututilizador = input('Diga o nome do evento que pretende eliminar ou se pretende sair')
        if inpututilizador in Tasklist:
            del Tasklist[inpututilizador]
            return Tasklist
        if inpututilizador=='sair':
            return Tasklist
        else:
            print('Input incorreto')
