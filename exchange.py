import requests


API_QUERY_TEMPLATE = 'https://api.exchangeratesapi.io/latest?base=' \
                     '{source}&symbols={target}'


class Money:

    def __init__(self, amount, currency='USD'):
        self.amount = amount
        self.currency = currency.upper()

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount
                         + self.exchange(other.currency,
                                         self.currency)
                         * other.amount, self.currency)
        else:
            return self

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __mul__(self, other):
        return Money(self.amount * other, self.currency)

    def __rmul__(self, other):
        return self * other

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

    @staticmethod
    def exchange(source, target):
        source = source.upper()
        target = target.upper()
        if source == target:
            return 1
        else:
            resp = requests.get(API_QUERY_TEMPLATE.format(
                source=source, target=target))
            if resp.status_code == 200:
                return resp.json()["rates"][target]
            else:
                raise Exception('Bad response. Status code: '
                                '{}'.format(resp.status_code))


if __name__ == '__main__':
    eur = Money(789, 'EUR')
    usd = Money(123.321)
    gbp = Money(456.654, 'GBP')

    print(sum([gbp, eur, usd]))
    print(usd + 3.22 * gbp + eur * 42)
