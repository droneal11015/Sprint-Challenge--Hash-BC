#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    current_index = 0

    for item in tickets:
      if item.source is "NONE":
        route[0] = item.destination
      hash_table_insert(ht, item.source, item.destination)

    while route[current_index] is not "NONE":
      route[current_index + 1] = hash_table_retrieve(ht, route[current_index])
      current_index += 1

    """
    YOUR CODE HERE
    """

    return route
