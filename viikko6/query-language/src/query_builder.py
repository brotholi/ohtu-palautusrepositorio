from matchers import *

class QueryBuilder:
    def __init__(self, query = All()):
        self.query = query

    def build(self):
        return self.query
    
    def playsIn(self, team):
        query = QueryBuilder(And(self.query, PlaysIn(team)))
        return query
    
    def hasAtLeast(self, value, attr):
        query = QueryBuilder(And(self.query, HasAtLeast(value, attr)))
        return query
    
    def hasFewerThan(self, value, attr):
        query = QueryBuilder(And(self.query, HasFewerThan(value, attr)))
        return query
    
    def oneOf(self, m1, m2):
        query = QueryBuilder(Or(m1, m2))
        return query