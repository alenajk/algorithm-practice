def find_largest_sum(filename):
    """ Finds the path in triangle that will lead to the largest sum"""

    # Open and parse file and save as list of lists where each inner list represents a row in triangle 
    f = open(filename)
    triangle = []
    for line in f:
        line = line.strip().split()
        triangle.append(line)

    # Initialize sum to be value of first row in triangle
    sum = int(triangle[0][0])

    current_index = 0
    current_row = 0

    # Loop through rows in triangle comparing values of potential next steps in path
    # which are n and n+1 indices in next row
    for i in range(len(triangle)-1):
        possibility1 = triangle[current_row+1][current_index]
        possibility2 = triangle[current_row+1][current_index+1]
        print possibility1, possibility2
        chosen = int(max(possibility1, possibility2))
        sum += chosen
        current_row += 1
        if chosen == possibility2:
            current_index += 1

    return sum