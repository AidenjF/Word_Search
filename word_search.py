""" File: word_search.py
    Author: Aiden Foster
    Purpose: To take a file that has a grid and a 
             list of words, and make it apparent 
             to the user where the words are and 
             if they are not there, we let them know.
"""
def main():
    """ This is the main function that will open
        the file and call the other functions to run
    """
    file = input('Please give the puzzle filename: \n')
    try:
        file = open(file, 'r')
    except FileNotFoundError:
        print("If we get here, the file didn't exist.")
        print("Please run the file again with a real file")
        return
    
    # call the grid_function function that will return the
    # grid and the list of words we need to find
    grid, words = grid_function(file)
    # run the function that does the checks for the words
    checks(grid, words)


def checks(grid, words):
    """ This function contains the beggining of the checks
        run throughs, it will call other functions when needed
        grid: this is a 2d list of the entire grid
        words: this is a list of all the words we need to find
    """
    found = []
    for word in words:
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == word[0]:
                    other = list(grid)
                    # north
                    north(other, word, x , y, grid, found)
                    # south
                    south(other, word, x , y, grid, found)
                    # west
                    west(other, word, x, y, grid, found)
                    # east
                    east(other, word, x, y, grid, found)
                    # northwest
                    northwest(other, word, x, y, grid, found) 
                    # northeast
                    northeast(other, word, x, y, grid, found)
                    # southwest
                    southwest(other, word, x, y, grid, found)
                    # southeast
                    southeast(other, word, x, y, grid, found)
        if word not in found:
            print(f"Word '{word}' not found")
            print()

def north(other, word, x , y, grid, found):
    """ This is the check functions that sees if the word
        is to the north or not.
        other: other is a copy of the list we can manipulate
        word: this is the word we need to find
        x: is the x index we are looking at
        y: is the y index we are looking at
        grid: this is a 2d list of the entire grid
        found: is a list of the words we have found
    """
    try:
        true_cords = []
        # check the next letter to see if it matches
        if grid[y - 1][x] == word[1]:
            string = ''
            k = 0
            while k < len(word):
                if grid[y - k][x] == word[k]:
                    # save the cordinates of the letter we need
                    cords = [[y - k],[x]]
                    true_cords.append(cords)
                    string += word[k]
                    k += 1
                    # if the cordinates go negative we want to quit
                    # because that will be a different side of the grid
                    if ((y - k) < 0 or (x) < 0) and (string != word):
                        break
                else:
                    break
                if string == word:
                    found.append(word)
                    new_grid(true_cords, other) 
    except IndexError:
        pass

def south(other, word, x , y, grid, found):
    """ This is the check functions that sees if the word
        is to the south or not.
        other: other is a copy of the list we can manipulate
        word: this is the word we need to find
        x: is the x index we are looking at
        y: is the y index we are looking at
        grid: this is a 2d list of the entire grid
        found: is a list of the words we have found
    """
    try:
        true_cords = []
        if grid[y + 1][x] == word[1]:
            string = ''
            k = 0
            while k < len(word):
                if grid[y + k][x] == word[k]:
                    cords = [[y + k],[x]]
                    true_cords.append(cords)
                    string += word[k]
                    k += 1
                    if ((y + k) < 0 or (x) < 0) and (string != word):
                        break
                else:
                    break
            if string == word:
                found.append(word)
                new_grid(true_cords, other)
    except IndexError:
        pass

def west(other, word, x, y, grid, found):
    """ This is the check functions that sees if the word
        is to the west or not.
        other: other is a copy of the list we can manipulate
        word: this is the word we need to find
        x: is the x index we are looking at
        y: is the y index we are looking at
        grid: this is a 2d list of the entire grid
        found: is a list of the words we have found
    """
    try:
        true_cords = []
        if grid[y][x - 1] == word[1]:
            string = ''
            k = 0
            while k < len(word):
                if grid[y][x - k] == word[k]:
                    cords = [[y],[x - k]]
                    true_cords.append(cords)
                    string += word[k]
                    k += 1
                    if ((y) < 0 or (x - k) < 0) and (string != word):
                        break
                else:
                    break
            if string == word:
                found.append(word)
                new_grid(true_cords, other)
    except IndexError:
        pass

def east(other, word, x, y, grid, found):
    """ This is the check functions that sees if the word
        is to the east or not.
        other: other is a copy of the list we can manipulate
        word: this is the word we need to find
        x: is the x index we are looking at
        y: is the y index we are looking at
        grid: this is a 2d list of the entire grid
        found: is a list of the words we have found
    """
    try:
        true_cords = []
        if grid[y][x + 1] == word[1]:
            string = ''
            k = 0
            while k < len(word):
                if grid[y][x + k] == word[k]:
                    cords = [[y],[x + k]]
                    true_cords.append(cords)
                    string += word[k]
                    k += 1
                    if ((y) < 0 or (x + k) < 0) and (string != word):
                        break
                else:
                    break
            if string == word:
                found.append(word)
                new_grid(true_cords, other)
    except IndexError:
        pass

