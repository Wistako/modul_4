import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def main():
    print('W celu zakończenia programu wprowadź "q"')
    print('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie')
    while True:
        user_input = input('Wprowadź działanie: ')
        if user_input == 'q':
            break
        elif int(user_input) in [2,4]:
            first_number = float(input('Podaj składnik 1: '))
            second_number = float(input('Podaj składnik 2: '))
        elif int(user_input) in [1,3]:
            print('Możesz podać dowolną ilość składników, jeśli chcesz już wykonać działanie wpisz "e"')
            number_array = []
            count = 1
            while True:
                new_num = input(f'Wpisz "e" lub składnik {count}: ')
                if new_num == 'e': 
                    break
                else:

                    number_array.append(float(new_num))
                count += 1
        else: 
            print('Podano nieprawidłową wartość, spróbuj ponownie.')
            continue 

        user_input = int(user_input)
        if user_input == 1:
            print(f'Dodaję {" i ".join(map(str, number_array))}')
            result = 0
            for num in number_array:
                result += num
            print(f'Wynik to {result}')
        elif user_input == 2:
            print(f'Odejmuję {first_number} i {second_number}')
            print(f'Wynik to {first_number - second_number}')
        elif user_input == 3:
            print(f'Mnożę {" i ".join(map(str, number_array))}')
            result = number_array[0]
            for num in number_array[1:]:
                result *= num
            print(f'Wynik to {result}')
        elif user_input == 4:
            if second_number == 0:
                print('Nie można dzielić przez zero! /n Spróbuj ponownie')
                continue
            print(f'Dzielę {first_number} i {second_number}')
            print(f'Wynik to {first_number / second_number}')



        

if __name__ == "__main__":
    main()