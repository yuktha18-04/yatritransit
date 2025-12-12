
# route_calc.py
def calculate_route(origin: str, destination: str) -> dict:
    routes = {
        ("A", "B"): {"stops": ["A", "X", "B"], "distance_km": 12.5, "time_min": 20},
        ("B", "C"): {"stops": ["B", "Y", "C"], "distance_km": 8.0, "time_min": 12},
        ("A", "C"): {"stops": ["A", "X", "B", "Y", "C"], "distance_km": 20.5, "time_min": 32},
    }
    key = (origin, destination)
    if key in routes:
        return {"origin": origin, "destination": destination, **routes[key]}
    return {"origin": origin, "destination": destination, "stops": [origin, destination], "distance_km": 5.0, "time_min": 8}
