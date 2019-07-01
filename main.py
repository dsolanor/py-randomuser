import randomuser


if __name__ == '__main__':
    ru = randomuser.get(results=10, nat='es,dk', gender='female')

    print(ru)