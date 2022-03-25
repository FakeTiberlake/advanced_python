people = [{'name': 'Andrei Petrov', 'position_id': 1},
          {'name': 'Sergei Ivanov', 'position_id': 2},
          {'name': 'Alex Smirnov', 'position_id': 3},
          {'name': 'Elena Semenova', 'position_id': 2},
          {'name': 'Maria Ostapenko', 'position_id': 4},
          {'name': 'Anna Pavlova', 'position_id': 1}]

positions = [{'id': 1, 'name': 'repairman', 'salary': 3000},
             {'id': 2, 'name': 'stripper', 'salary': 6000},
             {'id': 3, 'name': 'postman', 'salary': 10000},
             {'id': 4, 'name': 'sniper', 'salary': 7000}]


def get_employees():
    return [{'name': p['name'],
             'position': next(i['name'] for i in positions if i['id'] == p['position_id']),
             'id': p['position_id'],
             'salary': next(i['salary'] for i in positions if i['id'] == p['position_id'])} for p in people]