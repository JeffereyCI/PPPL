from interface.observer import Observer

class CurrentConditionsDisplay(Observer):
    def update(self, temperature: float):
        print(f"[CurrentConditionsDisplay] Suhu saat ini: {temperature} Derajat Celsius")
