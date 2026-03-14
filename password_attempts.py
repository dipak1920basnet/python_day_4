# Simulate login attempts. 
correct_password = "python123"
attempted_password = "hello"
attempt = 1
while attempt < 4:
    print(f"attempt{attempt} ", end="")
    if attempted_password == correct_password:
        print("Login successful")
        break
    else:
        print("Wrong attempt")
    attempt+=1
else:
    print("Attempt chances are over")
