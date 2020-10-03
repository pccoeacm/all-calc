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
        print(len(self.options)+1, "exit")

        while(True):
            try:
                ui = int(input("\nWhich operations to excute > "))
                break
            except:
                print("Enter a Valid Integer")
                continue

        if(ui == len(self.options)+1):
            return -1
        elif(ui > len(self.options or ui < 0)):
            print("Incorrect Option")
        else:
            response = self.functions[self.options[ui - 1]](should_print=True)

            if response is not None:
                print("\n", response)


print(
    r"""  /$$      /$$           /$$                                                     /$$
| $$  /$ | $$          | $$                                                    | $$
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$        /$$$$$$    /$$$$$$
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$      |_  $$_/   /$$__  $$
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$        | $$    | $$  \ $$
| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/        | $$ /$$| $$  | $$
| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$        |  $$$$/|  $$$$$$/
|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/         \___/   \______/



  /$$$$$$  /$$ /$$          /$$$$$$            /$$
 /$$__  $$| $$| $$         /$$__  $$          | $$
| $$  \ $$| $$| $$        | $$  \__/  /$$$$$$ | $$  /$$$$$$$
| $$$$$$$$| $$| $$ /$$$$$$| $$       |____  $$| $$ /$$_____/
| $$__  $$| $$| $$|______/| $$        /$$$$$$$| $$| $$
| $$  | $$| $$| $$        | $$    $$ /$$__  $$| $$| $$
| $$  | $$| $$| $$        |  $$$$$$/|  $$$$$$$| $$|  $$$$$$$
|__/  |__/|__/|__/         \______/  \_______/|__/ \_______/ """)

c = Calc()

while True:
    user_option = c.build_options()
    if(user_option == -1):
        break
