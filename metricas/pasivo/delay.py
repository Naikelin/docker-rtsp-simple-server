# Esta funcion se aplica al intercept de polymorph
def test(packet):

    # your code here
    import time
    packet.xdd('datos', [packet['RTP']['seq'], time.time()])
    print('-------------------------------------------------------------------------')
    # If the condition is meet
    return packet
