# Predefined disease list that will be used
def predict(crop, yellow, spots, wilting, white):
    if crop == "potato":
        if spots == "yes" and yellow == "yes":
            return "Possible Disease:Early Blight"
        elif white == "yes":
            return "Possible Disease : Powdery Mildew"
        elif wilting == "yes":
            return "Possible disease : Wilt Disease"
        else:
            return "Disease could not be identified."
            
    elif crop == "rice":
        # Fixed "yes " typo here
        if spots == "yes" and yellow == "yes":
            return "Possible Disease:Rice Blast"
        elif wilting == "yes":
            return "Possible Disease :Bacterial Disease"
        else:
            return "Disease can not be identified." 
            
    elif crop == "wheat":
        if yellow == "yes" or spots == "yes":
            return "Possible Disease: Leaf Rust"
        elif white == "yes":
            return "possible Disease : Powdery Mildew"
        else: 
            return "Disease could not be identified"
            
    else:
        return "crop not available"