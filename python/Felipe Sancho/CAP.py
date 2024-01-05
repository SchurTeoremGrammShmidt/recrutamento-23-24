import events

def new():
    return []
def binary_search(cap, target):
        start = 0
        end = len(cap) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if events.Stime(cap[mid]) == target:
                return mid
            elif events.Stime(cap[mid]) < target:
                start = mid + 1
            else:
                end = mid - 1

        return start
  
def add(cap, evt): # adiciona evt a CAP por ordem cronológica

    cap.insert(binary_search(cap, events.Stime(evt)), evt)
    return cap

def remove(cap, Kind, Time): #Filtra os eventos que tenham essas caracteristicas
    return list(filter(lambda x: Kind != events.kind(x) or events.Stime(x) > Time or Time > events.Ftime(x), cap))

def remove_first(cap):
    return cap[1:]

def next(cap): #devolve o proximo evento da CAP
    return cap[0]

def size(cap):
    return len(cap)
