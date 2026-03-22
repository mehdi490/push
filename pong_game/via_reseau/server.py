

import socket, time, pickle, random

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("127.0.0.1", 5555))
serversocket.listen(2)
#[player_1_y, player_2_y, ball_y, ball_x, score_1, score_2]
arr = [400,400,400,400,0,0]
connection = []
ball_y_speed = 1
ball_x_speed = 1


def process_positions(array, player_1, player_2):

    global ball_y_speed, ball_x_speed


    '''PADDLE MOVING'''
    if player_1[0] == True: # player 1 up
        array[0]-=1 
    else:
        array[0] = array[0] # the position of the paddle will not change
    if player_1[1] == True: # player 1 down
        array[0]+=1 # the position of the paddle will increase by 1
    else:
        array[0] = array[0]

    if player_2[0] == True: # player 2 up
        array[1]-=1 # the position of the paddle will decrease by 1
    else:
        array[1] = array[1] # the position of the paddle will not change 
    if player_2[1] == True:
        array[1]+=1
    else:
        array[1] = array[1]

    if array[0]<0: #  if the position less than 0, it will be set to 0
        array[0] = 0
    elif array[0] > 540: 
        array[0] = 540 # if the position greater than 540, it will be set to 540

    if array[1]<0: 
        array[1] = 0
    elif array[1] > 540:
        array[1] = 540

    '''PADDLE MOVING'''

    '''BALL MOVING'''
    array[2] += round(ball_y_speed) 
    array[3] += round(ball_x_speed)
    
    # In order to make the ball speed up, I will multiply the ball speed by a random number between -1.5 and -0.6 or 1 and 1.5 when the ball hits the wall
    negative_speed = [-0.6, -0.65, -0.7, -0.75, -0.8, -0.85, -0.9, -0.95, -1]
    positive_speed = [-1, -1.05, -1.1, -1.15, -1.2, -1.25, -1.3, -1.35, -1.4, -1.45, -1.5]

    if array[2] > 595: # if the ball hits the bottom wall, it will bounce back and speed up
        if ball_y_speed >= 1:
            ball_y_speed *= random.choice(negative_speed)
        elif ball_y_speed < 1:
            ball_y_speed *= random.choice(positive_speed)
    if array[2] < 0: # if the ball hits the top wall, it will bounce back and speed up
        if ball_y_speed >= 1:
            ball_y_speed *= random.choice(negative_speed)
        elif ball_y_speed < 1:
            ball_y_speed *= random.choice(positive_speed)

    if array[3]>795: # if the ball hits the right wall, it will bounce back and speed up, and player 1 will score a point
        if ball_x_speed >= 1:
            ball_x_speed *= random.choice(negative_speed)
        elif ball_x_speed < 1:
            ball_x_speed *= random.choice(positive_speed)
        array[4] += 1
    if array[3]<0: # if the ball hits the left wall, it will bounce back and speed up, and player 2 will score a point
        if ball_x_speed >= 1:
            ball_x_speed *= random.choice(negative_speed)
        elif ball_x_speed < 1:
            ball_x_speed *= random.choice(positive_speed)
        array[5] += 1

    '''BALL MOVING'''


    '''PADDLE DETECTION'''
    if array[3]<20 and (array[0]<array[2] and array[0]+60>array[2]): # if the ball hits the left paddle, 
        # it will bounce back and speed up
        ball_x_speed *=-1
    if array[3]>780 and (array[1]<array[2] and array[1]+60>array[2]): # if the ball hits the right paddle, 
        # it will bounce back and speed up
        ball_x_speed *=-1

    return array

def waiting_for_connections():
    while len(connection)<2:
        conn, addr = serversocket.accept()
        connection.append(conn)
        print(conn)
        print(connection)

def recieve_information():
    player_1_info = pickle.loads(connection[0].recv(1024))
    player_2_info = pickle.loads(connection[1].recv(1024))

    return player_1_info, player_2_info


while True:
    waiting_for_connections()

    data_arr = pickle.dumps(arr)
    print(data_arr)
    connection[0].send(data_arr)
    connection[1].send(data_arr)

    player1, player2 = recieve_information()

    arr = process_positions(arr,player1, player2)
