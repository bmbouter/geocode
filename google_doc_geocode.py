import gdata.spreadsheet.service
from geocode import geocode

key = 'tM8UdRPe-6209NB-Hsx24rw'

client = gdata.spreadsheet.service.SpreadsheetsService(source='yourCompany-YourAppName-v1')
client.ClientLogin('username@gmail.com', 'password')
list_feed = client.GetListFeed(key,'1')

f = open('not_geocoded.txt', 'a')
for i, entry in enumerate(list_feed.entry):
    address = entry.custom['address'].text
    if entry.custom['latitude'].text is None and entry.custom['longitude'].text is None:
        print 'geocoding: %s' % address
        try:
            lat, lng = geocode(address)
        except Exception as E:
            import pdb;pdb.set_trace()
            print 'EXCEPTION CAUGHT ... WRITING TO FILE'
            f.write(address)
            continue
        print 'results = %s, %s' % (lat, lng)
        client.UpdateCell(i+2, 2, str(lat), key)
        client.UpdateCell(i+2, 3, str(lng), key)
    else:
        print 'skipping address: %s' % address
f.close()
