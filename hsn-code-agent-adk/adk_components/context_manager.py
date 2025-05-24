def extract_codes(user_input):
    import re
    return re.findall(r'\b\d{2,8}\b', user_input)
