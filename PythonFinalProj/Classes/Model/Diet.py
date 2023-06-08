
"""
Diet class responsible for representing the diet model
"""
class Diet:
    def __init__(self, Id, dayName, calories, protein, fat, carbs):
        self.Id = Id
        self.dayName = dayName
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs

    def __str__(self):
        return f"{self.dayName} {self.calories} {self.protein} {self.fat} {self.carbs}"
