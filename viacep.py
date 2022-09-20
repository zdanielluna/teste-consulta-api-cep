from pycep_correios import get_address_from_cep, WebService, exceptions
from time import sleep


with open('ceps.txt', 'r') as f:
    ceps = [line.strip() for line in f]

# print(ceps)
count = 0
for cep in ceps:
    try:
        address = get_address_from_cep(
            cep, webservice=WebService.VIACEP)
        print(f'| {count} | {address}')
        print('---------------------------------------------')
    except exceptions.InvalidCEP as eic:
        print(eic)

    except exceptions.CEPNotFound as ecnf:
        print(ecnf)

    except exceptions.ConnectionError as errc:
        print(errc)

    except exceptions.Timeout as errt:
        print(errt)

    except exceptions.HTTPError as errh:
        print(errh)

    except exceptions.BaseException as e:
        print(e)

    count += 1
sleep(2)
