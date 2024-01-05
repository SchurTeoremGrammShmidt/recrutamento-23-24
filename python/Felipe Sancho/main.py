import CAP,events,json,os
#criar/pegar o horário

H = CAP.new()
if os.path.getsize("persistance.json") > 2:
    with open("persistance.json","r") as f:
        p = json.load(f)

        while CAP.size(p) != 0:
            evt = CAP.next(p)
            H = CAP.add(H, events.new(events.kind(evt),events.desc(evt),events.Stime(evt),events.Ftime(evt)))
            p = CAP.remove_first(p)

#Função utilizada ao longo do programa
def pretty_print(H):
    aux = H[:]
    print("Horário Atual:")
    while CAP.size(aux) != 0: #Imprime o horário em um formato mais legível
        print(CAP.next(aux))
        aux = CAP.remove_first(aux)



while True:
    print("O que quer fazer?")
    print("1 - Adicionar uma nova tarefa")
    print("2 - remover uma tarefa")
    print("3 - verificar o horário atual")
    print("4 - Limpar completamente o horário, e apagar o horário persistente")
    print("5 - sair")
    escolha = input(": ")
    
    if escolha == "1":
        kind = input("tipo do evento: ")
        desc = input("desc do evento: ")
        while True:
            Stime = float(input("tempo de início do evento: "))
            Ftime  = float(input("tempo de fim do evento: "))
            if Stime > Ftime:
                print("O tempo de fim da tarefa deve ser após o tempo de início")
            else:
                break
        H = CAP.add(H, events.new(kind, desc, Stime, Ftime))#adiciona o evento ao horário
        pretty_print(H)

    elif escolha == "2":
        kind = input("tipo do evento: ")
        Time = float(input("tempo em que o evento esta a decorrer: "))
        H = CAP.remove(H, kind, Time)
        pretty_print(H)

    elif escolha == "3":
       pretty_print(H)

    elif escolha == "4":#Limpar o Horário
        H = CAP.new()
        with open("persistance.json","w") as f:
            json.dump(H,f,indent=2)
        print("Horário apagado :(")

    elif escolha == "5":
        print("Deseja guardar o horário atual?")
        guardar = input("S/N: ")
        if guardar.lower() == "s":
            with open("persistance.json","w") as f:#Guarda o horário no ficheiro Json
                json.dump(H,f,indent=2)
        break
        