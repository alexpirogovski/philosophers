from philosofer_class import Philosopher
from chopstick_class import Chopstick, ChopstickState

if __name__ == "__main__":

    global chopstick_array
    chopstick_array = []
    for i in range (0,5):
        chopstick_array.append(Chopstick())

    philosopher1 = Philosopher("Pooper", chopstick_array)
    philosopher2 = Philosopher("Schultz", chopstick_array)
    philosopher3 = Philosopher("Bados", chopstick_array)
    philosopher4 = Philosopher("Fabel", chopstick_array)
    philosopher5 = Philosopher("Denisko", chopstick_array)
    philosopher1.start()
    philosopher2.start()
    philosopher3.start()
    philosopher4.start()
    philosopher5.start()
