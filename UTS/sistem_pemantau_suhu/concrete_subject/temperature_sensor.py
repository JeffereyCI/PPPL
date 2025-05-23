from interface.observer import Observer
from subject.subject import Subject

class TemperatureSensor(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0.0

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float):
        print(f"\n[Sensor] Suhu baru: {temperature}°C")
        self._temperature = temperature
        self.notify_observers()