import sipfullproxy
import logging
import time


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=logging.INFO,datefmt='%H:%M:%S')
logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))

hostname = sipfullproxy.socket.gethostname()

ipaddress = "192.168.0.80"
sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress,sipfullproxy.PORT)
sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,sipfullproxy.PORT)
server = sipfullproxy.SocketServer.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
server.serve_forever()
