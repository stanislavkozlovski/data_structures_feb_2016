"""
Write a program that reads a set of events in format "Event name | Date and time"
and a series of date ranges a < b and prints for each range (a < b)
all events within the range [a … b] inclusively (ordered by date;
for duplicated dates preserve the order of appearance).

Examples
Input
5
C# Course – Group II | 15-Aug-2015 14:00
Data Structures Course | 13-Aug-2015 18:00
C# Course – Group I | 15-Aug-2015 10:00
Seminar for Java Developers | 18-Aug-2015 19:00
Game Development Seminar | 15-Aug-2015 10:00
2
15-Aug-2015 10:00 | 1-Sep-2015 0:00
13-Aug-2015 10:00 | 13-Aug-2015 20:00

Output
4
C# Course - Group I | 15-Aug-2015
Game Development Seminar | 15-Aug-2015
C# Course - Group II | 15-Aug-2015
Seminar for Java Developers | 18-Aug-2015
1
Data Structures Course | 13-Aug-2015 18:00

"""
from datetime import datetime
from sortedcontainers import SortedDict
import dateparser

def main():
    events = read_events(int(input()))  # type: SortedDict
    process_events_in_given_date(events, int(input()))


def process_events_in_given_date(events: SortedDict, events_count: int):
    """
    Reads each line of user input to get the events between the two dates
    """
    for _ in range(events_count):
        start_date, end_date = [dateparser.parse(part) for part in input().split('|')]
        print_events_between_dates(events, start_date, end_date)


def print_events_between_dates(events:SortedDict, start_date:datetime, end_date:datetime):
    date_keys_between_dates = events.irange(minimum=start_date, maximum=end_date, inclusive=(True, True))
    events = [(event, date_key) for date_key in date_keys_between_dates for event in events[date_key]]
    for event, date in events:
        print("{event} | {date}".format(event=event, date=date))


def read_events(events_count) -> SortedDict:
    """
    Save a SortedDictionary of type {
        key: DateTime object
        value: List of courses that will happen then
    }
    """
    events_dict = SortedDict()

    for _ in range(events_count):
        event, time_str = input().split('|')
        time = dateparser.parse(time_str)

        if time not in events_dict.keys():
            events_dict[time] = []
        events_dict[time].append(event)

    return events_dict


if __name__ == '__main__':
    main()