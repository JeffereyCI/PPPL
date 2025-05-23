from concrete_subject.temperature_sensor import TemperatureSensor
from concrete_observer.current_conditions_display import CurrentConditionsDisplay
from concrete_observer.statistics_display import StatisticsDisplay

def main():
    sensor = TemperatureSensor()
    current_display = CurrentConditionsDisplay()
    stats_display = StatisticsDisplay()

    sensor.register_observer(current_display)
    sensor.register_observer(stats_display)

    while True:
        inputUser = input("Apakah anda ingin mengubah suhu? (y/n) : ")

        if inputUser.lower() == 'n':
            print("Keluar dari program")
            break
        elif inputUser.lower() == 'y':
            inputSuhu = float(input("Masukkan suhu : "))
            sensor.set_temperature(inputSuhu)
        else:
            print("Input tidak valid")
            continue

if __name__ == "__main__":
    main()