
import scapy.all as sc
import optparse
def get_arguments():
    par=optparse.OptionParser()
    par.add_option("-t","--taget",dest="target_ip" ,help="target IP")
    par.add_option("-r", "--router", dest="getway_ip", help="getway  IP")
    opt=par.parse_args()
    if not opt.target_ip:
        par.error("[-] plese enter ip of target")
    if not opt.getwat_ip:
        par.error("[-] please enter ip of getway")
    return opt
opt=get_arguments()
def get_macaddress(ip):
    arp_requst=sc.ARP(pdst=ip)
    arp_broadcast=sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_requst_bro=arp_requst/arp_broadcast
    anw=sc.srp(arp_requst_bro,timeout=1,verbose=False)[0]
    return anw[0][1].hwsrc




