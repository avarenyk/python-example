class Phone:

    def __init__(self, number: str = None, model: str = None, weight: str = None):
        self.number = number
        self.model = model
        self.weight = weight

        for i in self.number:
            if i.isalpha():
                raise TypeError(
                    f'Invalid {self.number.index(i)+1} symbol "{i}" in number {self.number}')

    def __str__(self):
        return f'My phone number is {self.number}, model is {self.model} and it weight is {self.weight}'

    def receiveCall(self, number: str = None, name: str = None):
        for i in number:
            if i.isalpha() and number != None:
                raise TypeError(
                    f'Invalid {number.index(i)+1} symbol "{i}" in number {number}')
        if name == None:
            return f'{number} is calling'
        else:
            return f'{name} is calling, number is {number}'

    def getNumber(self):
        return self.number

    def sendMessage(self, *args: str):
        for i in args:
            if not isinstance(i, int):
                raise TypeError(f'Invalid {args.index(i)+1} symbol "{i}"')
            else:
                return ', '.join(str(x) for x in args)
