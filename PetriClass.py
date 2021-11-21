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
    def run(self):
        while True:
            Execute = any(trans.Can_fire() for trans in self.list_transition)
            if not Execute:
                break
            for trans in self.list_transition:
                if trans.Can_fire():
                    trans.fire()
        print("### Ket qua cac Places:")
        for i in self.list_place:
            i.print_place()
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
    








