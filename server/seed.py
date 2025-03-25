#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from datetime import datetime, timedelta

from models import db, User, Plant, Category, CareNote

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        db.drop_all()
        db.create_all()

        # Seed Users
        users = []
        for name in ["Lunaxx", "Darya", "Pardis"]:
            user = User(username=name, password_hash=fake.password())
            users.append(user)
            db.session.add(user)
        db.session.commit()

        # Seed Categories
        category_names = ["Succulents", "Ferns", "Flowering Plants", "Herbs"]
        categories = []
        for name in category_names:
            category = Category(category_name=name)
            categories.append(category)
            db.session.add(category)
        db.session.commit()

        # Seed Plants
        plants = []
        for user in users:
            for _ in range(4):
                category = rc(categories)
                plant = Plant(
                    plant_name=fake.word().capitalize(),
                    image=fake.image_url(),
                    created_at=fake.date_this_decade(),
                    user_id=user.id,
                    category_id=category.id
                )
                plants.append(plant)
                db.session.add(plant)
        db.session.commit()

        # Seed CareNotes
        care_types = ["Watering", "Fertilizing", "Pruning", "Repotting"]
        for plant in plants:
            for _ in range(3):
                care_note = CareNote(
                    care_type=rc(care_types),
                    frequency=randint(3, 14),
                    starting_date=datetime.utcnow(),
                    next_care_date=datetime.utcnow() + timedelta(days=randint(3, 14)),
                    custom_interval=randint(7, 30),
                    plant_id=plant.id
                )
                db.session.add(care_note)
        db.session.commit()

        print("Seeding complete!")
