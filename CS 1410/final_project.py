class RouteAndPersonalPreference:
  def __init__(self):
    self.start_point = ""
    self.end_point = ""
    # We use a dictionary to store specific data for each preference
    self.personal_preference = {}

  def get_user_input(self):
    """Collects journey details. Users can enter specific data or leave blank."""
    print("Plan your Journey")
    self.start_point = input("Enter point of Origin: ")
    self.end_point = input("Enter point of Destination: ")

# Capture specific data or None
    print("Enter your personal preferences(or press Enter to skip):")

    petrol = input("Preferred Gas Station: ").strip()
    self.personal_preference['gas station'] = petrol if petrol else None

    food = input("Preferred Restaurant/ Fast Food Place: ").strip()
    self.personal_preference['restaurant'] = food if food else None

    accomodation = input("Preferred accomodation: ").strip()
    self.personal_preference['accomodation'] = accomodation if accomodation else None

    return self.start_point, self.end_point, self.personal_preference


class RouteFinder:
  def __init__(self, origin, destination):
    self.origin = origin
    self.destination = destination

  def find_all_route(self):
        
        #Simulated routes with specific data metadata.
        #In a real app, 'amenities' would be populated by a Map API.
        
    return [
            {
                "id": "Route A",
                "amenities": {"gas station": "Shell", "restaurant": "Chipotle"},
                "distance": 150
            },
            {
                "id": "Route B",
                "amenities": {"restaurant": "Chick Fil A", "accommodation": "Hotel"},
                "distance": 200
            },
            {
                "id": "Route C",
                "amenities": {"gas station": "Chevron", "accommodation": "AirBnb"},
                "distance": 150
            }
        ]


class PreferredRoute:
    def __init__(self, user_prefs, routes):
        self.user_prefs = user_prefs 
        self.routes = routes

    def get_best_route(self):
        """Compares user preferences data against route amenities."""
        best_route = None
        highest_score = -1

        for route in self.routes:
            current_score = 0

# Logic: Iterate through user preferences
            for category, user_value in self.user_prefs.items():
                if user_value: # If the user actually provided data
                    # Check if the route has that category AND if the data matches

                    route_value = route["amenities"].get(category)
                    if route_value and user_value.lower() in route_value.lower():
                        current_score += 1
# Update best route based on matches
            if current_score > highest_score:
                highest_score = current_score
                best_route = route
                # Tie-breaker: choose the shorter distance
            elif current_score == highest_score:
                if best_route and route["distance"] < best_route["distance"]:
                    best_route = route

        return best_route


user_session = RouteAndPersonalPreference()
start, end, prefs = user_session.get_user_input()

finder = RouteFinder(start, end)
all_paths = finder.find_all_route()

selector = PreferredRoute(prefs, all_paths)
final_choice = selector.get_best_route()

print("\n--- Optimized Result ---")
if final_choice:
    print(f"The best route for your specific needs is: {final_choice['id']}")
    print(f"Amenities found: {final_choice['amenities']}")
    print(f"Total distance: {final_choice['distance']} miles")
else:
    print("No route found matching your criteria.")
