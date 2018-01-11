import sys

try:
    import urllib2 as urlreq # Python 2.x
except:
    import urllib.request as urlreq # Python 3.x
req = urlreq.Request("https://api.telegram.org/botXXXX/sendMessage?chat_id=XXXX&text="+sys.argv[1])

urlreq.urlopen(req).read()
