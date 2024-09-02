calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(a: str):
    tuple1 = (len(a), a.upper(), a.lower())
    count_calls()
    return tuple1


def is_contains(a: str, b: list):
    for line in b:
        if line == a:
            return True
    count_calls()
    return False


line = input("Введите строку: ")
print(string_info(line))
line1 = input("Введите ещё строку: ")
line2 = input("И ещё одну: ")
line3 = input("И последнюю: ")
list_1 = [line1, line2, line3]
print(is_contains(line, list_1))
print(calls)