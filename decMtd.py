class Robot:
    # Состояние батареи базовой станции:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    def update_base_battery_status(self, new_status):
        """Обновляет состояние батареи базовой станции."""
        self.base_battery_status = new_status

    def report(self):
        """Печатает в консоли состояние батареи базовой станции."""
        print(
            f'{self.name} reporting: Battery status is '
            f'{self.base_battery_status}%'
        )


# Создаём двух роботов:
robot1 = Robot('R2-D2')
robot2 = Robot('C-3PO')

# Печатаем состояние батареи:
robot1.report()
robot2.report()

# Обновляем статус батареи - но только в одном из роботов:
robot1.update_base_battery_status(80)

# Снова печатаем состояние батареи:
robot1.report()
robot2.report()