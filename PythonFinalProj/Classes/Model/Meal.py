class Meal:
    def __init__(self, name, cal, protein, fat, carbs):
        self.name = name
        self.calories = cal
        self.protein = protein
        self.fat = fat
        self.carbs = carbs

    def __str__(self):
        return f"{self.name} {str(self.calories) + ' Cal'} {str(self.protein) + ' P'} {str(self.fat) + ' F'} {str(self.carbs) + ' C'}"
