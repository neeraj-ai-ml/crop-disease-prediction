import inputs
import predictor
import loop_handler

print("--- Crop Prediction Disease System ---")

while True:
    crop, yellow, spots, wilting, white = inputs.get_inputs()
    
    # Making prediction
    print("Crop disease prediction result: ")
    result = predictor.predict(crop, yellow, spots, wilting, white)
    print(result)
    
    # If user wants to continue
    if not loop_handler.check_continue():
        break