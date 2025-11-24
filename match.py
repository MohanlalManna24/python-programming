def match_case():
    """Demonstrate Python's match-case feature with various examples"""
    
    # Example 1: Basic pattern matching
    def basic_match(value):
        match value:
            case 1:
                return "One"
            case 2:
                return "Two"
            case 3:
                return "Three"
            case _:
                return "Unknown number"
    
    # Example 2: Pattern matching with data extraction
    def match_with_extraction(data):
        match data:
            case {"type": "user", "name": name, "age": age}:
                return f"User {name} is {age} years old"
            case {"type": "admin", "name": name}:
                return f"Admin {name}"
            case {"type": "guest"}:
                return "Guest user"
            case _:
                return "Unknown user type"
    
    # Example 3: Matching lists and tuples
    def match_sequences(seq):
        match seq:
            case [first, second, third]:
                return f"List with 3 elements: {first}, {second}, {third}"
            case [first, *rest]:
                return f"List starting with {first}, rest: {rest}"
            case (x, y):
                return f"Tuple with coordinates: ({x}, {y})"
            case []:
                return "Empty sequence"
            case _:
                return "Other sequence"
    
    # Example 4: Matching with guards (conditions)
    def match_with_guards(value):
        match value:
            case x if x < 0:
                return f"Negative number: {x}"
            case x if x == 0:
                return "Zero"
            case x if x > 0 and x < 10:
                return f"Single digit positive: {x}"
            case x if x >= 10:
                return f"Large number: {x}"
            case _:
                return "Unknown"
    
    # Example 5: Matching custom objects
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __getitem__(self, key):
            if key == 0:
                return self.x
            elif key == 1:
                return self.y
            raise IndexError("Point only has x and y coordinates")
    
    def match_point(point):
        match point:
            case Point(0, 0):
                return "Origin point"
            case Point(x, 0):
                return f"Point on x-axis: ({x}, 0)"
            case Point(0, y):
                return f"Point on y-axis: (0, {y})"
            case Point(x, y):
                return f"Point at ({x}, {y})"
            case _:
                return "Not a point"
    
    # Example 6: Complex nested matching
    def match_nested(data):
        match data:
            case {"users": [{"name": name, "role": "admin"} as admin, *rest]}:
                return f"Admin user: {name}, other users: {len(rest)}"
            case {"users": [*users]}:
                return f"User list with {len(users)} users"
            case {"error": error_msg}:
                return f"Error: {error_msg}"
            case _:
                return "Unknown data structure"
    
    # Test all the functions
    print("=== Python Match-Case Examples ===\n")
    
    # Test basic matching
    print("1. Basic Pattern Matching:")
    for i in range(1, 5):
        print(f"   {i} -> {basic_match(i)}")
    
    # Test data extraction
    print("\n2. Pattern Matching with Data Extraction:")
    users = [
        {"type": "user", "name": "Alice", "age": 25},
        {"type": "admin", "name": "Bob"},
        {"type": "guest"}
    ]
    for user in users:
        print(f"   {user} -> {match_with_extraction(user)}")
    
    # Test sequence matching
    print("\n3. Sequence Matching:")
    sequences = [[1, 2, 3], [1, 2], (5, 10), [], [1, 2, 3, 4, 5]]
    for seq in sequences:
        print(f"   {seq} -> {match_sequences(seq)}")
    
    # Test guards
    print("\n4. Matching with Guards:")
    numbers = [-5, 0, 3, 15]
    for num in numbers:
        print(f"   {num} -> {match_with_guards(num)}")
    
    # Test custom objects
    print("\n5. Custom Object Matching:")
    points = [Point(0, 0), Point(5, 0), Point(0, 3), Point(2, 4)]
    for point in points:
        print(f"   Point({point.x}, {point.y}) -> {match_point(point)}")
    
    # Test nested matching
    print("\n6. Nested Pattern Matching:")
    nested_data = [
        {"users": [{"name": "Admin", "role": "admin"}, {"name": "User", "role": "user"}]},
        {"users": [{"name": "Guest"}]},
        {"error": "Access denied"}
    ]
    for data in nested_data:
        print(f"   {data} -> {match_nested(data)}")

# Run the examples
if __name__ == "__main__":
    match_case()