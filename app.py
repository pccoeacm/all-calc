import glob
import importlib
import inspect


class Calc:
    def __init__(self):
        self.operators = {}
        self.functions = {}
        self.options = []
        self.load()
        self.build_options()

    def load(self):
        modules = [f.split('\\')[1] for f in glob.glob("functions/*.py")]

        for mods in modules:
            self.operators[mods.split(".")[0]] = importlib.import_module(
                f'functions.{mods.split(".")[0]}')

        for name, func in self.operators.items():
            self.functions[name] = inspect.getmembers(func,
                                                      inspect.isfunction)[0][1]
            self.options.append(name)

    def build_options(self):
        for i, option in enumerate(self.options):
            print(i + 1, option)

        ui = int(input("Which opertaions to excute > "))

        self.functions[self.options[ui - 1]]()


c = Calc()
c.build_options()