from matchers import *

class QueryBuilder:
    def __init__(self):
        self.query = All()
        self.matchers = []
        self.or_query = False

    def build(self):
        if self.or_query:
            self.query = Or(*self.matchers)
        else:
            self.query = All()
            for matcher in self.matchers:
                self.query = And(self.query, matcher)
        
        return self.query

    def playsIn(self, team):
        self.matchers.append(PlaysIn(team))
        return self
    
    def hasAtLeast(self, value, attr):
        self.matchers.append(HasAtLeast(value, attr))
        return self
    
    def hasFewerThan(self, value, attr):
        self.matchers.append(HasFewerThan(value, attr))
        return self
    
    def oneOf(self, *matchers):
        self.or_query = True
        self.matchers = matchers
        return self
        