def check_in_row(board):
    '''
    check if there is same numbers in a row
    '''
    for row in board:
        for sign in row:
            if sign != "*" and sign != " ":
                count = row.count(sign)
                if count > 1:
                    return False
                return True      

def check_in_column(board):
    '''
    check if there is same numbers in a column
    '''
    column_lst = []
    
    for i in range(len(board[0])):
        column = ""
        for j in range(len(board)):
            if board[j][i] != "*" and \
            board[j][i] != " ":
                column += board[j][i]
        column_lst.append(column)
    
    for obj in column_lst:
        for element in obj:
            if obj.count(element) > 1:
                return False
    
    return True

def color_list(board, middle_x, middle_y):
    beginning_column = middle_y - 5
    end_row = middle_x + 5
    color = ""

    for i in range(beginning_column, middle_y):
        if board[i][middle_x]!= "*" and\
        board[i][middle_x]!= " ":
            color += board[i][middle_x]

    for j in range(middle_x, end_row):
        if board[middle_y][j] !="*" and\
        board[middle_y][j] !=" ":
            color += board[middle_y][j]

    return color

def check_in_color(board):
    lst = []

    for i in range(5):
        lst.append(color_list(board, middle_x = i, middle_y = len(board) - 1 - i))

    for color in lst:
        for element in  color:
            if color.count(element) > 1:
                return False
    return True

def validate_board(board):
    '''
    Check if there are same numbers in a same colored area
    '''
    if check_in_row(board) == True and check_in_column(board) == True and check_in_color(board) == True:
        return True
    return False

board = [
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   6  **",\
 "  8  2***",\
 "  2  ****"]
print(validate_board(board))
# print(check_in_row(board))
# print(check_in_column(board))
# print(check_in_color(board))
