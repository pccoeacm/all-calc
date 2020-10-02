import glob
import importlib
import inspect


class Calc:
    def __init__(self):
        self.operators = {}
        self.functions = {}
        self.options = []
        self.load()

    def load(self):
        modules = [f.split('\\')[1] for f in glob.glob("functions/*.py")]

        for mods in modules:
            self.operators[mods.split(".")[0]] = importlib.import_module(
                f'functions.{mods.split(".")[0]}')

        for name, func in self.operators.items():

            fns = inspect.getmembers(func, inspect.isfunction)

            if (len(fns) == 0):
                print(f"No functions in {name}.py")
                exit()

            found = False
            for f in fns:
                if f[0] == 'calc':
                    self.functions[name] = f[1]
                    found = True

            if not found:
                print(f"Can't find calc function in {name}.py")

            # self.functions[name] = inspect.getmembers(func,
            #                                           inspect.isfunction)[0][1]
            self.options.append(name)

    def build_options(self):
        print("\n")
        for i, option in enumerate(self.options):
            print(i + 1, option)

        ui = int(input("\nWhich operations to excute > "))

        if (ui > len(self.options or ui < 0)):
            print("Incorrect Option")

        else:
            self.functions[self.options[ui - 1]]()


c = Calc()

while True:
    c.build_options()