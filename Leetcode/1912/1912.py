from typing import List, Dict, Tuple


# ENTRIES = [SHOP, MOVIE, PRICE]


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.price_map: Dict[Tuple[int, int], int] = {}
        for s, m, p in entries:  # {(SHOP, MOVIE) : PRICE}
            self.price_map[(s, m)] = p

        # RENTED MOVIES
        self.rented = set()  # (SHOP, MOVIE)

    def search(self, movie: int) -> List[int]:
        # RETURN LIST OF **SHOPS** WHICH POSSESS THE MOVIE AND IS NOT RENTED.
        res = []

        for (s, m), p in self.price_map.items():
            if m == movie and (s, m) not in self.rented:
                res.append((p, s))

        # SORT BY PRICE ASC >> SHOP ASC
        res.sort()
        return [s for _, s in res[:5]]

    def rent(self, shop: int, movie: int) -> None:
        # RENTS THE GIVEN MOVIE FROM THE GIVEN SHOP
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.discard((shop, movie))

    def report(self) -> List[List[int]]:
        # RETURN THE CHEAPEST 5 RENTED MOVIES
        res = []
        for s, m in self.rented:
            # PRICE, SHOP, MOVIE -> FOR EASIER SORTING ACCORDING TO DESCRIPTION
            res.append((self.price_map[s, m], s, m))

        # SORTING THE RENTED MOVIES ACCORDING TO PRICE ASC ORDER >> SMALLER SHOP >> SMALLER MOVIE
        res.sort()
        return [[s, m] for _, s, m in res[:5]]
