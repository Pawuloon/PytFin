class DietDTO:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs

    def __str__(self):
        return f"{self.name} {self.calories} {self.protein} {self.fat} {self.carbs}"