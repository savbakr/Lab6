#Tanner Fulwider's Program

def encode(password):
    res = ''
    for item in password:
        res += str(int(item) + 3)
    return res

def main():
    coder_continue = True
    while coder_continue:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        option = int(input('\nPlease enter an option: '))
        if option == 1:
            decoded_pass = input('Please enter your password to encode: ')
            encoded_password = encode(decoded_pass)
            print('Your password has been encoded and stored!')
            print()
        if option == 3:
            coder_continue = False
            break

if __name__ == '__main__':
    main()
