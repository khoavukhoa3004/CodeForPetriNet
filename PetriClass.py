import graphviz

# Place: chua ten va token
class Place:
    def __init__(Place_object, name, token):
        Place_object.name = name
        Place_object.token = token
    
    def print_place(Place_object):
        print("{}: {}".format(Place_object.name, Place_object.token))

    def get_name(Place_object):
        return Place_object.name
    def get_token(Place_object):
        return Place_object.token

    # Place ---In----> Transition --- Out--->Place
    # In va Out deu chua Place va amount = 1
class In:
    def __init__(In_object, place, amount = 1):
        In_object.place = place
        In_object.amount = 1
    def triggle(In_object):
        # Remove Tokens
        In_object.place.token -= In_object.amount
    
    def Can_execute(In_object):
        if In_object.place.token >= In_object.amount:
            return True
        return False
class Out:
    def __init__(Out_object, place, amount =1):
        Out_object.place = place
        Out_object.amount = 1
    def triggle(Out_object):
        Out_object.place.token += Out_object.amount

# Transition chua tap cac In va tap cac Out
class Transition:
    def __init__(Transition_object,name, in_arc, out_arc):
        Transition_object.name = name
        Transition_object.in_arc = set(in_arc)
        Transition_object.out_arc = set(out_arc)
        
    def Can_fire(Transition_object):
        Execute = all(arc.Can_execute() for arc in Transition_object.in_arc)
        return Execute

    def fire(Transition_object):
        for arc in Transition_object.in_arc:
            arc.triggle()
        for arc in Transition_object.out_arc:
            arc.triggle()

# PetriNet co hai thanh phan: tap cac transition va tap cac place 
class PetriNet:
    def __init__(self, list_transition, list_place):
        self.list_transition = list_transition
        self.list_place = list_place
    def printMarking(self, count):
        print("M_{} = [".format(count), end ='')
        i = len(self.list_place)
        for place in self.list_place:
            print("{}.{}".format(place.token,place.name),end ='; ')
        print("]")
    def run(self):
        count = 0
        print("Initial Marking: ", end ='')
        self.printMarking(count)
        print("")
        count += 1
        while True:
            Execute = any(trans.Can_fire() for trans in self.list_transition)
            if not Execute:
                break
            for trans in self.list_transition:
                if trans.Can_fire():
                    while trans.Can_fire():
                        trans.fire()
                    print("firing \"{}\", ket qua thu duoc: ".format(trans.name), end='')
                    self.printMarking(count)
                    print("")
                    count += 1
                else:
                    break

                
                    
        print("### Ket qua cac Places: ", end ='')
        self.printMarking('result')

    # Ham tao file anh ve PetriNet
    def export(self, file_name):
        PeTriGraph = graphviz.Digraph(name = file_name, format='png')
        for i in self.list_place:
            PeTriGraph.node(i.get_name(), i.get_name() + ": "+str(i.get_token()))
        for i in self.list_transition:
            PeTriGraph.node(i.name, i.name, shape = 'square')
            for j in i.in_arc:
                PeTriGraph.edge(j.place.get_name(), i.name)
            for j in i.out_arc:
                PeTriGraph.edge(i.name, j.place.get_name())
        PeTriGraph.render()

def count(ps, list_place, arr1, arr2, arr3, int_size):  
    a = 0
    while(a != int_size):
        ps[a].token = list_place[a]
        a += 1
    print("## Ket qua cac place")
    for b in ps:
        b.print_place()

    ps1 = [0,0,0,0,0,0]
    ps2 = [0,0,0,0,0,0]
    ps3 = [0,0,0,0,0,0]
    int_d = 0
    int_m = 0
    int_n = 0
    i = 0
    while(i != int_size):
        ps1[i] = list_place[i] + arr1[i]
        if ps1[i] < 0:
            int_d = 0
            i += 1
            continue
        int_d += 1
        i += 1
    
    j = 0
    while(j != int_size):
        ps2[j] = list_place[j] + arr2[j]
        if ps2[j] < 0:
            int_m = 0
            j += 1
            continue
        int_m += 1
        j += 1

    k = 0
    while(k != int_size):
        ps3[k] = list_place[k] + arr3[k]
        if ps3[k] < 0:
            int_n = 0
            k += 1
            continue
        int_n += 1
        k += 1
        
    if int_m == int_size and int_n == int_size and int_d == int_size:
        return (count(ps,ps1,arr1,arr2,arr3,int_size) + count(ps,ps2,arr1,arr2,arr3,int_size) + count(ps,ps3,arr1,arr2,arr3,int_size) + 1)
    
    if int_m == int_size and int_n == int_size:
        return (count(ps,ps2,arr1,arr2,arr3,int_size) + count(ps,ps3,arr1,arr2,arr3,int_size) + 1)
    
    if int_n == int_size and int_d == int_size:
        return (count(ps,ps1,arr1,arr2,arr3,int_size) + count(ps,ps3,arr1,arr2,arr3,int_size) + 1)
    
    if int_m == int_size and int_d == int_size:
        return (count(ps,ps1,arr1,arr2,arr3,int_size) + count(ps,ps2,arr1,arr2,arr3,int_size) + 1)
    
    if int_d == int_size:
        return (count(ps,ps1,arr1,arr2,arr3,int_size) + 1)
    
    if int_m == int_size:   
        return (count(ps,ps2,arr1,arr2,arr3,int_size) + 1)
    
    if int_n == int_size:     
        return (count(ps,ps3,arr1,arr2,arr3,int_size) + 1)
    
    return 1

def input_34(): 
    print("Nhap luong nguoi o: ")
    while True:
        try:
            wait = int(input("wait: "))
            if wait < 0:
                print("Gia tri am, vui long nhap lai!")
                continue
            free = int(input("free: "))
            if free < 0:
                print("Gia tri am, vui long nhap lai!")
                continue
            busy = int(input("busy: "))
            if busy < 0:
                print("Gia tri am, vui long nhap lai!")
                continue
            inside = int(input("inside: "))
            if inside < 0:
                print("Gia tri am, vui long nhap lai!")
                continue
            done = int(input("done: "))
            if done < 0:
                print("Gia tri am, vui long nhap lai!")
                continue
            document = int(input("document: "))
            if document < 0:
                print("Gia tri am, vui long nhap lai!")
                continue
            break
        except ValueError:
            print("Gia tri khong hop le! Vui long nhap lai...")
    return wait,free, busy, inside, done, document







