# Powered By SkayZ

try:
    from pypresence import Presence
    import time

    client_id = input("ID: ")
    statee = input("STATE: ")
    detailss = input("DETAILS: ")
    large_imagee = input("LARGE IMAGE: ")
    large_textt = input("LARGE TEXT: ")
    smail_imagee = input("SMAIL IMAGE: ")
    joinn = input("JOIN: ")
    party_size_1 = int(input("PARTY SIZE MEMBERS: "))
    party_size_2 = int(input("PARTY MAX MEMBERS: "))
    party_idd = input("PARTY ID: ")

    RPC = Presence(client_id)

    RPC.connect()

    RPC.update(state=statee, details=detailss, large_image=large_imagee, start=time.time(), large_text=large_textt, small_image=smail_imagee, join=joinn, party_size=[party_size_1,party_size_2], party_id=party_idd, instance=True)

    while True:
        time.sleep(15)

except:
    print("An error has happened.")
