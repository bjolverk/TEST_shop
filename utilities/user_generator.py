import random

from mimesis import Person
from mimesis import Address
from mimesis.locales import Locale

person = Person(Locale.RU)


def phone_generator():
    """"""

    return person.telephone(mask='### ### ## ##')


def email_generator():
    return person.email()


def name_generator():
    return f'{person.first_name()} {person.last_name()}'


def address_generator(full=0):
    address = Address('ru')
    if full == 1:
        return f'{address.state()},{address.city()}, {address.address()}'
    else:
        return f'Москва, {address.address()} кв. {random.randint(1, 101)}'


if __name__ == '__main__':
    print(phone_generator(), email_generator(), address_generator(), name_generator())
