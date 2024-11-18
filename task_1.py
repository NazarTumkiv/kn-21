class Route:
    def __init__(self, start, finish, *distances):
        self.start = start
        self.finish = finish
        self.distances = list(distances)

    def __str__(self):
        total_distance = self.total_length()
        num_stops = self.num_stops()
        return f"Маршрут {self.start} - {self.finish}: {total_distance} км, {num_stops} привалів"

    def total_length(self):
        return sum(self.distances)

    def num_stops(self):
        return len(self.distances) - 1  # Кількість привалів (на 1 менше ніж переходів)

    def max_distance(self):
        return max(self.distances)

    # Перевантаження операторів порівняння за довжиною маршруту
    def __lt__(self, other):
        return self.total_length() < other.total_length()

    def __eq__(self, other):
        return self.total_length() == other.total_length()

# Створення списку маршрутів вручну
routes = [
    Route('Кваси', 'Дземброня', 8, 8, 12, 18, 12),
    Route('Ясіня', 'Говерла', 5, 7, 9, 10, 8),
    Route('Львів', 'Київ', 20, 25, 30),
    Route('Ужгород', 'Мукачево', 15, 18, 12, 10),
    Route('Чернівці', 'Івано-Франківськ', 12, 14, 15, 8),
    Route('Косів', 'Яремче', 7, 9, 12, 10, 13, 8),
    Route('Славське', 'Трускавець', 10, 12, 14),
    Route('Рахів', 'Буковель', 10, 10, 8, 20, 5),
    Route('Коломия', 'Долина', 6, 9, 7, 15),
    Route('Бережани', 'Тернопіль', 12, 8, 11)
]

# Упорядкування маршрутів за довжиною
routes.sort()

# Виведення всіх маршрутів
print("Упорядковані маршрути:")
for route in routes:
    print(route)

# Функція для знаходження маршруту з максимальною кількістю привалів
def route_with_max_stops(routes):
    max_stops_route = routes[0]
    for route in routes:
        if route.num_stops() > max_stops_route.num_stops():
            max_stops_route = route
    return max_stops_route

# Функція для знаходження маршруту з найдовшим переходом
def route_with_longest_leg(routes):
    longest_leg_route = routes[0]
    for route in routes:
        if route.max_distance() > longest_leg_route.max_distance():
            longest_leg_route = route
    return longest_leg_route

# Функція для пошуку маршрутів за початковою або кінцевою точкою
def routes_with_start_or_finish(routes, point):
    matching_routes = []
    for route in routes:
        if route.start == point or route.finish == point:
            matching_routes.append(route)
    return matching_routes

# Виведення маршруту з максимальною кількістю привалів
max_stops_route = route_with_max_stops(routes)
print("\nМаршрут з максимальною кількістю привалів:")
print(max_stops_route)

# Виведення маршруту з найдовшим переходом
longest_leg_route = route_with_longest_leg(routes)
print("\nМаршрут з найдовшим переходом:")
print(longest_leg_route)

# Пошук маршрутів за початковою або кінцевою точкою
point = 'Кваси'  # Вкажіть бажану точку
matching_routes = routes_with_start_or_finish(routes, point)
print(f"\nМаршрути з початком або кінцем у '{point}':")
for route in matching_routes:
    print(route)
