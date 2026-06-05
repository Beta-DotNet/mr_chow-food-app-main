from store.models import Product

# Clear existing products
Product.objects.all().delete()

products = [
    {
        "name": "Crispy Samosas",
        "price": "8.50",
        "description": "Golden, crispy pastry filled with spiced potatoes and peas. Served with a side of refreshing mint chutney.",
        "image_url": "https://images.unsplash.com/photo-1601050690597-df0568f70950?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Spicy Chicken Wrap",
        "price": "12.00",
        "description": "Grilled chicken breast with spicy mayo, fresh lettuce, and tomatoes wrapped in a warm, toasted tortilla.",
        "image_url": "https://images.unsplash.com/photo-1626804475297-41609ea004eb?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Oreo Cupcake",
        "price": "5.50",
        "description": "Decadent chocolate cupcake topped with creamy cookies-and-cream frosting and a whole Oreo cookie.",
        "image_url": "https://images.unsplash.com/photo-1587668178277-295251f900ce?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Meat & Fries Platter",
        "price": "16.50",
        "description": "Juicy, seasoned meat chunks served with a generous portion of crispy golden french fries.",
        "image_url": "https://images.unsplash.com/photo-1599596817294-8798bbcb0b06?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Chocolate Dip Churros",
        "price": "9.00",
        "description": "Freshly fried churros coated in cinnamon sugar, accompanied by a rich, dark chocolate dipping sauce.",
        "image_url": "https://images.unsplash.com/photo-1624371414361-e670edf4898d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    }
]

for p in products:
    Product.objects.create(**p)

print("Database seeded with new items!")
