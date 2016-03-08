def add( first, second):
    
    return first + second
    

def subtract( first, second):
    
    return first - second
    

def multiply( first, second):
    
    return first * second
    

def divide( first, second):
    try:
       result = first / second
    except ZeroDivisionError:
        print('I\'m sorry, I can\'t divide by zero')
    else:
        print('result is', result)

       
    return first / second
