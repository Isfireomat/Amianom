i = "пздц"
if isinstance(i, str): 
    match type(i):
        case list:
            print("!")
        case str:
            print(i)