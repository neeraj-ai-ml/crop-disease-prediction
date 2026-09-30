def get_inputs():
    crop = input("Enter crop (potato/rice/wheat): ")
    print("Enter symptoms: ")
    yellow = input("Leaves are yellow?(yes/no): ")
    spots = input("Leaves have spots?(yes/no): ")
    wilting = input("Plant is wilting?(yes/no): ")
    white = input("white powder on leaves?(yes/no): ")
    
    return crop, yellow, spots, wilting, white