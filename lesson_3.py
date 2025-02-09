class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        print("computations")

    def __str__(self):
        return f'CPU: {self.cpu}, Memory: {self.memory}'

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Call to {call_to_number} from {sim_card_number}')

    def __str__(self):
        return f'Sim_cards_list: {self.sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'Route to {location}')

    def __str__(self):
        return f'Cpu: {self.cpu}, Memory: {self.memory}, Sim_cards_list: {self.sim_cards_list}'


computer = Computer("Core i-9 14900k", 1024)
print(computer)

phone = Phone(["Mega", "O!", "Beeline"])
print(phone)

iphone = SmartPhone("A17", 512, ["Mega", "O!"])
print(iphone)

samsung = SmartPhone("SnapDragon", 256, ["Beeline", "Mega"])
print(samsung)

iphone.call(["Mega", "O!", "Beeline"][0], "0556995755")
samsung.use_gps("London")
print(f'The computer has more memory than iphone: {computer.memory > iphone.memory}')
print(f'The computer has less memory than samsung: {computer.memory < samsung.memory}')
