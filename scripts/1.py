def printPackets(packet):
    if(packet["TCP"]["dstport"] == 8554 and packet["TCP"]["payload"]):
        try:
            payload = (packet["TCP"]["payload"]).decode()
            splitted = payload.split("\r\n")
            for i in range(len(splitted)):
                if "CSeq" in splitted[i]:
                    import random
                    splitted[i] = "CSeq: " + str(random.randint(0,999))
    
            payload = "\r\n".join(splitted)
            print(payload.encode())
            packet["TCP"]["payload"] = payload.encode()
        except:
            print("cant decode packet")
    return packet