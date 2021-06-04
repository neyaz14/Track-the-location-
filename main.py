import pygeoip

gip = pygeoip.GeoIP('GeoLiteCity.dat')
res = gip.record_by_addr("") # give a ip address here between the quotes

for key, val in res.items():
    print('%s : %s' % (key, val))
