class Solution:
    def assignBikes(
        self, workers: List[List[int]], bikes: List[List[int]]
    ) -> List[int]:
        # T: O(w * b), S: O(w * b)
        # Step 1: Compute all distances and store in buckets
        distance_map = defaultdict(list)
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx - bx) + abs(wy - by)
                distance_map[dist].append((i, j))  # Store (worker, bike)

        # Step 2: Process distances in sorted order
        assigned = [-1] * len(workers)
        taken_bikes = set()

        for dist in sorted(distance_map.keys()):
            for worker, bike in sorted(
                distance_map[dist]
            ):  # Maintain worker-bike order
                if assigned[worker] == -1 and bike not in taken_bikes:
                    assigned[worker] = bike
                    taken_bikes.add(bike)

        return assigned
