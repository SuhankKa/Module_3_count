# "Счётчик вызовов"

calls = 0

def count_calls():
    global calls
    calls += 1
    return calls
        
def string_info(string):
    count_calls()
    a = len(string)
    b = string.upper()
    c = string.lower()
    d = tuple([a, b, c])
    return d    
    
def is_contains(string, list_to_search):
    count_calls()
    a = string.upper()
    b = "".join(list_to_search)
    c = b.upper()
    d = a in c
    return d

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)

