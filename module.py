#!/usr/bin/python

"""
IwTools
  author: Wander Domingos (wandervilhalvadomingos@gmail.com)

"""

from subprocess import Popen, PIPE
import re

VERSION = "0.1"

class iwtools(object):

    
    @classmethod
    def interface_json(cls, *args):
        """Função para coletar informações do Access Point especifico e retorna em formato JSON"""

        cmd = f"iw dev {args[0]} info"
        txt = Popen(cmd, shell=True, stdout=PIPE).communicate()[0].decode()
        
        regex = re.compile("Interface\s([\w_-]+)[\S\s]*ifindex\s([\d]+)[\S\s]*wdev\s([\w-]+)[\S\s]*addr\s([\w:-]+)[\S\s]*ssid\s([\w_-]+)[\S\s]*type\s([\w]+)[\S\s]*wiphy\s([\d]+)[\S\s]*channel\s([\d]+)[\S\s]*width:\s([\d]+)[\S\s]*center1:\s([\d]+)[\S\s]*txpower\s([\d]+)")

        return regex.findall(txt)
        

    @classmethod
    def get_ap_json(cls, ap):
        """Get informações do Access Point"""
        return cls.interface_json(ap)



    @classmethod
    def station_json(cls, args):
        """Função para coletar informações de uma Station especifica e retorna em formato JSON"""
        
        cmd = f"iw dev {args[0]} station get {args[1]}"
                
        txt = Popen(cmd, shell=True, stdout=PIPE).communicate()[0].decode()
        txt_new = txt.replace('\n\t',' ').replace('\t',' ').replace('\n',' ')
        
        regex = re.compile("Station\s([\w:-]+)[\S\s]*\(on\s([\w-]+)[\S\s]*inactive\stime:\s([\d]+)[\S\s]*rx\sbytes:\s([\d]+)[\S\s]*rx\spackets:\s([\d]+)[\S\s]*tx\sbytes:\s([\d]+)[\S\s]*tx\spackets:\s([\d]+)[\S\s]*tx\sretries:\s([\d]+)[\S\s]*tx\sfailed:\s([\d]+)[\S\s]*rx\sdrop\smisc:\s([\d]+)[\S\s]*signal:\s\s\s([\d-]+)[\S\s]*signal\savg:\s([\d-]+)[\S\s]*tx\sbitrate:\s([\d.]+)[\S\s]*tx\sduration:\s([\d]+)[\S\s]*rx\sbitrate:\s([\d.]+)[\S\s]*rx\sduration:\s([\d]+)[\S\s]*authorized:\s([\w]+)[\S\s]*authenticated:\s([\w]+)[\S\s]*associated:\s([\w]+)[\S\s]*preamble:\s([\w]+)[\S\s]*WMM/WME:\s([\w]+)[\S\s]*MFP:\s\s([\w]+)[\S\s]*TDLS\speer:\s([\w]+)[\S\s]*DTIM\speriod:\s([\d]+)[\S\s]*beacon\sinterval:([\d]+)[\S\s]*short\sslot\stime:([\w]+)[\S\s]*connected\stime:\s([\d]+)[\S\s]*boottime]:\s([\d.]+)[\S\s]*associated\sat:\s([\d]+)[\S\s]*current\stime:\s([\d]+)[\S\s]")
        
        return regex.findall(txt_new)
        

    @classmethod
    def get_sta_json(cls, args):
        """Get informações do Station"""
        #print(args)
        return cls.station_json(args)   


    @classmethod
    def station_get(cls, *args):
        """Station Get"""
        cmd = f"iw dev {args[2]} station get {args[3]} | egrep {args[0]} {args[1]}"
        return Popen(cmd, shell=True, stdout=PIPE).communicate()[0].decode().split("\n")[0]

    @classmethod
    def station_list(cls, *args):
        """Funcao para listar todos os MAC conectados"""
        cmd = f"iw dev {args[2]} station dump | egrep {args[0]} {args[1]}"
        return Popen(cmd, shell=True, stdout=PIPE).communicate()[0].decode().split("\n")

    @classmethod
    def station_dump(cls, *args):
        """Command line Station Dump"""
        cmd = f"iw dev {args[2]} station dump | egrep {args[0]} {args[1]}"
        return Popen(cmd, shell=True, stdout=PIPE).communicate()[0].decode().split("\n")[0]

    @classmethod
    def interface_dump(cls, *args):
        """Command line Interface dump"""
        cmd = f"iw dev | grep {args[0]} {args[1]}"
        return Popen(cmd, shell=True, stdout=PIPE).communicate()[0].decode().split("\n")

    @classmethod
    def list_sta(cls, ap):
        """Imprime o MAC da Station conectada no AP"""
        return cls.station_list("'Station'", " | awk '{print $2}'", ap)

    @classmethod
    def get_inactive(cls, args):
        """Imprime o tempo Inativo de cada Station conectada no AP"""
        return cls.station_get("'inactive time:'", " | awk '{print $3}'", args[0], args[1])

    @classmethod
    def get_rxbytes(cls, args):
        """Imprime o RX bytes da Station conectada no AP"""
        return cls.station_get("'rx bytes:'", " | awk '{print $3}'", args[0], args[1])

    @classmethod
    def get_txbytes(cls, args):
        """Imprime o TX bytes da Station conectada no AP"""
        return cls.station_get("'tx bytes:'", " | awk '{print $3}'", args[0], args[1])

    @classmethod
    def get_rxpackets(cls, args):
        """Imprime o RX packets da Station conectada no AP"""
        return cls.station_get("'rx packets:'", " | awk '{print $3}'", args[0], args[1])

    @classmethod
    def get_txpackets(cls, args):
        """Imprime o TX Packets da Station conectada no AP"""
        return cls.station_get("'tx packets:'", " | awk '{print $3}'", args[0], args[1])

    @classmethod
    def get_txretries(cls, args):
        """Imprime o TX Retries da Station conectada no AP"""
        return cls.station_get("'tx retries:'", " | awk '{print $3}'", args[0], args[1])

    @classmethod
    def get_txfailed(cls, args):
        """Imprime o TX Failed da Station conectada no AP"""
        return cls.station_get("'tx failed:'", " | awk '{print $3}'", args[0], args[1])

    @classmethod
    def get_rxdrop(cls, args):
        """Imprime o RX Drop Misc da Station conectada no AP"""
        return cls.station_get(
            "'rx drop misc:'", " | awk '{print $4}'", args[0], args[1]
        )

    @classmethod
    def get_rssi(cls, args):
        """Imprime o RSSI da Station conectada no AP"""
        return cls.station_get("'signal:'", " | awk '{print $2}'", args[0], args[1])

    @classmethod
    def get_rssi_avg(cls, args):
        """Imprime o RSSI-AVG da Station conectada no AP"""
        return cls.station_get("'signal avg:'", " | awk '{print $3}'", args[0], args[1])

    @classmethod
    def get_txbitrate(cls, args):
        """Imprime o TX Bitrate da Station conectada no AP"""
        return cls.station_get("'tx bitrate:'", " | awk '{print $3}'", args[0], args[1])

    @classmethod
    def get_txduration(cls, args):
        """Imprime o TX Duration da Station conectada no AP"""
        return cls.station_get(
            "'tx duration:'", " | awk '{print $3}'", args[0], args[1]
        )

    @classmethod
    def get_rxduration(cls, args):
        """Imprime o RX Duration da Station conectada no AP"""
        return cls.station_get(
            "'rx duration:'", " | awk '{print $3}'", args[0], args[1]
        )

    @classmethod
    def get_dtim(cls, args):
        """Imprime o DTIM period da Station conectada no AP"""
        return cls.station_get(
            "'DTIM period:'", " | awk '{print $3}'", args[0], args[1]
        )

    @classmethod
    def get_beacon(cls, args):
        """Imprime o Beacon Interval da Station conectada no AP"""
        return cls.station_get(
            "'beacon interval:'",
            " | sed -e 's/interval://' | awk '{print $2}'",
            args[0],
            args[1],
        )

    @classmethod
    def get_connected(cls, args):
        """Imprime o Connected Time da Station conectada no AP"""
        return cls.station_get(
            "'connected time:'", " | awk '{print $3}'", args[0], args[1]
        )

    @classmethod
    def get_boottime(cls, args):
        """Imprime o Boottime da Station conectada no AP"""
        return cls.station_get("'[boottime]:'", " | awk '{print $3}'", args[0], args[1])

    @classmethod
    def get_associated(cls, args):
        """Imprime o tempo Associado da Station conectada no AP"""
        return cls.station_get(
            "'associated at:'", " | awk '{print $3}'", args[0], args[1]
        )

    @classmethod
    def get_current(cls, args):
        """Imprime o tempo Atual da Station conectada no AP"""
        return cls.station_get(
            "'current time:'", " | awk '{print $3}'", args[0], args[1]
        )

    @classmethod
    def list_ap(cls):
        """Lista todos os Access Points conectados na rede"""
        return cls.interface_dump("'Interface'", ' | cut -f 2 -s -d" " ')

    @classmethod
    def interface_info(cls, *args):
        """Command line Interface Info"""
        # print(f'arg0 = {args[0]}, arg1 = {args[1]}, arg2 = {args[2]}')
        cmd = f"iw dev {args[2]} info | egrep {args[0]} {args[1]}"
        return Popen(cmd, shell=True, stdout=PIPE).communicate()[0].decode().split("\n")[0]

    @classmethod
    def get_ap_mac(cls, ap):
        """Imprime o MAC do Access Point"""
        return cls.interface_info("'addr'", " | awk '{print $2}'", ap)

    @classmethod
    def get_ap_ssid(cls, ap):
        """Imprime o SSID do Access Point"""
        return cls.interface_info("'ssid'", " | awk '{print $2}'", ap)

    @classmethod
    def get_ap_channel(cls, ap):
        """Imprime o Channel do Access Point"""
        return cls.interface_info("'channel'", " | awk '{print $2}'", ap)

    @classmethod
    def get_ap_freq(cls, ap):
        """Imprime a Frequencia do Access Point"""
        return cls.interface_info(
            "'channel'", " | sed -e 's/(//' | awk '{print $3}'", ap
        )

    @classmethod
    def get_ap_txpower(cls, ap):
        """Imprime o TxPower do Access Point"""
        return cls.interface_info(
            "'txpower'", " | sed -e 's/dBm//' | awk '{print $2}'", ap
        )
