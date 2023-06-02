class Diet:
    def __init__(self, breakfast, lunch, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner

    def __str__(self):
        return f"{self.breakfast} {self.lunch} {self.dinner}"
