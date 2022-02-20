from random import randrange
import string
import sys

class Generator:
    def __str__(self) -> str:
        return 'Random password generator.'

    def generate(self, length) -> None:
        result = ''

        for _ in range(length // 4):
            result += self.get_char('number')

        for _ in range(length // 4):
            result += self.get_char('symbol')

        for _ in range(length // 4):
            result += self.get_char('uppercase')

        for _ in range(length - (length // 4 * 3)):
            result += self.get_char('lowercase')

        print(self.shuffle(result))

    def get_char(self, type) -> str:
        dictionay = {
            'number': string.digits,
            'symbol': string.punctuation,
            'lowercase': string.ascii_lowercase,
            'uppercase': string.ascii_uppercase,
        }
        dataset = dictionay[type]
        return dataset[randrange(len(dataset))]

    def shuffle(self, string) -> str:
        data = list(string)
        length = len(data)

        for i in range(length-1, -1, -1):
            x = randrange(length)
            data[i], data[x] = data[x], data[i]

        return ''.join(data)

class Checker:
    def __str__(self) -> str:
        return 'Password strength checker.'

    def test(self, password) -> None:
        dictionary = {
            'number': 0,
            'symbol': 0,
            'lowercase': 0,
            'uppercase': 0
        }

        for i in list(password):
            if i in string.digits:
                dictionary['number'] += 1
            if i in string.punctuation:
                dictionary['symbol'] += 1
            if i in string.ascii_lowercase:
                dictionary['lowercase'] += 1
            if i in string.ascii_uppercase:
                dictionary['uppercase'] += 1

        category = self.categorize(dictionary)
        print(category)

    def categorize(self, dictionary) -> str:
        length = sum(dictionary.values())

        contain_number = bool(dictionary['number'])
        contain_symbol = bool(dictionary['symbol'])
        contain_lowercase = bool(dictionary['lowercase'])
        contain_uppercase = bool(dictionary['uppercase'])

        # Categories: danger, bad, weak, good, excellent

        if contain_number and contain_symbol and contain_lowercase and contain_uppercase:
            if length >= 13:
                category = 'excellent'
            elif length >= 11:
                category = 'good'
            elif length >= 9:
                category = 'weak'
            elif length >= 6:
                category = 'bad'
            else:
                category = 'danger'
        elif contain_number and contain_lowercase and contain_uppercase:
            if length >= 14:
                category = 'excellent'
            elif length >= 11:
                category = 'good'
            elif length >= 9:
                category = 'weak'
            elif length >= 6:
                category = 'bad'
            else:
                category = 'danger'
        elif contain_lowercase and contain_uppercase:
            if length >= 15:
                category = 'excellent'
            elif length >= 12:
                category = 'good'
            elif length >= 10:
                category = 'weak'
            elif length >= 7:
                category = 'bad'
            else:
                category = 'danger'
        elif contain_lowercase or contain_uppercase:
            if length >= 18:
                category = 'excellent'
            elif length >= 14:
                category = 'good'
            elif length >= 11:
                category = 'weak'
            elif length >= 8:
                category = 'bad'
            else:
                category = 'danger'
        else:
            if length >= 16:
                category = 'weak'
            elif length >= 11:
                category = 'bad'
            else:
                category = 'danger'

        return category

class Parser:
    def __str__(self) -> str:
        return 'CLI parser.'

    def parse(self, argv) -> None:
        if len(argv) == 0:
            sys.exit('Empty argument.')
        elif argv[0] not in ('generate', 'test'):
            sys.exit("Invalid argument '{}'.".format(argv[0]))
        else:
            argument = argv[0]

            try:
                value = argv[1]
            except IndexError:
                value = None

            if argument == 'test':
                if value is None:
                    message = "python3 password.py test 'ABCdef123!@#$%'"
                    sys.exit("Invalid argument. Should be:\n{}".format(message))

                checker = Checker()
                checker.test(value)
            else:
                length = 13 if value is None else int(value)
                password = Generator()
                password.generate(length)

def main():
    argv = sys.argv
    argv = argv[1:]

    cli = Parser()
    cli.parse(argv)

if __name__ == '__main__':
    main()
