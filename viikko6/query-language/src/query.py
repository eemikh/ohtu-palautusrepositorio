from matchers import All, And, HasAtLeast, HasFewerThan, Or, PlaysIn

class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matcher = matcher

    def plays_in(self, team):
        return QueryBuilder(matcher=And(self._matcher, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(matcher=And(self._matcher, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(matcher=And(self._matcher, HasFewerThan(value, attr)))

    def one_of(self, *builders):
        return QueryBuilder(matcher=Or(*[builder._matcher for builder in builders]))

    def build(self):
        return self._matcher
