from f_app import app
from models import db, Pet

with app.app_context():
    db.create_all()
    pet1 = Pet(name='Костик', age='2 года', species='кот', breed='Сибирская голубая гладкошерстная')
    pet2 = Pet(name='Милка', age='3 года', species='пес', breed='Дворовая')
    pet3 = Pet(name='Макси', age='5 лет', species='пес', breed='Дворовая')
    pet4 = Pet(name='Тедди', age='2 месяца', species='кот', breed='Тайская')
    pet5 = Pet(name='Клео', age='5 лет', species='кот', breed='Дворовая')
    db.session.add_all([pet1, pet2, pet3, pet4, pet5])
    db.session.commit()