def converting(value):
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return None
    else:
        return None
def cleaning(value):
    if isinstance(value, str):
        return value.strip().capitalize()
    else:
        return None
        

        
    