class Helpers:
    ROBOT_LIBRARY_SCOPE = 'SUITE'

    def find_max_price(self, elements):
        prices = []
        for i in elements:
            prices.append(i.text)
        highest = max(prices)
        return highest
