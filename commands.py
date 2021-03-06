from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")


@db_commands.cli.command("seed")
def seed_db():
    
    from models.Suggestion import Suggestion
    from models.User import User
    from models.Kanji import Kanji
    from main import bcrypt
    from faker import Faker
    import random

    faker = Faker(['en_US','ja_JP'])
    users = []

    for i in range(5):
        user = User()
        user.username = f"user{i}"
        user.email = f"test{i}@test.com"
        user.image_file = "/static/images/netflix_logo.png"
        user.password = bcrypt.generate_password_hash("123456").decode("utf-8")
        db.session.add(user)
        users.append(user)

    db.session.commit()

    for i in range(20):    
        suggestion=Suggestion()
        suggestion.title = faker.catch_phrase()
        suggestion.user_id = random.choice(users).id
        suggestion.genre = faker.name()
        suggestion.content = faker.name()
        suggestion.date_created = faker.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
        db.session.add(suggestion)

    db.session.commit()
    
    for i in range(20):    
        kanji=Kanji()
        kanji.id = f"{i}"
        kanji.character = faker.word()
        kanji.meaning = faker.word()
        kanji.onyomi = faker.word()
        kanji.kunyomi = faker.word()

    db.session.commit()
    
    
    
    
    print("Tables seeded")
