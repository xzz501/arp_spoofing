
from scipy.all import *
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

