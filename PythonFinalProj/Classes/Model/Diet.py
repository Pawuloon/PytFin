class Diet:
    def __init__(self, dayName, calories, protein, fat, carbs):
        self.dayName = dayName
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs

    def __str__(self):
        return f"{self.dayName} {self.calories} {self.protein} {self.fat} {self.carbs}"
