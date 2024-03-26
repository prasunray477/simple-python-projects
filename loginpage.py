import pandas as pd

user_input = []
num_rows = int(input("How many users data want to input: "))

for i in range(num_rows):
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    user_input.append([username, password])

df = pd.DataFrame(user_input, columns=['username', 'password'])
print(df) 
while True:
    change_data = input("Do you want to change any username or password? (yes/no): ")
    if change_data == 'yes':
        change_type = input("Which data do you want to change? (username/password): ")
        if change_type == 'username':
            old_username = input("Enter the old username: ")
            if old_username not in df['username'].values:
                print("username not found!")
                continue
            new_username = input("Enter the new username: ")
            df.loc[df['username'] == old_username, 'username'] = new_username
        elif change_type == 'password':
            old_password = input("Enter the old password: ")
            if old_password not in df['password'].values:
                print("Password not found!")
                continue
            new_password = input("Enter the new password: ")
            df.loc[df['password'] == old_password, 'password'] = new_password
        else:
            print("Invalid input. Please enter either 'username' or 'password'.")
    else:
        print("Your response has been recorded :) ")
        break
df.to_csv("login_page.csv",index=False) 
