def route_intent(user_input):
    if "validate" in user_input.lower() or "hsn" in user_input.lower():
        return "ValidateHSNCode"
    return "FallbackIntent"
