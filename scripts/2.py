def changeReplyOptions(packet):
    if(packet["TCP"]["srcport"] == 8554 and packet["TCP"]["payload"]):
        try:
            payload = packet["TCP"]["payload"].decode()
            splitted = payload.split("\r\n")
            for i in range (len(splitted)):
                if "Public" in splitted[i]:
                    splitted[i] = 'Public: '
            payload = "\r\n".join(splitted)
            packet["TCP"]["payload"] = payload.encode()
            print('sending ', packet["TCP"]["payload"])
        except:
            print("cant decode packet")
    return packet