def check_continue():
    again = input("Do you want to check another crop?(yes/no):")
    if again == "no":
        print("thank you for using crop disease prediction!")
        return False
    return True