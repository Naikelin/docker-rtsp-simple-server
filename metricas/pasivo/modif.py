# Esta funcion se aplica al codigo fuente de polymorph en packets.py
def xdd(self, name, default):
        try:
            setattr(self, name, eval("self." + str(name)) + [default[0], default[1], default[1] - eval("self." + str(name))[len(eval("self." + str(name)))-2]])
        except:
            setattr(self, name, [default[0], default[1], 0])
        print(eval("self." + str(name)))
