# Restaurant Dictionaries

restaurants = {
    'restaurant1': {
        'name': 'The French Restaurant',
        'cuisine_type': 'French'
    },
    'restaurant2': {
        'name': 'Sio Mai Love',
        'cuisine_type': 'Chinese'
    },
    'restaurant3': {
        'name': 'Soba Hero',
        'cuisine_type': 'Japanese'
    },
    'restaurant4': {
        'name': 'Oistera Restaurant',
        'cuisine_type': 'Italian'
    },
    'restaurant5': {
        'name': 'Pizzeria Frenzy',
        'cuisine_type': 'Italian'
    }
}

# Function to display restaurant details
def display_restaurants(restaurant_dict):
    print("Restaurants:")
    for key, details in restaurant_dict.items():
        print(f"{key}: Name: '{details['name']}', Cuisine Type: {details['cuisine_type']}")

# Display the restaurants
display_restaurants(restaurants)
