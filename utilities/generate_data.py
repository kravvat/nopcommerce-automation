import random, string
from faker import Faker


class GenerateRandomData():
    
    @staticmethod
    def generate_random_email(length=8):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        domain = random.choice(['gmail.com', 'yahoo.com', 'proton.me', 'outlook.com'])
        return f"{username}@{domain}"


    @staticmethod
    def generate_random_password(length=12):
        return ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*()-_=+', k=length))


    @staticmethod
    def generate_random_first_name():
        fake = Faker()
        return fake.first_name()    


    @staticmethod
    def generate_random_last_name():
        fake = Faker()
        return fake.last_name()


    @staticmethod
    def generate_random_company():
        fake = Faker()
        return fake.company()


    @staticmethod
    def generate_random_comment():
        fake = Faker()
        return fake.sentence(random.randint(1, 100))


    @staticmethod
    def generate_random_category():
        return random.choice(
            [
                "computers",
                "electronics",
                "apparel",
                "digital-downloads",
                "books",
                "jewelry",
                "gift-cards",
            ]
        )


    @staticmethod
    def generate_random_subcategory(category):
        match category:
            case "computers":
                return random.choice(
                    [
                        "desktops",
                        "notebooks",
                        "software",
                    ]
                )
            case "electronics":
                return random.choice(
                    [
                        "camera-photo",
                        "cell-phones",
                        "others",
                    ]
                )
            case "apparel":
                return random.choice(
                    [
                        "shoes",
                        "clothing",
                        "accessories",
                    ]
                )
