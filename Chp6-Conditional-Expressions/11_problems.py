blance = 5000

withdrow_acount = int(input("Enter the amount you want to withdrow: "))


if withdrow_acount <= blance:
    print("Transaction is successful.")
else:
    print("Transaction failed. Insufficient balance.")
