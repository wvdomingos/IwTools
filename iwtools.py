#!/usr/bin/python

"""
IwTools
  author: Wander Domingos (wandervilhalvadomingos@gmail.com)

To see options:
  sudo iwtools -h

Example:
  iwtools <COMMAND> -i <AP> -c <MAC>

Listas de Comandos:
 
  Comandos para coletar informacoes do Access Point:
    --list-ap
    --get-ap-mac     -i <AP>
    --get-ap-ssid    -i <AP>
    --get-ap-channel -i <AP>
    --get-ap-freq    -i <AP>
    --get-ap-txpower -i <AP>
    --get-ap-json    -i <AP>

  Comandos para coletar informacoes das Station:
    --list-sta       -i <AP> -c <MAC>
    --get-inactive   -i <AP> -c <MAC>
    --get-rxbytes    -i <AP> -c <MAC>
    --get-rxpackets  -i <AP> -c <MAC> 
    --get-txbytes    -i <AP> -c <MAC>
    --get-txpackets  -i <AP> -c <MAC> 
    --get-txretries  -i <AP> -c <MAC> 
    --get-txfailed   -i <AP> -c <MAC>
    --get-rxdrop     -i <AP> -c <MAC>
    --get-rssi       -i <AP> -c <MAC>
    --get-rssi-avg   -i <AP> -c <MAC>
    --get-txbitrate  -i <AP> -c <MAC> 
    --get-txduration -i <AP> -c <MAC>  
    --get-rxduration -i <AP> -c <MAC>  
    --get-dtim       -i <AP> -c <MAC>
    --get-beacon     -i <AP> -c <MAC>
    --get-connected  -i <AP> -c <MAC> 
    --get-boottime   -i <AP> -c <MAC> 
    --get-associated -i <AP> -c <MAC>  
    --get-current    -i <AP> -c <MAC> 
    --get-sta-json   -i <AP> -c <MAC>   
"""

import sys
import getopt
from module import iwtools
import json

