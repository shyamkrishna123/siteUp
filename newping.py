import os
import subprocess

def ping_return_code(hostname):
    """Use the ping utility to attempt to reach the host. We send 5 packets
    ('-c 5') and wait 3 milliseconds ('-W 3') for a response. The function
    returns the return code from the ping utility.
    """
    ret_code = subprocess.call(['ping', '-c', '1', '-W', '3', hostname],
                               stdout=open(os.devnull, 'w'),
                               stderr=open(os.devnull, 'w'))
    return ret_code

def verify_hosts(host_list):
    """For each hostname in the list, attempt to reach it using ping. Returns a
    dict in which the keys are the hostnames, and the values are the return
    codes from ping. Assumes that the hostnames are valid.
    """
    return_codes = dict()
    for hostname in host_list:
        return_codes[hostname] = ping_return_code(hostname)

    return return_codes

def main():
    hosts_to_test = [
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.1.1'
    ]
    print verify_hosts(hosts_to_test)

if __name__ == '__main__':
    main()
