from flight import Flight
class CustomPriorityQueue:
    def __init__(self):
        self.queue = []
    
    def push(self, item):
        """Insert an item into the queue, maintaining order by the first element in the tuple."""
        self.queue.append(item)
        self.queue.sort()  # Sort by the first element, which is the priority value
    
    def pop(self):
        """Pop the item with the lowest priority (first item in tuple)."""
        if not self.queue:
            return None
        return self.queue.pop(0)
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

class Planner:
    def __init__(self, flights):
        """The Planner
        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.flights_from_city = {}
        for flight in flights:
            if flight.start_city not in self.flights_from_city:
                self.flights_from_city[flight.start_city] = []
            self.flights_from_city[flight.start_city].append(flight)

    def _is_valid_connection(self, prev_flight, next_flight):
        """Helper to check if connection between flights is valid"""
        return next_flight.departure_time >= prev_flight.arrival_time + 20

    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        """Return route with least flights and earliest arrival"""
        memo = {}  # Memoization for paths to avoid recomputation

        def dfs(curr_city, curr_time, path):
            if curr_city == end_city:
                return path

            if (curr_city, curr_time) in memo:
                return memo[(curr_city, curr_time)]

            valid_paths = []
            for flight in self.flights_from_city.get(curr_city, []):
                if flight.departure_time >= curr_time and flight.arrival_time <= t2:
                    if flight.departure_time >= t1:
                        if not path or self._is_valid_connection(path[-1], flight):
                            new_path = dfs(flight.end_city, flight.arrival_time, path + [flight])
                            if new_path:
                                valid_paths.append(new_path)

            # Select the best path by minimum length, then by earliest arrival
            best_path = min(valid_paths, key=lambda x: (len(x), x[-1].arrival_time), default=None)
            memo[(curr_city, curr_time)] = best_path
            return best_path

        return dfs(start_city, t1, []) or []

    def cheapest_route(self, start_city, end_city, t1, t2):
        """Return cheapest route with optimized custom priority queue usage"""
        distances = {start_city: (0, [], t1)}
        pq = CustomPriorityQueue()
        pq.push((0, start_city, [], t1))  # (cost, city, path, current time)

        while not pq.is_empty():
            curr_cost, curr_city, curr_path, curr_time = pq.pop()

            if curr_city == end_city:
                return curr_path

            if distances.get(curr_city, (float('inf'),))[0] < curr_cost:
                continue

            for flight in self.flights_from_city.get(curr_city, []):
                if flight.departure_time >= curr_time and flight.departure_time >= t1 and flight.arrival_time <= t2:
                    if not curr_path or self._is_valid_connection(curr_path[-1], flight):
                        new_cost = curr_cost + flight.fare
                        new_path = curr_path + [flight]
                        if new_cost < distances.get(flight.end_city, (float('inf'),))[0]:
                            distances[flight.end_city] = (new_cost, new_path, flight.arrival_time)
                            pq.push((new_cost, flight.end_city, new_path, flight.arrival_time))

        return distances.get(end_city, (float('inf'), []))[1]

    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """Return route with least flights and cheapest fare with optimized custom priority queue usage"""
        distances = {start_city: (0, 0, [], t1)}
        pq = CustomPriorityQueue()
        pq.push((0, 0, start_city, [], t1))  # (num_flights, cost, city, path, current time)

        while not pq.is_empty():
            num_flights, curr_cost, curr_city, curr_path, curr_time = pq.pop()

            if curr_city == end_city:
                return curr_path

            if distances.get(curr_city, (float('inf'), float('inf')))[0] < num_flights:
                continue

            for flight in self.flights_from_city.get(curr_city, []):
                if flight.departure_time >= curr_time and flight.departure_time >= t1 and flight.arrival_time <= t2:
                    if not curr_path or self._is_valid_connection(curr_path[-1], flight):
                        new_cost = curr_cost + flight.fare
                        new_flights = num_flights + 1
                        new_path = curr_path + [flight]
                        if (new_flights, new_cost) < distances.get(flight.end_city, (float('inf'), float('inf'))):
                            distances[flight.end_city] = (new_flights, new_cost, new_path, flight.arrival_time)
                            pq.push((new_flights, new_cost, flight.end_city, new_path, flight.arrival_time))

        return distances.get(end_city, (float('inf'), float('inf'), []))[2]
