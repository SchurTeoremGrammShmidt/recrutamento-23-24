from pysondb import getDb

ficheiro = getDb('Calendario.json')


def criar_task():
    tasklist = {}  # {'anos': {'data': '15', 'descricao': 'festa de anos'},'festa': {'data': '15', 'descricao': 'festa de anos'}}
    return tasklist


def ask_input(prompt):
    return input('prompt').lower()

def descricao_evento(nome,tasklist):
    descricao=input('Qual a descricao que deseja?')
    tasklist[nome]['Descricao'] = descricao

def data_evento(nome,tasklist):
    data=input('Qual a data que deseja')
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
        nome=input('Digite o nome do seu evento')
        if nome in Tasklist:
            repetido=ask_input('já existe um evento com esse nome, gostaria de editar ou cancelar')
            if repetido=='editar':
                editar(nome)
            elif repetido=='sair':
                break
        elif nome not in Tasklist:
            Tasklist[nome]={}
            data_evento(nome,Tasklist)
            descricao_evento(nome,Tasklist)
            print(Tasklist)

adicionar_evento(criar_task())

def editar():
    pass

def remover():
    pass

