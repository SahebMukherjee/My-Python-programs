b = {"math":3,
     "science":2,
     "english":4,
     "history":1
    }
b_name = input("Enter book name:").lower()
if b_name in b:
    if b[b_name] > 0:
        b[b_name] -= 1
        print("Book issued successfully!")
    else:
        print("Books not found.")
print("Remaining books:")
for b, qty in b.items():
    print(b,":",qty)
