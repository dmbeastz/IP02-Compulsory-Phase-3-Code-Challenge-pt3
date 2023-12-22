class Database:
    def __init__(self):
        self.customers = []
        self.restaurants = []
        self.reviews = []

class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = None

    def given_name(self):
        return self.first_name

    def family_name(self):
        return self.last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, db):
        self.id = len(db.customers) + 1
        db.customers.append(self)

    @classmethod
    def find_by_name(cls, db, full_name):
        for customer in db.customers:
            if customer.full_name() == full_name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, db, given_name):
        return [customer for customer in db.customers if customer.given_name() == given_name]

    @classmethod
    def find_by_id(cls, db, id):
        for customer in db.customers:
            if customer.id == id:
                return customer
        return None

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.id = None

    def save(self, db):
        self.id = len(db.restaurants) + 1
        db.restaurants.append(self)

    def average_star_rating(self, db):
        ratings = [review.rating for review in db.reviews if review.restaurant == self]
        return sum(ratings) / len(ratings) if ratings else 0

    def reviews(self, db):
        return [review for review in db.reviews if review.restaurant == self]

    def customers(self, db):
        return list(set([review.customer for review in db.reviews if review.restaurant == self]))

    @classmethod
    def find_by_id(cls, db, id):
        for restaurant in db.restaurants:
            if restaurant.id == id:
                return restaurant
        return None

class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.id = None

    def save(self, db):
        self.id = len(db.reviews) + 1
        db.reviews.append(self)

    @classmethod
    def all(cls, db):
        return db.reviews


db = Database()

# Creating instances
customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("Good Eats")
review1 = Review(customer1, restaurant1, 4)


customer1.save(db)
restaurant1.save(db)
review1.save(db)

all_reviews = Review.all(db)
for review in all_reviews:
    print(f"Review ID: {review.id}, Customer: {review.customer.full_name()}, Restaurant: {review.restaurant.name}, Rating: {review.rating}")


average_rating = restaurant1.average_star_rating(db)
print(f"Average Star Rating for {restaurant1.name}: {average_rating}")


restaurant_reviews = restaurant1.reviews(db)
for review in restaurant_reviews:
    print(f"Review ID: {review.id}, Rating: {review.rating}")

restaurant_customers = restaurant1.customers(db)
for customer in restaurant_customers:
    print(f"Customer: {customer.full_name()}")


found_customer = Customer.find_by_name(db, "John Doe")
print(f"Found Customer: {found_customer.full_name()}")

customers_with_given_name = Customer.find_all_by_given_name(db, "John")
for customer in customers_with_given_name:
    print(customer.full_name())

customer2 = Customer("Jane", "Doe")
restaurant2 = Restaurant("Tasty Bites")
review2 = Review(customer2, restaurant2, 5)

customer2.save(db)
restaurant2.save(db)
review2.save(db)


all_reviews = Review.all(db)
for review in all_reviews:
    print(f"Review ID: {review.id}, Customer: {review.customer.full_name()}, Restaurant: {review.restaurant.name}, Rating: {review.rating}")

average_rating = restaurant2.average_star_rating(db)
print(f"Average Star Rating for {restaurant2.name}: {average_rating}")


restaurant_reviews = restaurant2.reviews(db)
for review in restaurant_reviews:
    print(f"Review ID: {review.id}, Rating: {review.rating}")


restaurant_customers = restaurant2.customers(db)
for customer in restaurant_customers:
    print(f"Customer: {customer.full_name()}")

found_customer = Customer.find_by_name(db, "Jane Doe")
print(f"Found Customer: {found_customer.full_name()}")


customers_with_given_name = Customer.find_all_by_given_name(db, "Jane")
for customer in customers_with_given_name:
    print(customer.full_name())