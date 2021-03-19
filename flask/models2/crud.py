from model import db, Person
from datetime import datetime

man1 = Person(
    'Taro',
    '090-2222-2222',
    21,
    datetime.now(),
    datetime.now()
)

man2 = Person(
    'Jiro',
    '080-2222-2222',
    19,
    datetime.now(),
    datetime.now()
)

man3 = Person(
    'Saburo',
    '080-3333-3333',
    16,
    datetime.now(),
    datetime.now()
)

# db.session.add_all([man1, man2, man3])
# db.session.commit()

# print(Person.query.get(1)) # 主キー
# print(Person.query.first())

# for x in Person.query.filter_by(name='Mike').all():
#     print(x.name)

# for x in Person.query.filter(Person.name.endswith('o')):
#     print(x.name)

# id=1を削除
# Person.query.filter_by(id=1).delete()
# db.session.commit()

Person.query.filter_by(name='nanashi').update(
    {
        'name': 'John',
        'update_at': datetime.now()
    }
)

db.session.commit()