# --------- Main
def main():
    
    argv = sys.argv[1:]

    try:
        getopt.getopt(
            argv,
            "hi:c:",
            [
                "help",
                "list-sta=",
                "get-inactive=",
                "get-rxbytes=",
                "get-rxpackets=",
                "get-txbytes=",
                "get-txpackets=",
                "get-txretries=",
                "get-txfailed=",
                "get-rxdrop=",
                "get-rssi=",
                "get-rssi-avg=",
                "get-txbitrate=",
                "get-txduration=",
                "get-rxduration=",
                "get-dtim=",
                "get-beacon=",
                "get-connected=",
                "get-boottime=",
                "get-associated=",
                "get-current=",
                "list-ap",
                "get-ap-mac=",
                "get-ap-ssid=",
                "get-ap-channel=",
                "get-ap-freq=",
                "get-ap-txpower=",
                "get-ap-json=",
                "get-sta-json="
            ],
        )

    except getopt.GetoptError:
        raise SystemExit(f"Ops! Algo deu errado, favor consulte a documentação com o comando: iwtools --help")
        

    if len(sys.argv[1:]) == 0:
        raise SystemExit(f"Ops! Algo deu errado, favor consulte a documentação com o comando: iwtools --help")

    elif len(sys.argv) == 4:
        ap = sys.argv[3]

    elif len(sys.argv) == 6:
        ap = sys.argv[3]
        mac = sys.argv[5]
        ap_mac = [sys.argv[3], sys.argv[5]]
    
    if sys.argv[1] in ("-h", "--help"):
        help(iwtools)
        sys.exit()

    elif sys.argv[1] == "--list-sta":
        # Lista os MAC das Station conectadas no AP
        print("Entrei aqui")
        mac = iwtools.list_sta(ap)
        r = f"AP\tMAC\n"
        if len(mac) != 1:
            for m in range(len(mac) - 1):
                r += f"{ap}\t{mac[m]}\n"
            print(r)
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-inactive":
        # Imprime o tempo Inativo de cada Station conectada no AP
        x = iwtools.get_inactive(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tInactive(ms)\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-rxbytes":
        # Imprime o RX bytes da Station conectada no AP
        x = iwtools.get_rxbytes(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tRX bytes\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-rxpackets":
        # Imprime o RX packets da Station conectada no AP
        x = iwtools.get_rxpackets(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tRX Packets\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-txbytes":
        # Imprime o TX bytes da Station conectada no AP
        x = iwtools.get_txbytes(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tTX bytes\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-txpackets":
        # Imprime o TX Packets da Station conectada no AP
        x = iwtools.get_txpackets(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tTX Packets\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-txretries":
        # Imprime o TX Packets da Station conectada no AP
        x = iwtools.get_txretries(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tTX Retries\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-txfailed":
        # Imprime o TX Packets da Station conectada no AP
        x = iwtools.get_txfailed(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tTX Failed\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-rxdrop":
        # Imprime o TX Packets da Station conectada no AP
        x = iwtools.get_rxdrop(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tRX Drop\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-rssi":
        # Imprime o RSSI da Station conectada no AP
        x = iwtools.get_rssi(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tRSSI(dBm)\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-rssi-avg":
        # Imprime o RSSI da Station conectada no AP
        x = iwtools.get_rssi_avg(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tRSSI-AVG(dBm)\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-txbitrate":
        # Imprime o RSSI da Station conectada no AP
        x = iwtools.get_txbitrate(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tTX Bitrate(MBit/s)\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-txduration":
        # Imprime o RSSI da Station conectada no AP
        x = iwtools.get_txduration(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tTX Duration(us)\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-rxduration":
        # Imprime o RSSI da Station conectada no AP
        x = iwtools.get_rxduration(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tRX Duration(us)\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-dtim":
        # Imprime o RSSI da Station conectada no AP
        x = iwtools.get_dtim(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tDTIM\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-beacon":
        # Imprime o RSSI da Station conectada no AP
        x = iwtools.get_beacon(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tBeacon\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-connected":
        # Imprime o RSSI da Station conectada no AP
        x = iwtools.get_connected(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tConnected(seconds)\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-boottime":
        # Imprime o tempo conectado da Station conectada no AP
        x = iwtools.get_boottime(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tBoottime(s)\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-associated":
        # Imprime o tempo Associado da Station conectada no AP
        x = iwtools.get_associated(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tAssociated(ms)\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-current":
        # Imprime o tempo Atual da Station conectada no AP
        x = iwtools.get_current(ap_mac)
        if len(x) != 0:
            print(f"AP\tMAC\tCurrent(ms)\n{ap}\t{mac}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--list-ap":
        # Imprime a Interface conectadas na rede
        interface = iwtools.list_ap()
        if len(interface) != 1:
            r = f"AP\n"
            for i in range(len(interface) - 1):
                r += f"{interface[i]}\n"
            print(r)
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-ap-mac":
        # Imprime o MAC do Access Point
        x = iwtools.get_ap_mac(ap)
        if len(x) != 0:
            print(f"AP\tMAC\n{ap}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-ap-ssid":
        # Imprime o SSID do Access Point
        x = iwtools.get_ap_ssid(ap)
        if len(x) != 0:
            print(f"AP\tSSID\n{ap}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-ap-channel":
        # Imprime o Channel do Access Point
        x = iwtools.get_ap_channel(ap)
        if len(x) != 0:
            print(f"AP\tChannel\n{ap}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-ap-freq":
        # Imprime o Frequencia do Access Point
        x = iwtools.get_ap_freq(ap)
        if len(x) != 0:
            print(f"AP\tFrequence\n{ap}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-ap-txpower":
        # Imprime o TX Power do Access Point
        x = iwtools.get_ap_txpower(ap)
        if len(x) != 0:
            print(f"AP\tTX Power\n{ap}\t{x}\n")
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-ap-json":
        # Imprime as informações do AP em formato JSON
        result = iwtools.get_ap_json(ap)
        if len(result) != 0:
            dic_ap = {'Interface': result[0][0], 'ifindex': result[0][1], 'wdev': result[0][2], 
            'addr': result[0][3], 'ssid': result[0][4], 'type': result[0][5],
            'wiphy': result[0][6], 'channel': result[0][7], 'width': result[0][8],
            'center1': result[0][9], 'txpower': result[0][10]}


            with open('accesspoint.json', 'w') as file:
                json.dump(dic_ap, file)

            print("Arquivo accesspoint.json criado com sucesso...")
        
            sys.exit()
        else:
            sys.exit()

    elif sys.argv[1] == "--get-sta-json":
        # Imprime as informações do AP em formato JSON
        result = iwtools.get_sta_json(ap_mac)
        if len(result) != 0:
            dic_sta = {'MAC': result[0][0], 'Station': result[0][1], 'inactive time': result[0][2], 
                        'rx bytes': result[0][3], 'rx packets': result[0][4], 'tx bytes': result[0][5],
                        'tx packets': result[0][6], 'tx retries': result[0][7], 'tx failed': result[0][8],
                        'rx drop misc': result[0][9], 'RSSI': result[0][10], 'RSSI AVG': result[0][11], 
                        'tx bitrate': result[0][12], 'tx duration': result[0][13], 'rx bitrate': result[0][14],
                        'rx duration': result[0][15], 'authorized': result[0][16], 'authenticated': result[0][17], 
                        'associated': result[0][18], 'preamble:': result[0][19], 'WMM/WME:': result[0][20], 'MFP:': result[0][21],
                        'TDLS peer:': result[0][22], 'DTIM period:': result[0][23], 'beacon interval:': result[0][24],
                        'short slot time:': result[0][25], 'connected time:': result[0][26], 'boottime:': result[0][27],
                        'associated at:': result[0][28], 'current time:': result[0][29]}

            with open('station.json', 'w') as file:
                json.dump(dic_sta, file)

            print("Arquivo station.json criado com sucesso...")
        
            sys.exit()
        else:
            sys.exit()

if __name__ == "__main__":
    main()
