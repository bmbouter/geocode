import gdata.spreadsheet.service

client = gdata.spreadsheet.service.SpreadsheetsService(source='yourCompany-YourAppName-v1')
client.ClientLogin('username@gmail.com', 'password')
feed = client.GetListFeed('A7cDE67aA2nPdDJaY0g1eWxockhQwSM0RlNEM19uYVE','1')

for entry in feed.entry:
    for key in entry.custom:
        print key + ": " + entry.custom[key].text.__str__()
