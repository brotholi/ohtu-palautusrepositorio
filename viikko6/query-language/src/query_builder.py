from matchers import *

class QueryBuilder:
    def __init__(self):
        self.query = All()

    def build(self):
        return self.query
    
    def playsIn(self, team):
        self.query = And(self.query, PlaysIn(team))
        return self
    
    def hasAtLeast(self, value, attr):
        self.query = And(self.query, HasAtLeast(value, attr))
        return self
    
    def hasFewerThan(self, value, attr):
        self.query = And(self.query, HasFewerThan(value, attr))
        return self
    
    def oneOf(self, *matchers):
        for matcher in matchers:
            self.query = Or(self.query, matcher)
        return self
        