# ippuller
This module is based off[phoemur/ipgetter](https://github.com/phoemur/ipgetter) module. However instead of using urllib and/or urllib2 this module uses requests. In future speed of ippuller will be tested against ipgetter to see if any advantages are conferred when we use urllib/urllib2 over requests. 

# API Usage
```
>>> import ippuller
>>> myip = ippuller.myip()
>>> myip
>>> '0.0.0.0'
```
