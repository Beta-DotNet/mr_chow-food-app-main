from store.models import Product

products = [
    {
        "name": "Wagyu Beef Burger",
        "price": "24.99",
        "description": "Premium wagyu beef patty with truffle mayo, caramelized onions, and aged cheddar on a brioche bun.",
        "image_url": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Truffle Mushroom Risotto",
        "price": "28.50",
        "description": "Creamy arborio rice cooked with wild mushrooms, white wine, parmesan cheese, and finished with truffle oil.",
        "image_url": "https://images.unsplash.com/photo-1626074964464-f27be462004a?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Lobster Ravioli",
        "price": "32.00",
        "description": "Handmade ravioli stuffed with fresh Maine lobster, served in a rich saffron cream sauce.",
        "image_url": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Artisan Margherita Pizza",
        "price": "18.00",
        "description": "Wood-fired pizza with San Marzano tomato sauce, fresh mozzarella di bufala, and basil.",
        "image_url": "https://images.unsplash.com/photo-1604068549290-dea0e4a30536?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Matcha Tiramisu",
        "price": "12.50",
        "description": "A modern twist on the classic dessert with premium ceremonial grade matcha and mascarpone.",
        "image_url": "https://images.unsplash.com/photo-1571115177098-24de412030ac?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    }
]

for p in products:
    Product.objects.get_or_create(name=p['name'], defaults=p)

print("Database seeded with premium products!")
