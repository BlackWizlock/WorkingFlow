n = int(input())
scopes = {'global': {'funcs': [], 'vars': []}}


def add(place, current_namespace, what):
    if current_namespace not in place:
        place[current_namespace] = {}
        place[current_namespace]['vars'] = []
        place[current_namespace]['vars'].append(what)
    else:
        if 'vars' not in place[current_namespace]:
            place[current_namespace]['vars'] = []
            place[current_namespace]['vars'].append(what)
        else:
            place[current_namespace]['vars'].append(what)


def create(place, current_namespace, parent_namespace):
    if current_namespace not in place:
        place[current_namespace] = {}
        place[current_namespace]['funcs'] = []
        place[current_namespace]['vars'] = []
        place[parent_namespace]['funcs'].append(current_namespace)
        place[current_namespace]['parent'] = parent_namespace
    else:
        if 'funcs' not in place[current_namespace]:
            place[current_namespace]['funcs'] = []
            place[current_namespace]['parent'] = parent_namespace
            place[parent_namespace]['funcs'].append(current_namespace)
        else:
            place[current_namespace]['funcs'].append(current_namespace)
            place[parent_namespace]['funcs'].append(current_namespace)


def search(place, namespace, what):
    if what in place[namespace]['vars']:
        return namespace
    else:
        try:
            upper_namespace = place[namespace]['parent']
        except KeyError:
            return None
        return search(place, upper_namespace, what)


for i in range(n):
    command = input().split()
    if command[0] == 'add':
        add(scopes, command[1], command[2])
    elif command[0] == 'create':
        create(scopes, command[1], command[2])
    elif command[0] == 'get':
        print(search(scopes, command[1], command[2]))
