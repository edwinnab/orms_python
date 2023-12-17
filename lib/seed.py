from product import Product
from faker import Faker
import random

fake = Faker()


if __name__ == "__main__":
    Product.clear_table()
    
    print("Seeding to the db!!!")
    
    for i in range(1, 51):
        Product.create(
            name = fake.name(),
            price = random.randint(300, 1500),
            description = fake.word()
        )
        
    print("Seeding complete!!")
    




