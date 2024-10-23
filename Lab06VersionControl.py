#Tanner Fulwider's Program

def encode(password):
    res = ''
    for item in password:
        num = str(int(item) + 3)
        if len(num) == 2:
            num = num[1]
        res += num
    return res

def main():
    # NEW: Added this line to store encoded password globally in the function
    encoded_password = ''  
    
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
            
        # NEW: Added entire elif block for option 2 
        elif option == 2:  
            if encoded_password:  
                pass  # Placeholder for partner's decode implementation 
            else:  
                print("Please encode a password first.")  
                print()  
                
        # CHANGED: elif instead of if, and removed break statement 
        elif option == 3:  
            coder_continue = False
            
if __name__ == '__main__':
    main()
