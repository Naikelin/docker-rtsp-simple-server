def changeMessage(packet):
    if(packet["TCP"]["dstport"] == 8554 and packet["TCP"]["payload"]):
        try:
            payload = packet["TCP"]["payload"].decode()
            splitted = payload.split("\r\n")
            for i in range (len(splitted)):
                if "PLAY" in splitted[i]:
                    splitted[i] += "               "
            payload = "\r\n".join(splitted)
            packet["TCP"]["payload"] = payload.encode()
            print('sending ', packet["TCP"]["payload"])
        except:
            print("cant decode packet")
    return packet