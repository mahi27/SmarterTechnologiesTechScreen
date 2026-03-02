def sort(width, height, length, mass):
    #check input validity
    #width, height, length should be in cm; mass should be in kg
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("Enter valid input!")
    
    volume = width * height * length
    # Check conditions
    bulky = volume >= 1000000 or max(width, height, length) >= 150
    heavy = mass >= 20
    
    # Determine stack
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
