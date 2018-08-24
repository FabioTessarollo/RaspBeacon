from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Dispositivo rilevato", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)


def calcolaDistanza(rssi):
    int
    txpower = -59
    if rssi == 0:
        return -1
    else:
        ratio = rssi / txpower
        if ratio < 1:
            return ratio ** 10
        else:
            return 0.89976 * ratio ** 7.7095 + 0.111

for dev in devices:
    print "Dispositivo %s (%s), RSSI=%d dB, Distanza=%d m" % (dev.addr, dev.addrType, dev.rssi, calcolaDistanza(dev.rssi))
    for (adtype, desc, value) in dev.getScanData():
        print "  %s = %s" % (desc, value)