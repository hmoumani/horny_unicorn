import time
from random import randint
import os
# ... your definition of log decorator...
def log(func):
    def wrapper(*args, **kwargs):
        f = open("machine.log", "a")
        print(f"({os.environ['USER']})Running:", end=' ', file=f)
        print("{: <19}".format(func.__name__.replace('_', ' ').capitalize()), end='', file=f)
        start_time = time.time() * 1000
        ret = func(*args, **kwargs)
        end_time = (time.time() * 1000) - start_time
        end_time = "{:.3f} s".format(end_time / 1000) if int(end_time / 1000) > 0 else "{:.3f} ms".format(end_time)
        print("[ exec-time = {} ]".format(end_time), file=f)
        return ret
    return wrapper

class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
