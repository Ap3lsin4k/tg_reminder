class NOTE:
    def __init__(self):
        self.some_group = {}
        print("constructor")
    def add_note(self):
        #якщо ми не пишемо self. то змінна буде локальною, і видалиться при завершенні функції
        self.time = {'year': None, 'month': None, 'day': None,
               'hour': None, 'minute': None}#delete
        print("Enter a note name")
        self.name_note = str(input())
        self.some_group[self.name_note] = {'time': None, 'description': None}
    
        print("Enter year, month, day")
        self.time['year'], self.time['month'], self.time['day'] = input().split()
    
    
        print("Enter time (hour, minute)")
        self.time['hour'], self.time['minute'] = input().split()
        self.some_group[self.name_note]['time'] = self.time
    
        print("Enter description")
        self.some_group[self.name_note]['description'] = input()
    def data_output(self):
        print("=========\n")
        # перебираємо всі ключі
        for name_note in self.some_group:
            print(name_note, "\ttime:", self.some_group[name_note]['time'],"\n",
                self.some_group[name_note]['description'], "\n")
            print()
work = NOTE()
home = NOTE()
group1 = NOTE()
"""
'work':
{
    'name':
    {
        'time':
        {
            'year': '2018',
            'month': '02',
            'day': '21',
            'hour': None,
            'minut': None
        },
        'description': None
    },
    'name2':
    {
        'time': {'year': '2018', 'month': '02', 'day': '21', 'hour': None, 'minut': None},
        'description': None
    }
    'name3':
    {
        'time': {'year': '2018', 'month': '02', 'day': '21', 'hour': None, 'minut': None},
        'description': None
    }
},
'home':
{
    'name':
    {
        'time': {...},
        'description': ...
    },
    'name2':
    {
        ...
    },
    '...':
    {
        ...
    },
    ...
}
"""
