import randomuser


if __name__ == '__main__':
    ru = randomuser.get(results=10, nat='es,dk', gender='female')

    print(ru)
    print(ru[0].name_first)
    print(ru[0].get_full_name())
