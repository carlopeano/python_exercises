current_users = ['mArio', 'caesar', 'AGRippa', 'marla25','legend85']

our_users = [current_user.lower() for current_user in current_users]

print(our_users)


new_users = ['Agrippa', 'bruto', 'maRio', 'vale', 'anto']

for new_user in new_users:
    if new_user.lower() in our_users:
        print(f"The username {new_user} is already used. Please, choose another one.")
    else:
        print(f"The username {new_user} is available.")