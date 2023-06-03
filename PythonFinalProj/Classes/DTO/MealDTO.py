class MealDTO:
    def __init__(self, name, cal, protein, fat, carbs):
        self.name = name
        self.calories = cal
        self.protein = protein
        self.fat = fat
        self.carbs = carbs

    def __str__(self):
        return f"{self.name} {self.calories} {self.protein} {self.fat} {self.carbs}"
