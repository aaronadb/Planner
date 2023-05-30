from ics import Calendar, Event
import arrow
from datetime import timedelta, datetime
def icaltojson(filename):
    file=open(filename)
    cal=Calendar(file.read())
    events=list(cal.events)
    return events

def assignEvent(events, event, grace=0):
    e_s=arrow.get(event.early_start_time)
    l_s=arrow.get(event.late_start_time)
    d=event.duration
    s=e_s
    for e in events:
        if e.begin<=s and (e.end+timedelta(minutes=grace))>=s:
            s=e.end+timedelta(minutes=grace)
            continue
        elif s<=e.begin and (s+timedelta(minutes=d+grace))>=e.begin:
            s=e.end+timedelta(minutes=grace)
            continue
    if s<l_s:
        return s
    else:
        return None

def addEvent(cal, event, s):
    e=Event()
    e.name=event.name
    e.begin=s
    e.end=s+timedelta(minutes=event.duration)
    cal.events.add(e)
    return cal