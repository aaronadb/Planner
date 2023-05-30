from ics import Calendar
def icaltojson(filename):
    file=open(filename)
    cal=Calendar(file.read())
    events=list(cal.events)
    return events


