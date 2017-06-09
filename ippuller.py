#!/usr/bin/env python3
"""
This is designed to pull your external IP address. It is based on phoemur/ipgetter but uses requests instead of urllib.
I'm mainly designing this module as a practically means of differentiating between requests and urllib.

"""
import re
import random
import requests

__version__ = "0.1"

def myip():
    return IPpuller().get_external_ip()

class IPpuller():
    """ This class is designed to fetch your external IP address from one of the
    listed sites in the server list below."""

    def __init__(self):
        self.server_list = ['http://ip.dnsexit.com',
                            'http://ifconfig.me/ip',
                            'http://echoip.com',
                            'http://checkip.dyndns.org/plain',
                            'http://ipogre.com/linux.php',
                            'http://whatismyipaddress.com/WhatIsMyIp',
                            'http://getmyipaddress.org/',
                            'http://www.my-ip-address.net/',
                            'http://myexternalip.com/raw',
                            'http://www.canyouseeme.org/',
                            'http://www.trackip.net/',
                            'http://icanhazip.com/',
                            'http://www.iplocation.net/',
                            'http://www.howtofindmyipaddress.com/',
                            'http://www.ipchicken.com/',
                            'http://whatsmyip.net/']

    def get_external_ip(self):
        """
        This function getsyour IP from a random server
        """

        myip = ''
        for i in range(7):
            myip = self.fetch(random.choice(self.server_list))
            if myip != '':
                return myip
            else:
                continue
        return ''

    def fetch(self, server):
        """
        This function gets your IP from a specific server.
        """
        url = None
        opener = requests.get(server)
        content = opener.text

        ip_finder = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',
                content)

        myip = ip_finder.group(0)
        return myip if len(myip) > 0 else ''

if __name__ == '__main__':
    print(myip())