def northwest(other, word, x, y, grid, found):
    """ This is the check functions that sees if the word
        is to the northwest or not.
        other: other is a copy of the list we can manipulate
        word: this is the word we need to find
        x: is the x index we are looking at
        y: is the y index we are looking at
        grid: this is a 2d list of the entire grid
        found: is a list of the words we have found
    """
    try:
        true_cords = []
        if grid[y + 1][x - 1] == word[1]:
            string = ''
            k = 0
            w = 0
            while k < len(word):
                if grid[y + k][x - w] == word[k]:
                    cords = [[y + k],[x - w]]
                    true_cords.append(cords)
                    string += word[k]
                    k += 1
                    w += 1
                    if ((y + k) < 0 or (x - w) < 0) and (string != word):
                        break
                else:
                    break
            if string == word:
                found.append(word)
                new_grid(true_cords, other)
    except IndexError:
        pass

def northeast(other, word, x, y, grid, found):
    """ This is the check functions that sees if the word
        is to the northeast or not.
        other: other is a copy of the list we can manipulate
        word: this is the word we need to find
        x: is the x index we are looking at
        y: is the y index we are looking at
        grid: this is a 2d list of the entire grid
        found: is a list of the words we have found
    """
    try:
        true_cords = []
        if grid[y + 1][x + 1] == word[1]:
            string = ''
            k = 0
            w = 0
            while k < len(word):
                if grid[y + k][x + w] == word[k]:
                    cords = [[y + k],[x + w]]
                    true_cords.append(cords)
                    string += word[k]
                    k += 1
                    w += 1
                    if ((y + k) < 0 or (x + w) < 0) and (string != word):
                        break
                else:
                    break
            if string == word:
                found.append(word)
                new_grid(true_cords, other)
    except IndexError:
        pass

def southwest(other, word, x, y, grid, found):
    """ This is the check functions that sees if the word
        is to the southwest or not.
        other: other is a copy of the list we can manipulate
        word: this is the word we need to find
        x: is the x index we are looking at
        y: is the y index we are looking at
        grid: this is a 2d list of the entire grid
        found: is a list of the words we have found
    """
    try:
        true_cords = []
        if grid[y - 1][x - 1] == word[1]:
            string = ''
            k = 0
            w = 0
            while k < len(word):
                if grid[y - k][x - w] == word[k]:
                    cords = [[y - k],[x - w]]
                    true_cords.append(cords)
                    string += word[k]
                    k += 1
                    w += 1
                    if ((y - k) < 0 or (x - w) < 0) and (string != word):
                        break
                else:
                    break
            if string == word:
                found.append(word)
                new_grid(true_cords, other)
    except IndexError:
        pass

def southeast(other, word, x, y, grid, found):
    """ This is the check functions that sees if the word
        is to the southeast or not.
        other: other is a copy of the list we can manipulate
        word: this is the word we need to find
        x: is the x index we are looking at
        y: is the y index we are looking at
        grid: this is a 2d list of the entire grid
        found: is a list of the words we have found
    """
    try:
        true_cords = []
        if grid[y - 1][x + 1] == word[1]:
            string = ''
            k = 0
            w = 0
            while k < len(word):
                if grid[y - k][x + k] == word[k]:
                    cords = [[y - k],[x + k]]
                    true_cords.append(cords)
                    string += word[k]
                    k += 1
                    w += 1
                    if ((y - k) < 0 or (x + k) < 0) and (string != word):
                        break
                else:
                    break
            if string == word:
                found.append(word)
                new_grid(true_cords, other)
    except IndexError:
        pass

def grid_function(file):
    """ This function takes the input file and will
        spit out a grid or 2d list for us to work on
        file: this is the file that we opened to read
    """
    lines = file.readlines()
    x = []
    # go through each lines
    for line in lines:
        inner = []
        line = line.strip('\n')
        # go through each letter
        for letters in line:
            inner.append(letters)
        x.append(inner)
    words = []
    i = 0
    # this loop decides where the grid ends
    while i <= len(x) - 1:
        if x[i] == []:
            x.remove(x[i])
            while i <= len(x) - 1:
                word = ''.join(x[i])
                words.append(word)
                x.remove(x[i])
        i += 1
    return x, words
    
def new_grid(true_cords, grid):
    """ This function creates a new grid that was 
        manipulated to show where the word was for the
        user
        truecords: is a list of the cordinates where the
        word is located
        grid: is a 2d list of the grid we are searching 
        through
    """
    other = []
    # itterate through the grid to find the cords
    for y in range(len(grid)):
        other_inner = []
        for x in range(len(grid[0])):
            cordinate = [[y],[x]]
            # if it is not in the cords list
            # then append a '.' instead
            if cordinate not in true_cords:
                other_inner.append('.')
            else: 
                other_inner.append(grid[y][x])
        other.append(other_inner)
    for y in range(len(other)):
        f = ''.join(other[y])
        # print each line
        print(f)
    print()


if __name__=="__main__":
    main()