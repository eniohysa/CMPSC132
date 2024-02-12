class Date:
    def __init__(self, mm=1, dd=1, yyyy=2024):
        self.__month = mm
        self.__date = dd
        self.__year = yyyy

    def __str__(self):
        return f''