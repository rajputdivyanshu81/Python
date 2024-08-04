def https_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "internal server error"
        case _:
            return "unknown error"
        
print(https_status(3095  ))