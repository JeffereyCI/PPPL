from interface.observer import Observer

class StatisticsDisplay(Observer):
    def __init__(self):
        self.temperatures = []

    def update(self, temperature: float):
        self.temperatures.append(temperature)
        avg = sum(self.temperatures) / len(self.temperatures)
        min_temp = min(self.temperatures)
        max_temp = max(self.temperatures)
        print(f"[StatisticsDisplay] Rata-rata: {avg:.2f} Derajat Celsius, minimum: {min_temp:.2f} Derajat Celsius, maksimum: {max_temp:.2f} Derajat Celsius")
