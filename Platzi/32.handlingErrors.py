#https://docs.python.org/3.5/reference/compound_stmts.html#try

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(input("Write the name of the country: ")).lower()

    try:

        print('Population of {} is: {} millions'.format(country, countries[country]))

    except KeyError:
        print('Data not available for {}'.format(country))