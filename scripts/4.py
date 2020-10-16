def slowMessages(packet):
  try:
    from time import sleep
    from random import randint

    if "RTSP" in packet["TCP"]["payload"].decode():
      print(packet["TCP"]["payload"])
      sleep(randint(30,180)
  except:
    pass

  return packet