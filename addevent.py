from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import date
from color import getcolorId

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

dateToday = date.today()
GMT_OFF = '-07:00'      # PDT/MST/GMT-7


def addEvent (title, date, description):
    EVENT = {
        'summary': '%s' %title,
        'description': '%s' %description,
        'start':  {'date': '%s'%date},
        'end':    {'date': '%s'%date},
        'colorId': '%s' %getcolorId()
    }

    e = GCAL.events().insert(calendarId='primary',
            sendNotifications=True, body=EVENT).execute()

    #print('''*** %r event added:
    #    Start: %s
    #    End:   %s''' % (e['summary'].encode('utf-8'),
    #        #e['start']['dateTime'], e['end']['dateTime']))
    #        e['start'], e['end']))
