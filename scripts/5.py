def protoConfusion(packet):
  try:
    from re import search

    info = packet["TCP"]["payload"].decode()
    if search("^SETUP", info):
      packet["TCP"]["payload"] = info.replace("UDP","TCP").encode()

    if search("CSeq: 3", info):
      packet["TCP"]["payload"] = info.replace("TCP","").encode()

    return packet
  except:
    print("X")
    return None