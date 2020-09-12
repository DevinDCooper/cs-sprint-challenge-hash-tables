#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    map = {}
    for ticket in tickets:
        map[ticket.source] = ticket.destination

    route = []
    start = "NONE"
    end = None
    while end is not "None":
        end = map.get(start)
        route.append(end)
        start = end

    return route
