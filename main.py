# python3
import math

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class PhoneBook:
    def __init__(self):
        self.buckets = [[] for _ in range(8)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(str(s)):
            ans = (ans * 0.6 + ord(c)) % 10000003
        return math.floor(ans % 8)
    
    def add(self, cur_query):
        string = cur_query.number
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i in bucket:
            if i.number == cur_query.number:
                i.name = cur_query.name
                return
        self.buckets[hashed] = [cur_query] + bucket
        return

    def delete(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i, k in enumerate(bucket):
            if k.number == string:
                bucket.pop(i)
                break
        return

    def find(self, string):
        hashed = self._hash_func(string)
        for i in self.buckets[hashed]:
            if i.number == string:
                return i.name
        return "not found"

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    phonebook = PhoneBook()
    result = []
    for cur_query in queries:
        if cur_query.type == 'add':
            phonebook.add(cur_query)
        elif cur_query.type == 'del':
            phonebook.delete(cur_query.number)
        elif cur_query.type == 'find':
            response = phonebook.find(cur_query.number)
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))