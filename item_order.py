# Function to count custumer order
def item_order(order):
    ''' function input is string with order 
    function output displays the items ordered
    '''
   
    # Define variables to be used in function 
    s = 0
    h = 0
    w = 0
    count = 0

    # while loop to count order
    while count < len(str(order)):
        if order[count:count+5] == 'salad':
            s += 1
        elif order[count:count+5] == 'water':
                w += 1
        elif order[count:count+9] == 'hamburger':
                h += 1
        
        count += 1

    # Return string of order items
    itemorder = 'salad:' + str(s) + ' hamburger:' + str(h) + ' water:' + str(w)
    return itemorder