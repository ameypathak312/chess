
paths=[[' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ',' ']]
board=[['R1','N1','B1','Q1','K','B2','N2','R2'],
       ['P1','P2','P3','P4','P5','P6','P7','P8'],
       [' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ',' '],
       ['p1','p2','p3','p4','p5','p6','p7','p8'],
       ['r1','n1','b1','q1','k','b2','n2','r2']]

w_queen_num=2
b_queen_num=2
b_king_moved=0
w_king_moved=0
king_involved=[0]
valid_pos=[]
alive=[]
wsurround=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bsurround=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
wem_passent=[0,0,0,0,0,0,0,0]
bem_passent=[0,0,0,0,0,0,0,0]
bpos=([1,0,1],[1,1,1],[1,2,1],[1,3,1],[1,4,1],[1,5,1],[1,6,1],[1,7,1],[0,0,1],[0,7,1],[0,1,1],[0,6,1],[0,2,1],[0,5,1],[0,3,1],[0,4,1]
      ,[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1])
wpos=([6,0,1],[6,1,1],[6,2,1],[6,3,1],[6,4,1],[6,5,1],[6,6,1],[6,7,1],[7,0,1],[7,7,1],[7,1,1],[7,6,1],[7,2,1],[7,5,1],[7,3,1],[7,4,1]
      ,[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1],[-1,-1,-1])
wattack_piece=[]
battack_piece=[]
wdefend_pos=([],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
bdefend_pos=([],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
wdefend_num=[]
bdefend_num=[]
wdir=0
bdir=0
block_wdir=0
block_bdir=0
checkpiece=[-1,-1]
CHECKPIECE=[-1,-1]
wblockpieces=0
bblockpieces=0
kingneighbour=[]
KINGNEIGHBOUR=[]
def reset():
       global paths
       global board
       global w_queen_num,b_queen_num,b_king_moved,w_king_moved,king_involved,valid_pos,alive,wsurround
       global bsurround,wem_passent,bem_passent,bpos,wpos,wattack_piece,battack_piece,wdefend_pos,bdefend_pos,wdefend_num
       global bdefend_num,wdir,bdir,block_wdir,block_bdir,checkpiece,CHECKPIECE,wblockpieces,bblockpieces,kingneighbour,KINGNEIGHBOUR
       paths = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
       board = [['R1', 'N1', 'B1', 'Q1', 'K', 'B2', 'N2', 'R2'],
                ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8'],
                ['r1', 'n1', 'b1', 'q1', 'k', 'b2', 'n2', 'r2']]

       w_queen_num = 2
       b_queen_num = 2
       b_king_moved = 0
       w_king_moved = 0
       king_involved = [0]
       valid_pos = []
       alive = []
       wsurround = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       bsurround = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       wem_passent = [0, 0, 0, 0, 0, 0, 0, 0]
       bem_passent = [0, 0, 0, 0, 0, 0, 0, 0]
       bpos = (
       [1, 0, 1], [1, 1, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 6, 1], [1, 7, 1], [0, 0, 1], [0, 7, 1],
       [0, 1, 1], [0, 6, 1], [0, 2, 1], [0, 5, 1], [0, 3, 1], [0, 4, 1]
       , [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1])
       wpos = (
       [6, 0, 1], [6, 1, 1], [6, 2, 1], [6, 3, 1], [6, 4, 1], [6, 5, 1], [6, 6, 1], [6, 7, 1], [7, 0, 1], [7, 7, 1],
       [7, 1, 1], [7, 6, 1], [7, 2, 1], [7, 5, 1], [7, 3, 1], [7, 4, 1]
       , [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1, -1, -1])
       wattack_piece = []
       battack_piece = []
       wdefend_pos = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
       bdefend_pos = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
       wdefend_num = []
       bdefend_num = []
       wdir = 0
       bdir = 0
       block_wdir = 0
       block_bdir = 0
       checkpiece = [-1, -1]
       CHECKPIECE = [-1, -1]
       wblockpieces = 0
       bblockpieces = 0
       kingneighbour = []
       KINGNEIGHBOUR = []
def reset1():
       reset()
def intersection(lst1,lst2):
       global king_involved
       lst =[value for value in lst1 if value in lst2]
       if len(lst)!=0:
              king_involved[0]=1
       return lst
def find_num(piece):
       if piece=='p1' or piece=='P1':
              return 0
       elif piece=='p2' or piece=='P2':
              return 1
       elif piece=='p3' or piece=='P3':
              return 2
       elif piece=='p4' or piece=='P4':
              return 3
       elif piece=='p5' or piece=='P5':
              return 4
       elif piece=='p6' or piece=='P6':
              return 5
       elif piece=='p7' or piece=='P7':
              return 6
       elif piece=='p8' or piece=='P8':
              return 7
       elif piece=='r1' or piece=='R1':
              return 8
       elif piece=='r2' or piece=='R2':
              return 9
       elif piece=='n1' or piece=='N1':
              return 10
       elif piece=='n2' or piece=='N2':
              return 11
       elif piece=='b1' or piece=='B1':
              return 12
       elif piece=='b2' or piece=='B2':
              return 13
       elif piece=='q1' or piece=='Q1':
              return 14
       elif piece=='k' or piece=='K':
              return 15
       elif piece=='q2' or piece=='Q2':
              return 16
       elif piece=='q3' or piece=='Q3':
              return 17
       elif piece=='q4' or piece=='Q4':
              return 18
       elif piece=='q5' or piece=='Q5':
              return 19
       elif piece=='q6' or piece=='Q6':
              return 20
       elif piece=='q7' or piece=='Q7':
              return 21
       elif piece=='q8' or piece=='Q8':
              return 22
       elif piece=='q9' or piece=='Q9':
              return 23
def test(a,b,c):
       inposx=a
       inposy=b
       a = a-1
       b = b-1
       ch=0
       while 0<=a and 0<=b:
              if board[a][b].islower():
                     break
              elif board[a][b][0]=='Q' or board[a][b][0]=='B':
                     ch=1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
                     break
              elif board[a][b].isupper():
                     break
              else:
                     a=a-1
                     b=b-1
       a = inposx
       b = inposy
       a = a - 1
       while 0 <= a :
              if board[a][b].islower():
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'R':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
                     break
              elif board[a][b].isupper():
                     break
              else:
                     a = a - 1
       a = inposx
       b = inposy
       a = a - 1
       b = b + 1
       while 0 <= a and b<=7:
              if board[a][b].islower():
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'B':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
                     break
              elif board[a][b].isupper():
                     break
              else:
                     a = a - 1
                     b = b + 1
       a = inposx
       b = inposy
       b = b + 1
       while b <= 7:
              if board[a][b].islower():
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'R':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
                     break
              elif board[a][b].isupper():
                     break
              else:
                     b = b + 1
       a = inposx
       b = inposy
       a = a + 1
       b = b + 1
       while a <= 7 and b <= 7:
              if board[a][b].islower():
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'B':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
                     break
              elif board[a][b].isupper():
                     break
              else:
                     a = a + 1
                     b = b + 1
       a = inposx
       b = inposy
       a = a + 1
       while a <= 7:
              if board[a][b].islower():
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'R':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
                     break
              elif board[a][b].isupper():
                     break
              else:
                     a = a + 1
       a = inposx
       b = inposy
       a = a + 1
       b = b - 1
       while a <= 7 and 0 <= b:
              if board[a][b].islower():
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'B':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
                     break
              elif board[a][b].isupper():
                     break
              else:
                     a = a + 1
                     b = b - 1
       a = inposx
       b = inposy
       b = b - 1
       while 0 <= b:
              if board[a][b].islower():
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'R':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
                     break
              elif board[a][b].isupper():
                     break
              else:
                     b = b - 1
       a = inposx
       b = inposy
       a = a-1
       b = b-2
       if 0<=b and b<=7 and 0<=a and a<=7:
              if board[a][b][0]=='N':
                     ch=1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
       a = a - 1
       b = b + 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
       b = b + 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
       a = a + 1
       b = b + 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
       a = a + 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
       a = a + 1
       b = b - 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
       b = b - 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
       a = a - 1
       b = b - 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
       return ch
def testpawnc(a,b,c):
       inposx = a
       inposy = b
       ch=0
       a=a-1
       b=b-1
       if 0<=a and 0<=b:
              if board[a][b][0]=='P':
                     ch=1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
       b = b+2
       if 0<=a and b<=7:
              if board[a][b][0]=='P':
                     ch=1
                     if c==0:
                            battack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx,inposy])
                            CHANGE_STATE(board[a][b],9)
       return ch
def testpawns(a,b):
       inposx = a
       inposy = b
       ch = 0
       a = a - 1
       if 0 <= a:
              if board[a][b][0]=='P':
                     ch = 1
                     x = find_num(board[a][b])
                     bdefend_num.append(x)
                     bdefend_pos[x].append([inposx, inposy])
                     CHANGE_STATE(board[a][b], 9)
       a = inposx
       b = inposy
       if a==3:
              a = a - 1
              if board[a][b]==' ':
                     a = a - 1
                     if board[a][b][0]=='P':
                            ch = 1
                            x = find_num(board[a][b])
                            bdefend_num.append(x)
                            bdefend_pos[x].append([inposx, inposy])
                            CHANGE_STATE(board[a][b], 9)
       return ch
def TEST(a,b,c):
       inposx=a
       inposy=b
       a = a-1
       b = b-1
       ch=0
       while 0<=a and 0<=b:
              if board[a][b].isupper():
                     break
              elif board[a][b][0]=='q' or board[a][b][0]=='b':
                     ch=1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
                     break
              elif board[a][b].islower():
                     break
              else:
                     a=a-1
                     b=b-1
       a = inposx
       b = inposy
       a = a - 1
       while 0 <= a :
              if board[a][b].isupper():
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'r':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
                     break
              elif board[a][b].islower():
                     break
              else:
                     a = a - 1
       a = inposx
       b = inposy
       a = a - 1
       b = b + 1
       while 0 <= a and b<=7:
              if board[a][b].isupper():
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'b':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
                     break
              elif board[a][b].islower():
                     break
              else:
                     a = a - 1
                     b = b + 1
       a = inposx
       b = inposy
       b = b + 1
       while b <= 7:
              if board[a][b].isupper():
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'r':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
                     break
              elif board[a][b].islower():
                     break
              else:
                     b = b + 1
       a = inposx
       b = inposy
       a = a + 1
       b = b + 1
       while a <= 7 and b <= 7:
              if board[a][b].isupper():
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'b':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
                     break
              elif board[a][b].islower():
                     break
              else:
                     a = a + 1
                     b = b + 1
       a = inposx
       b = inposy
       a = a + 1
       while a <= 7:
              if board[a][b].isupper():
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'r':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
                     break
              elif board[a][b].islower():
                     break
              else:
                     a = a + 1
       a = inposx
       b = inposy
       a = a + 1
       b = b - 1
       while a <= 7 and 0 <= b:
              if board[a][b].isupper():
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'b':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
                     break
              elif board[a][b].islower():
                     break
              else:
                     a = a + 1
                     b = b - 1
       a = inposx
       b = inposy
       b = b - 1
       while 0 <= b:
              if board[a][b].isupper():
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'r':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
                     break
              elif board[a][b].islower():
                     break
              else:
                     b = b - 1
       a = inposx
       b = inposy
       a = a-1
       b = b-2
       if 0<=b and b<=7 and 0<=a and a<=7:
              if board[a][b][0]=='n':
                     ch=1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
       a = a - 1
       b = b + 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
       b = b + 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
       a = a + 1
       b = b + 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
       a = a + 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
       a = a + 1
       b = b - 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
       b = b - 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
       a = a - 1
       b = b - 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
       return ch
def TESTPAWNC(a,b,c):
       inposx = a
       inposy = b
       ch=0
       a=a+1
       b=b-1
       if a<=7 and 0<=b:
              if board[a][b][0]=='p':
                     ch=1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
       b = b+2
       if a<=7 and b<=7:
              if board[a][b][0]=='p':
                     ch=1
                     if c==0:
                            wattack_piece.append([a,b])
                     elif c==1:
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx,inposy])
                            change_state(board[a][b],9)
       return ch
def TESTPAWNS(a,b):
       inposx = a
       inposy = b
       ch = 0
       a = a + 1
       if a<=7:
              if board[a][b][0]=='p':
                     ch = 1
                     x = find_num(board[a][b])
                     wdefend_num.append(x)
                     wdefend_pos[x].append([inposx, inposy])
                     change_state(board[a][b], 9)
       a = inposx
       b = inposy
       if a==4:
              a = a + 1
              if board[a][b]==' ':
                     a = a + 1
                     if board[a][b][0]=='p':
                            ch = 1
                            x = find_num(board[a][b])
                            wdefend_num.append(x)
                            wdefend_pos[x].append([inposx, inposy])
                            change_state(board[a][b], 9)
       return ch

def pawn(a,b,c,d,e):
       if c!=9:
              print('in pawn')
              print(board)

              unblock=((0,0,0,0),(1,1,1,1),(0,1,0,1),(1,0,0,0),(0,0,1,0))
              a=a-1
              b=b-1
              if unblock[c][0] == 1:
                     if 0<=a and 0<=b:
                            if (board[a][b].isupper() and board[a][b]!='K') or e == 1:
                                   paths[a][b]='*'
                                   wsurround[d]=1
              b=b+1
              if unblock[c][1] == 1:
                     if 0<=a:
                            if board[a][b]==' ':
                                   paths[a][b]='*'
                                   print(paths)
                                   wsurround[d] = 1
              b=b+1
              if unblock[c][2] == 1:
                     if 0<=a and b<=7:
                            if (board[a][b].isupper() and board[a][b]!='K') or e == 2:
                                   paths[a][b]='*'
                                   wsurround[d] = 1
              a=a+1
              b=b-1
              if unblock[c][3] == 1:
                     if a==6:
                            a=a-1
                            if board[a][b]==' ':
                                   a=a-1
                                   if board[a][b] == ' ':
                                          paths[a][b]='*'
       else:
              for pos in wdefend_pos[d]:
                     paths[pos[0]][pos[1]]='*'
                     wsurround[d] = 1
def bishop(a,b,c,d):
       if c!=9:
              inposx=a
              inposy=b
              unblock=((0,0,0,0),(1,1,1,1),(1,0,1,0),(0,1,0,1))
              if unblock[c][0] == 1:
                     a=a-1
                     b=b-1
                     while 0<=a and 0<=b and board[a][b]!='K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                                   a=a-1
                                   b=b-1
              if unblock[c][1] == 1:
                     a=inposx
                     b=inposy
                     a=a-1
                     b=b+1
                     while 0<=a and b<=7 and board[a][b]!='K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                                   a=a-1
                                   b=b+1
              if unblock[c][2] == 1:
                     a = inposx
                     b = inposy
                     a = a + 1
                     b = b + 1
                     while a <= 7 and b <= 7 and board[a][b] != 'K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   a = a + 1
                                   b = b + 1
              if unblock[c][3] == 1:
                     a = inposx
                     b = inposy
                     a = a + 1
                     b = b - 1
                     while a <= 7 and 0 <= b and board[a][b] != 'K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   a = a + 1
                                   b = b - 1
       else:
              for pos in wdefend_pos[d]:
                     paths[pos[0]][pos[1]]='*'
                     wsurround[d] = 1
def rook(a,b,c,d):
       if c!=9:
              inposx = a
              inposy = b
              unblock=((0,0,0,0),(1,1,1,1),(1,0,0,1),(0,1,1,0))
              if unblock[c][0] == 1:
                     a=a-1
                     while 0<=a and board[a][b]!='K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                                   a=a-1
              if unblock[c][1] == 1:
                     a = inposx
                     b = inposy
                     b=b+1
                     while b <= 7 and board[a][b] != 'K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   b = b + 1
              if unblock[c][2] == 1:
                     a = inposx
                     b = inposy
                     b = b - 1
                     while 0 <= b and board[a][b] != 'K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   b = b - 1
              if unblock[c][3] == 1:
                     a = inposx
                     b = inposy
                     a = a + 1
                     while a <= 7 and board[a][b] != 'K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   a = a + 1
       else:
              for pos in wdefend_pos[d]:
                     paths[pos[0]][pos[1]]='*'
                     wsurround[d] = 1
def knight(a,b,c,d):
       if c!=9:
              unblock=((0,0,0,0,0,0,0,0),(1,1,1,1,1,1,1,1))
              b=b-2
              a=a-1
              if unblock[c][0] == 1:
                     if 0<=a and a<=7 and 0<=b and b<=7:
                            if board[a][b].isupper() and board[a][b]!='K':
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                            elif board[a][b]==' ':
                                   paths[a][b]='*'
                                   wsurround[d] = 1
              b = b + 1
              a = a - 1
              if unblock[c][1] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].isupper() and board[a][b] != 'K':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                            elif board[a][b] == ' ':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
              b = b + 2
              if unblock[c][2] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].isupper() and board[a][b] != 'K':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                            elif board[a][b] == ' ':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
              b = b + 1
              a = a + 1
              if unblock[c][3] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].isupper() and board[a][b] != 'K':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                            elif board[a][b] == ' ':
                                   paths[a][b] = '*'
              a = a + 2
              if unblock[c][4] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].isupper() and board[a][b] != 'K':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                            elif board[a][b] == ' ':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
              b = b - 1
              a = a + 1
              if unblock[c][5] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].isupper() and board[a][b] != 'K':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                            elif board[a][b] == ' ':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
              b = b - 2
              if unblock[c][6] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].isupper() and board[a][b] != 'K':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                            elif board[a][b] == ' ':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
              b = b - 1
              a = a - 1
              if unblock[c][7] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].isupper() and board[a][b] != 'K':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                            elif board[a][b] == ' ':
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
       else:
              for pos in wdefend_pos[d]:
                     paths[pos[0]][pos[1]]='*'
                     wsurround[d] = 1
def queen(a,b,c,d):
       if c!=9:
              inposx=a
              inposy=b
              unblock = ((0,0,0,0,0,0,0,0),(1,1,1,1,1,1,1,1),(1,0,1,0,0,0,0,0),(0,1,0,1,0,0,0,0),(0,0,0,0,1,0,0,1),(0,0,0,0,0,1,1,0))
              if unblock[c][0] == 1:
                     a=a-1
                     b=b-1
                     while 0<=a and 0<=b and board[a][b]!='K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                                   a=a-1
                                   b=b-1
              if unblock[c][1] == 1:
                     a=inposx
                     b=inposy
                     a=a-1
                     b=b+1
                     while 0<=a and b<=7 and board[a][b]!='K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                                   a=a-1
                                   b=b+1
              if unblock[c][2] == 1:
                     a = inposx
                     b = inposy
                     a = a + 1
                     b = b + 1
                     while a <= 7 and b <= 7 and board[a][b] != 'K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   a = a + 1
                                   b = b + 1
              if unblock[c][3] == 1:
                     a = inposx
                     b = inposy
                     a = a + 1
                     b = b - 1
                     while a <= 7 and 0 <= b and board[a][b] != 'K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   a = a + 1
                                   b = b - 1
              if unblock[c][4] == 1:
                     a = inposx
                     b = inposy
                     a=a-1
                     while 0<=a and board[a][b]!='K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b]='*'
                                   wsurround[d] = 1
                                   a=a-1
              if unblock[c][5] == 1:
                     a = inposx
                     b = inposy
                     b=b+1
                     while b <= 7 and board[a][b] != 'K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   b = b + 1
              if unblock[c][6] == 1:
                     a = inposx
                     b = inposy
                     b = b - 1
                     while 0 <= b and board[a][b] != 'K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   b = b - 1
              if unblock[c][7] == 1:
                     a = inposx
                     b = inposy
                     a = a + 1
                     while a <= 7 and board[a][b] != 'K':
                            if board[a][b].islower():
                                   break
                            elif board[a][b].isupper():
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   break
                            else:
                                   paths[a][b] = '*'
                                   wsurround[d] = 1
                                   a = a + 1
       else:
              for pos in wdefend_pos[d]:
                     paths[pos[0]][pos[1]]='*'
                     wsurround[d] = 1
def king(a,b,c):
       inposx = a
       inposy = b
       t=0
       a=a-1
       b=b-1
       if 0<=a and a<=7 and 0<=b and b<=7:
              if board[a][b].isupper() or board[a][b]==' ':
                     if test(a,b,0)==0:
                            t=1
                     if testpawnc(a,b,0)==0 and t==1:
                            paths[a][b]='*'
       b = b + 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].isupper() or board[a][b] == ' ':
                     if test(a, b, 0) == 0:
                            t=1
                     if testpawnc(a, b, 0) == 0 and t==1:
                            paths[a][b] = '*'
       b = b + 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].isupper() or board[a][b] == ' ':
                     if test(a, b, 0) == 0:
                            t=1
                     if testpawnc(a, b, 0) == 0 and t==1:
                            paths[a][b] = '*'
       a = a + 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].isupper() or board[a][b] == ' ':
                     if test(a, b, 0) == 0:
                            t=1
                     if testpawnc(a, b, 0) == 0 and t==1:
                            paths[a][b] = '*'
       a = a + 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].isupper() or board[a][b] == ' ':
                     if test(a, b, 0) == 0:
                            t=1
                     if testpawnc(a, b, 0) == 0 and t==1:
                            paths[a][b] = '*'
       b = b - 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].isupper() or board[a][b] == ' ':
                     if test(a, b, 0) == 0:
                            t=1
                     if testpawnc(a, b, 0) == 0 and t==1:
                            paths[a][b] = '*'
       b = b - 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].isupper() or board[a][b] == ' ':
                     if test(a, b, 0) == 0:
                            t=1
                     if testpawnc(a, b, 0) == 0 and t==1:
                            paths[a][b] = '*'
       a = a - 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].isupper() or board[a][b] == ' ':
                     if test(a, b, 0) == 0:
                            t=1
                     if testpawnc(a, b, 0) == 0 and t==1:
                            paths[a][b] = '*'
       if c == 0:
              print('w=',w_king_moved)
              a = inposx
              b = inposy
              if test(a, b, 2) == 0 and testpawnc(a, b, 2) == 0:
                     b = b - 1
                     if board[a][b]==' ' and test(a, b, 2) == 0 and testpawnc(a, b, 2) == 0:
                            b = b - 1
                            if board[a][b]==' ' and test(a, b, 2) == 0 and testpawnc(a, b, 2) == 0:
                                   if board[7][0] == 'r1' and board[7][1] == ' ':
                                          paths[a][b]='*'
                     a = inposx
                     b = inposy
                     b = b + 1
                     if board[a][b]==' ' and test(a, b, 2) == 0 and testpawnc(a, b, 2) == 0:
                            b = b + 1
                            if board[a][b]==' ' and test(a, b, 2) == 0 and testpawnc(a, b, 2) == 0:
                                   if board[7][7] == 'r2' and board[7][6] == ' ':
                                          paths[a][b]='*'


       delete=0
       delete=intersection(kingneighbour,KINGNEIGHBOUR)
       if len(delete)>0:
              for pos in delete:
                     paths[pos[0]][pos[1]]=' '
       a = inposx
       b = inposy
       a = a - 1
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b]=='*':
                     wsurround[15] = 1
       b = b + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b]=='*':
                     wsurround[15] = 1
       b = b + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     wsurround[15] = 1
       a = a + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     wsurround[15] = 1
       a = a + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     wsurround[15] = 1
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     wsurround[15] = 1
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     wsurround[15] = 1
       a = a - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     wsurround[15] = 1
def find_kingneighbour(a,b):
       kingneighbour.clear()
       a = a - 1
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              kingneighbour.append([a, b])
       b = b + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              kingneighbour.append([a, b])
       b = b + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              kingneighbour.append([a, b])
       a = a + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              kingneighbour.append([a, b])
       a = a + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              kingneighbour.append([a, b])
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              kingneighbour.append([a, b])
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              kingneighbour.append([a, b])
       a = a - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              kingneighbour.append([a, b])

def PAWN(a,b,c,d,e,mode):
       if c!=9:
              a=a+1
              b=b-1
              unblock = ((0, 0, 0, 0), (1, 1, 1, 1), (0, 1, 0, 1),(1, 0, 0, 0),(0, 0, 1, 0))
              if unblock[c][0] == 1:
                     if a<=7 and 0<=b:
                            if (board[a][b].islower() and board[a][b]!='k') or e == 1:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d]=1
              b=b+1
              if unblock[c][1] == 1:
                     if a<=7:
                            if board[a][b] == ' ':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
              b=b+1
              if unblock[c][2] == 1:
                     if a<=7 and b<=7:
                            if (board[a][b].islower() and board[a][b]!='k') or e == 2:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
              a=a-1
              b=b-1
              if unblock[c][3] == 1:
                     if a == 1 :
                            a=a+1
                            if board[a][b]==' ':
                                   a=a+1
                                   if board[a][b] == ' ':
                                          if mode == 1:
                                                 paths[a][b] = '*'
                                          else:
                                                 valid_pos.append([a, b])
       else:
              for pos in bdefend_pos[d]:
                     if mode == 1:
                            paths[pos[0]][pos[1]] = '*'
                     else:
                            valid_pos.append([pos[0], pos[1]])
                     bsurround[d] = 1
def BISHOP(a,b,c,d,mode):
       if c!=9:
              inposx=a
              inposy=b
              unblock = ((0, 0, 0, 0), (1, 1, 1, 1), (1, 0, 1, 0), (0, 1, 0, 1))
              if unblock[c][0] == 1:
                     a=a-1
                     b=b-1
                     while 0<=a and 0<=b and board[a][b]!='k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   a=a-1
                                   b=b-1
              if unblock[c][1] == 1:
                     a=inposx
                     b=inposy
                     a=a-1
                     b=b+1
                     while 0<=a and b<=7 and board[a][b]!='k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   a=a-1
                                   b=b+1
              if unblock[c][2] == 1:
                     a = inposx
                     b = inposy
                     a = a + 1
                     b = b + 1
                     while a <= 7 and b <= 7 and board[a][b] != 'k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   a = a + 1
                                   b = b + 1
              if unblock[c][3] == 1:
                     a = inposx
                     b = inposy
                     a = a + 1
                     b = b - 1
                     while a <= 7 and 0 <= b and board[a][b] != 'k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   a = a + 1
                                   b = b - 1
       else:
              for pos in bdefend_pos[d]:
                     if mode == 1:
                            paths[pos[0]][pos[1]] = '*'
                     else:
                            valid_pos.append([pos[0], pos[1]])
                     bsurround[d] = 1
def ROOK(a,b,c,d,mode):
       if c!=9:
              unblock = ((0, 0, 0, 0), (1, 1, 1, 1), (1, 0, 0, 1), (0, 1, 1, 0))
              inposx = a
              inposy = b
              if unblock[c][0] == 1:
                     a=a-1
                     while 0<=a and board[a][b]!='k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   a=a-1

              if unblock[c][1] == 1:
                     a = inposx
                     b = inposy
                     b=b+1
                     while b <= 7 and board[a][b] != 'k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   b = b + 1

              if unblock[c][2] == 1:
                     a = inposx
                     b = inposy
                     b = b - 1
                     while 0 <= b and board[a][b] != 'k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   b = b - 1

              if unblock[c][3] == 1:
                     a = inposx
                     b = inposy
                     a = a + 1
                     while a <= 7 and board[a][b] != 'k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   a = a + 1
       else:
              for pos in bdefend_pos[d]:
                     if mode == 1:
                            paths[pos[0]][pos[1]] = '*'
                     else:
                            valid_pos.append([pos[0], pos[1]])
                     bsurround[d] = 1
def KNIGHT(a,b,c,d,mode):
       if c!=9:
              b=b-2
              a=a-1
              unblock = ((0, 0, 0, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1, 1))
              if unblock[c][0] == 1:
                     if 0<=a and a<=7 and 0<=b and b<=7:
                            if board[a][b].islower() and board[a][b]!='k':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                            elif board[a][b]==' ':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
              b = b + 1
              a = a - 1
              if unblock[c][1] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].islower() and board[a][b] != 'k':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                            elif board[a][b] == ' ':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
              b = b + 2
              if unblock[c][2] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].islower() and board[a][b] != 'k':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                            elif board[a][b] == ' ':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
              b = b + 1
              a = a + 1
              if unblock[c][3] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].islower() and board[a][b] != 'k':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                            elif board[a][b] == ' ':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
              a = a + 2
              if unblock[c][4] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].islower() and board[a][b] != 'k':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                            elif board[a][b] == ' ':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
              b = b - 1
              a = a + 1
              if unblock[c][5] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].islower() and board[a][b] != 'k':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                            elif board[a][b] == ' ':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
              b = b - 2
              if unblock[c][6] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].islower() and board[a][b] != 'k':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                            elif board[a][b] == ' ':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
              b = b - 1
              a = a - 1
              if unblock[c][7] == 1:
                     if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                            if board[a][b].islower() and board[a][b] != 'k':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                            elif board[a][b] == ' ':
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
       else:
              for pos in bdefend_pos[d]:
                     if mode == 1:
                            paths[pos[0]][pos[1]] = '*'
                     else:
                            valid_pos.append([pos[0], pos[1]])
                     bsurround[d] = 1
def QUEEN(a,b,c,d,mode):
       if c!=9:
              inposx=a
              inposy=b
              unblock = ((0, 0, 0, 0, 0, 0, 0, 0),(1, 1, 1, 1, 1, 1, 1, 1), (1, 0, 1, 0, 0, 0, 0, 0), (0, 1, 0, 1, 0, 0, 0, 0),
              (0, 0, 0, 0, 1, 0, 0, 1), (0, 0, 0, 0, 0, 1, 1, 0))
              if unblock[c][0] == 1:
                     a=a-1
                     b=b-1
                     while 0<=a and 0<=b and board[a][b]!='k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   a=a-1
                                   b=b-1
              if unblock[c][1] == 1:
                     a=inposx
                     b=inposy
                     a=a-1
                     b=b+1
                     while 0<=a and b<=7 and board[a][b]!='k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   a=a-1
                                   b=b+1
              if unblock[c][2] == 1:
                     a = inposx
                     b = inposy
                     a = a + 1
                     b = b + 1
                     while a <= 7 and b <= 7 and board[a][b] != 'k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   a = a + 1
                                   b = b + 1
              if unblock[c][3] == 1:
                     a = inposx
                     b = inposy
                     a = a + 1
                     b = b - 1
                     while a <= 7 and 0 <= b and board[a][b] != 'k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   a = a + 1
                                   b = b - 1
              if unblock[c][4] == 1:
                     a = inposx
                     b = inposy
                     a=a-1
                     while 0<=a and board[a][b]!='k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   a=a-1
              if unblock[c][5] == 1:
                     a = inposx
                     b = inposy
                     b=b+1
                     while b <= 7 and board[a][b] != 'k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   b = b + 1
              if unblock[c][6] == 1:
                     a = inposx
                     b = inposy
                     b = b - 1
                     while 0 <= b and board[a][b] != 'k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   b = b - 1
              if unblock[c][7] == 1:
                     a = inposx
                     b = inposy
                     a = a + 1
                     while a <= 7 and board[a][b] != 'k':
                            if board[a][b].isupper():
                                   break
                            elif board[a][b].islower():
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   break
                            else:
                                   if mode == 1:
                                          paths[a][b] = '*'
                                   else:
                                          valid_pos.append([a,b])
                                   bsurround[d] = 1
                                   a = a + 1
       else:
              for pos in bdefend_pos[d]:
                     if mode == 1:
                            paths[pos[0]][pos[1]] = '*'
                     else:
                            valid_pos.append([pos[0], pos[1]])
                     bsurround[d] = 1
def KING(a,b,c,mode):
       inposx = a
       inposy = b
       a=a-1
       b=b-1
       t=0
       if 0<=a and a<=7 and 0<=b and b<=7:
              if board[a][b].islower() or board[a][b]==' ':
                     if TEST(a,b,0)==0:
                            t=1
                     if TESTPAWNC(a, b, 0) == 0 and t==1:
                            if mode == 1:
                                   paths[a][b] = '*'
                            else:
                                   valid_pos.append([a, b])
       b = b + 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].islower() or board[a][b] == ' ':
                     if TEST(a, b, 0) == 0:
                            t=1
                     if TESTPAWNC(a, b, 0) == 0 and t==1:
                            if mode == 1:
                                   paths[a][b] = '*'
                            else:
                                   valid_pos.append([a, b])
       b = b + 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].islower() or board[a][b] == ' ':
                     if TEST(a, b, 0) == 0:
                            t=1
                     if TESTPAWNC(a, b, 0) == 0 and t==1:
                            if mode == 1:
                                   paths[a][b] = '*'
                            else:
                                   valid_pos.append([a, b])
       a = a + 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].islower() or board[a][b] == ' ':
                     if TEST(a, b, 0) == 0:
                            t=1
                     if TESTPAWNC(a, b, 0) == 0 and t==1:
                            if mode == 1:
                                   paths[a][b] = '*'
                            else:
                                   valid_pos.append([a, b])
       a = a + 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].islower() or board[a][b] == ' ':
                     if TEST(a, b, 0) == 0:
                            t=1
                     if TESTPAWNC(a, b, 0) == 0 and t==1:
                            if mode == 1:
                                   paths[a][b] = '*'
                            else:
                                   valid_pos.append([a, b])
       b = b - 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].islower() or board[a][b] == ' ':
                     if TEST(a, b, 0) == 0:
                            t=1
                     if TESTPAWNC(a, b, 0) == 0 and t==1:
                            if mode == 1:
                                   paths[a][b] = '*'
                            else:
                                   valid_pos.append([a, b])
       b = b - 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].islower() or board[a][b] == ' ':
                     if TEST(a, b, 0) == 0:
                            t=1
                     if TESTPAWNC(a, b, 0) == 0 and t==1:
                            if mode == 1:
                                   paths[a][b] = '*'
                            else:
                                   valid_pos.append([a, b])
       a = a - 1
       t=0
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if board[a][b].islower() or board[a][b] == ' ':
                     if TEST(a, b, 0) == 0:
                            t=1
                     if TESTPAWNC(a, b, 0) == 0 and t==1:
                            if mode == 1:
                                   paths[a][b] = '*'
                            else:
                                   valid_pos.append([a, b])
       if c == 0:
              a = inposx
              b = inposy
              if TEST(a, b, 2) == 0 and TESTPAWNC(a, b, 2) == 0:
                     b = b - 1
                     if board[a][b]==' ' and TEST(a, b, 2) == 0 and TESTPAWNC(a, b, 2) == 0:
                            b = b - 1
                            if board[a][b]==' ' and TEST(a, b, 2) == 0 and TESTPAWNC(a, b, 2) == 0:
                                   if board[0][0] == 'R1' and board[0][1] == ' ':
                                          if mode == 1:
                                                 paths[a][b] = '*'
                                          else:
                                                 valid_pos.append([a, b])
                     a = inposx
                     b = inposy
                     b = b + 1
                     if board[a][b]==' ' and TEST(a, b, 2) == 0 and TESTPAWNC(a, b, 2) == 0:
                            b = b + 1
                            if board[a][b]==' ' and TEST(a, b, 2) == 0 and TESTPAWNC(a, b, 2) == 0:
                                   if board[0][7] == 'R2' and board[0][6] == ' ':
                                          if mode == 1:
                                                 paths[a][b] = '*'
                                          else:
                                                 valid_pos.append([a, b])
       delete=0
       delete=intersection(KINGNEIGHBOUR,kingneighbour)
       if len(delete)>0:
              for pos in delete:
                     if mode == 1:
                            paths[pos[0]][pos[1]] = ' '
                     else:
                            if pos in valid_pos:
                                   valid_pos.remove(pos)
       a = inposx
       b = inposy
       a = a - 1
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*' or ([a,b] in valid_pos):
                     bsurround[15] = 1
       b = b + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*' or ([a,b] in valid_pos):
                     bsurround[15] = 1
       b = b + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*' or ([a,b] in valid_pos):
                     bsurround[15] = 1
       a = a + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*' or ([a,b] in valid_pos):
                     bsurround[15] = 1
       a = a + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*' or ([a,b] in valid_pos):
                     bsurround[15] = 1
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*' or ([a,b] in valid_pos):
                     bsurround[15] = 1
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*' or ([a,b] in valid_pos):
                     bsurround[15] = 1
       a = a - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*' or ([a,b] in valid_pos):
                     bsurround[15] = 1

def FIND_KINGNEIGHBOUR(a,b):
       KINGNEIGHBOUR.clear()
       a = a - 1
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              KINGNEIGHBOUR.append([a, b])
       b = b + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              KINGNEIGHBOUR.append([a, b])
       b = b + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              KINGNEIGHBOUR.append([a, b])
       a = a + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              KINGNEIGHBOUR.append([a, b])
       a = a + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              KINGNEIGHBOUR.append([a, b])
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              KINGNEIGHBOUR.append([a, b])
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              KINGNEIGHBOUR.append([a, b])
       a = a - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              KINGNEIGHBOUR.append([a, b])
def pawnrestore(a,b,c,d):
       if c!=9:
              a=a-1
              b=b-1
              if a>=0 and b>=0:
                     if paths[a][b]=='*':
                            paths[a][b]=' '
              b=b+1
              if a>=0:
                     if paths[a][b]=='*':
                            paths[a][b]=' '
              b=b+1
              if b<=7 and a>=0:
                     if paths[a][b]=='*':
                            paths[a][b]=' '
              a=a-1
              b=b-1
              if a>=0:
                     if paths[a][b]=='*':
                            paths[a][b]=' '
       else:
              if d<=15:
                     for pos in wdefend_pos[d]:
                            paths[pos[0]][pos[1]]=' '
              else:
                     for pos in bdefend_pos[d-16]:
                            paths[pos[0]][pos[1]]=' '
def bishoprestore(a,b,c,d):
       if c!=9:
              inposx = a
              inposy = b
              a=a-1
              b=b-1
              while 0<=a and 0<=b and paths[a][b]=='*':
                     paths[a][b] = ' '
                     a = a - 1
                     b = b - 1
              a = inposx
              b = inposy
              a = a - 1
              b = b + 1
              while 0 <= a and b <= 7 and paths[a][b] == '*':
                     paths[a][b] = ' '
                     a = a - 1
                     b = b + 1
              a = inposx
              b = inposy
              a = a + 1
              b = b + 1
              while a <= 7 and b <= 7 and paths[a][b] == '*':
                     paths[a][b] = ' '
                     a = a + 1
                     b = b + 1
              a = inposx
              b = inposy
              a = a + 1
              b = b - 1
              while a <= 7 and 0 <= b and paths[a][b] == '*':
                     paths[a][b] = ' '
                     a = a + 1
                     b = b - 1
       else:
              if d<=15:
                     for pos in wdefend_pos[d]:
                            paths[pos[0]][pos[1]]=' '
              else:
                     for pos in bdefend_pos[d-16]:
                            paths[pos[0]][pos[1]]=' '
def rookrestore(a,b,c,d):
       if c!=9:
              inposx = a
              inposy = b
              a=a-1
              while 0 <= a and paths[a][b]=='*':
                     paths[a][b]=' '
                     a=a-1
              a = inposx
              b = inposy
              b=b+1
              while b <= 7 and paths[a][b] == '*':
                     paths[a][b] = ' '
                     b = b + 1
              a = inposx
              b = inposy
              b = b - 1
              while 0 <= b and paths[a][b] == '*':
                     paths[a][b] = ' '
                     b = b - 1
              a = inposx
              b = inposy
              a = a + 1
              while a <= 7 and paths[a][b] == '*':
                     paths[a][b] = ' '
                     a = a + 1
       else:
              if d<=15:
                     for pos in wdefend_pos[d]:
                            paths[pos[0]][pos[1]]=' '
              else:
                     for pos in bdefend_pos[d-16]:
                            paths[pos[0]][pos[1]]=' '
def knightrestore(a,b,c,d):
       if c!=9:
              b=b-2
              a=a-1
              if 0<=a and a<=7 and 0<=b and b<=7:
                     if paths[a][b]=='*':
                            paths[a][b]=' '
              b = b + 1
              a = a - 1
              if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                     if paths[a][b] == '*':
                            paths[a][b] = ' '
              b = b + 2
              if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                     if paths[a][b] == '*':
                            paths[a][b] = ' '
              b = b + 1
              a = a + 1
              if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                     if paths[a][b] == '*':
                            paths[a][b] = ' '
              a = a + 2
              if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                     if paths[a][b] == '*':
                            paths[a][b] = ' '
              b = b - 1
              a = a + 1
              if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                     if paths[a][b] == '*':
                            paths[a][b] = ' '
              b = b - 2
              if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                     if paths[a][b] == '*':
                            paths[a][b] = ' '
              b = b - 1
              a = a - 1
              if 0 <= a and a <= 7 and 0 <= b and b <= 7:
                     if paths[a][b] == '*':
                            paths[a][b] = ' '
       else:
              if d<=15:
                     for pos in wdefend_pos[d]:
                            paths[pos[0]][pos[1]]=' '
              else:
                     for pos in bdefend_pos[d-16]:
                            paths[pos[0]][pos[1]]=' '
def queenrestore(a,b,c,d):
       if c!=9:
              inposx = a
              inposy = b
              a=a-1
              b=b-1
              while 0<=a and 0<=b and paths[a][b]=='*':
                     paths[a][b] = ' '
                     a = a - 1
                     b = b - 1
              a = inposx
              b = inposy
              a = a - 1
              b = b + 1
              while 0 <= a and b <= 7 and paths[a][b] == '*':
                     paths[a][b] = ' '
                     a = a - 1
                     b = b + 1
              a = inposx
              b = inposy
              a = a + 1
              b = b + 1
              while a <= 7 and b <= 7 and paths[a][b] == '*':
                     paths[a][b] = ' '
                     a = a + 1
                     b = b + 1
              a = inposx
              b = inposy
              a = a + 1
              b = b - 1
              while a <= 7 and 0 <= b and paths[a][b] == '*':
                     paths[a][b] = ' '
                     a = a + 1
                     b = b - 1
              a = inposx
              b = inposy
              a=a-1
              while 0 <= a and paths[a][b]=='*':
                     paths[a][b]=' '
                     a=a-1
              a = inposx
              b = inposy
              b=b+1
              while b <= 7 and paths[a][b] == '*':
                     paths[a][b] = ' '
                     b = b + 1
              a = inposx
              b = inposy
              b = b - 1
              while 0 <= b and paths[a][b] == '*':
                     paths[a][b] = ' '
                     b = b - 1
              a = inposx
              b = inposy
              a = a + 1
              while a <= 7 and paths[a][b] == '*':
                     paths[a][b] = ' '
                     a = a + 1
       else:
              if d<=15:
                     for pos in wdefend_pos[d]:
                            paths[pos[0]][pos[1]]=' '
              else:
                     for pos in bdefend_pos[d-16]:
                            paths[pos[0]][pos[1]]=' '
def kingrestore(a,b):
       inposx = a
       inposy = b
       a=a-1
       b=b-1
       if 0<=a and a<=7 and 0<=b and b<=7:
              if paths[a][b]=='*':
                     paths[a][b]=' '
       b = b + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     paths[a][b] = ' '
       b = b + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     paths[a][b] = ' '
       a = a + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     paths[a][b] = ' '
       a = a + 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     paths[a][b] = ' '
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     paths[a][b] = ' '
       b = b - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     paths[a][b] = ' '
       a = a - 1
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     paths[a][b] = ' '
       a = inposx
       b = inposy
       b = b - 2
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     paths[a][b] = ' '
       a = inposx
       b = inposy
       b = b + 2
       if 0 <= a and a <= 7 and 0 <= b and b <= 7:
              if paths[a][b] == '*':
                     paths[a][b] = ' '
def PAWNRESTORE(a,b,c,d):
       if c!=9:
              a=a+1
              b=b-1
              if a<=7 and b>=0:
                     if paths[a][b]=='*':
                            paths[a][b]=' '
              b=b+1
              if a<=7:
                     if paths[a][b]=='*':
                            paths[a][b]=' '
              b=b+1
              if a<=7 and b<=7:
                     if paths[a][b]=='*':
                            paths[a][b]=' '
              a=a+1
              b=b-1
              if a <= 7:
                     if paths[a][b]=='*':
                            paths[a][b]=' '
       else:
              if d<=15:
                     for pos in wdefend_pos[d]:
                            paths[pos[0]][pos[1]]=' '
              else:
                     for pos in bdefend_pos[d-16]:
                            paths[pos[0]][pos[1]]=' '
def change_state(piece,dir):
       if piece=='p1':
              if dir==2 :
                     wpos[0][2]=2
              elif dir==9:
                     wpos[0][2]=9
              elif dir==1:
                     wpos[0][2]=3
              elif dir==3:
                     wpos[0][2]=4
              else:
                     wpos[0][2]=0
       elif piece=='p2':
              if dir==2 :
                     wpos[1][2]=2
              elif dir==9:
                     wpos[1][2]=9
              elif dir==1:
                     wpos[1][2]=3
              elif dir==3:
                     wpos[1][2]=4
              else:
                     wpos[1][2]=0
       elif piece=='p3':
              if dir==2 :
                     wpos[2][2]=2
              elif dir==9:
                     wpos[2][2]=9
              elif dir==1:
                     wpos[2][2]=3
              elif dir==3:
                     wpos[2][2]=4
              else:
                     wpos[2][2]=0
       elif piece=='p4':
              if dir==2 :
                     wpos[3][2]=2
              elif dir==9:
                     wpos[3][2]=9
              elif dir==1:
                     wpos[3][2]=3
              elif dir==3:
                     wpos[3][2]=4
              else:
                     wpos[3][2]=0
       elif piece=='p5':
              if dir==2 :
                     wpos[4][2]=2
              elif dir==9:
                     wpos[4][2]=9
              elif dir==1:
                     wpos[4][2]=3
              elif dir==3:
                     wpos[4][2]=4
              else:
                     wpos[4][2]=0
       elif piece=='p6':
              if dir==2 :
                     wpos[5][2]=2
              elif dir==9:
                     wpos[5][2]=9
              elif dir==1:
                     wpos[5][2]=3
              elif dir==3:
                     wpos[5][2]=4
              else:
                     wpos[5][2]=0
       elif piece=='p7':
              if dir==2 :
                     wpos[6][2]=2
              elif dir==9:
                     wpos[6][2]=9
              elif dir==1:
                     wpos[6][2]=3
              elif dir==3:
                     wpos[6][2]=4
              else:
                     wpos[6][2]=0
       elif piece=='p8':
              if dir==2 :
                     wpos[7][2]=2
              elif dir==9:
                     wpos[7][2]=9
              elif dir==1:
                     wpos[7][2]=3
              elif dir==3:
                     wpos[7][2]=4
              else:
                     wpos[7][2]=0
       elif piece=='n1':
              if dir!=9:
                     wpos[10][2]=0
              else:
                     wpos[10][2]=9
       elif piece=='n2':
              if dir!=9:
                     wpos[11][2]=0
              else:
                     wpos[11][2]=9
       elif piece=='r1':
              if dir==2 or dir==6:
                     wpos[8][2]=2
              elif dir == 4 or dir == 8:
                     wpos[8][2]=3
              elif dir==9:
                     wpos[8][2]=9
              else:
                     wpos[8][2]=0
       elif piece=='r2':
              if dir==2 or dir==6:
                     wpos[9][2]=2
              elif dir == 4 or dir == 8:
                     wpos[9][2]=3
              elif dir==9:
                     wpos[9][2]=9
              else:
                     wpos[9][2]=0
       elif piece=='b1':
              if dir==1 or dir==5:
                     wpos[12][2]=2
              elif dir==3 or dir==7:
                     wpos[12][2]=3
              elif dir==9:
                     wpos[12][2]=9
              else:
                     wpos[12][2]=0
       elif piece=='b2':
              if dir==1 or dir==5:
                     wpos[13][2]=2
              elif dir==3 or dir==7:
                     wpos[13][2]=3
              elif dir==9:
                     wpos[13][2]=9
              else:
                     wpos[13][2]=0
       elif piece=='q1':
              if dir==2 or dir==6:
                     wpos[14][2]=4
              elif dir == 4 or dir == 8:
                     wpos[14][2]=5
              elif dir==1 or dir==5:
                     wpos[14][2]=2
              elif dir==3 or dir==7:
                     wpos[14][2]=3
              elif dir==9:
                     wpos[14][2]=9
       elif piece=='q2':
              if dir==2 or dir==6:
                     wpos[16][2]=4
              elif dir == 4 or dir == 8:
                     wpos[16][2]=5
              elif dir==1 or dir==5:
                     wpos[16][2]=2
              elif dir==3 or dir==7:
                     wpos[16][2]=3
              elif dir==9:
                     wpos[16][2]=9
       elif piece=='q3':
              if dir==2 or dir==6:
                     wpos[17][2]=4
              elif dir == 4 or dir == 8:
                     wpos[17][2]=5
              elif dir==1 or dir==5:
                     wpos[17][2]=2
              elif dir==3 or dir==7:
                     wpos[17][2]=3
              elif dir==9:
                     wpos[17][2]=9
       elif piece=='q4':
              if dir==2 or dir==6:
                     wpos[18][2]=4
              elif dir == 4 or dir == 8:
                     wpos[18][2]=5
              elif dir==1 or dir==5:
                     wpos[18][2]=2
              elif dir==3 or dir==7:
                     wpos[18][2]=3
              elif dir==9:
                     wpos[18][2]=9
       elif piece=='q5':
              if dir==2 or dir==6:
                     wpos[19][2]=4
              elif dir == 4 or dir == 8:
                     wpos[19][2]=5
              elif dir==1 or dir==5:
                     wpos[19][2]=2
              elif dir==3 or dir==7:
                     wpos[19][2]=3
              elif dir==9:
                     wpos[19][2]=9
       elif piece=='q6':
              if dir==2 or dir==6:
                     wpos[20][2]=4
              elif dir == 4 or dir == 8:
                     wpos[20][2]=5
              elif dir==1 or dir==5:
                     wpos[20][2]=2
              elif dir==3 or dir==7:
                     wpos[20][2]=3
              elif dir==9:
                     wpos[20][2]=9
       elif piece=='q7':
              if dir==2 or dir==6:
                     wpos[21][2]=4
              elif dir == 4 or dir == 8:
                     wpos[21][2]=5
              elif dir==1 or dir==5:
                     wpos[21][2]=2
              elif dir==3 or dir==7:
                     wpos[21][2]=3
              elif dir==9:
                     wpos[21][2]=9
       elif piece=='q8':
              if dir==2 or dir==6:
                     wpos[22][2]=4
              elif dir == 4 or dir == 8:
                     wpos[22][2]=5
              elif dir==1 or dir==5:
                     wpos[22][2]=2
              elif dir==3 or dir==7:
                     wpos[22][2]=3
              elif dir==9:
                     wpos[22][2]=9
       elif piece=='q9':
              if dir==2 or dir==6:
                     wpos[23][2]=4
              elif dir == 4 or dir == 8:
                     wpos[23][2]=5
              elif dir==1 or dir==5:
                     wpos[23][2]=2
              elif dir==3 or dir==7:
                     wpos[23][2]=3
              elif dir==9:
                     wpos[23][2]=9
def check():
       ch = 0
       a=wpos[15][0]
       b=wpos[15][1]
       a=a-1
       b=b-1
       global wblockpieces
       global wdir
       global block_wdir
       if 0<=a and 0<=b and board[a][b][0]=='P':
              ch=1
              wdir=1
              CHECKPIECE[0]=a
              CHECKPIECE[1]=b
       else:
              while 0<=a and 0<=b:
                     if board[a][b].islower() :
                            block_wdir=1
                            wblockpieces = board[a][b]
                            break
                     elif board[a][b][0]=='Q' or board[a][b][0]=='B':
                            ch=1
                            wdir=1
                            CHECKPIECE[0]=a
                            CHECKPIECE[1]=b
                            break
                     elif board[a][b].isupper():
                            break
                     else:
                            a=a-1
                            b=b-1
              if block_wdir!=0:
                     a=a-1
                     b=b-1
                     while 0 <= a and 0 <= b:
                            if board[a][b].islower():
                                   block_wdir=0
                                   wblockpieces=0
                                   break
                            elif board[a][b][0]=='Q' or board[a][b][0]=='B':
                                   change_state(wblockpieces,block_wdir)
                                   block_wdir = 0
                                   wblockpieces = 0
                                   break
                            elif board[a][b].isupper():
                                   block_wdir = 0
                                   wblockpieces = 0
                                   break
                            else:
                                   a=a-1
                                   b=b-1
                     if block_wdir!=0:
                            block_wdir = 0
                            wblockpieces = 0
       a = wpos[15][0]
       b = wpos[15][1]
       a = a - 1
       while 0 <= a :
              if board[a][b].islower():
                     block_wdir = 2
                     wblockpieces = board[a][b]
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'R':
                     ch = 1
                     wdir = 2
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
                     break
              elif board[a][b].isupper():
                     break
              else:
                     a = a - 1
       if block_wdir != 0:
              a = a - 1
              while 0 <= a :
                     if board[a][b].islower():
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     elif board[a][b][0] == 'Q' or board[a][b][0] == 'R':
                            change_state(wblockpieces, block_wdir)
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     elif board[a][b].isupper():
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     else:
                            a = a - 1
              if block_wdir != 0:
                     block_wdir = 0
                     wblockpieces = 0
       a = wpos[15][0]
       b = wpos[15][1]
       a = a - 1
       b = b + 1
       if 0<=a and b<=7 and board[a][b][0]=='P':
              ch=1
              wdir=3
              CHECKPIECE[0]=a
              CHECKPIECE[1]=b
       else:
              while 0<=a and b<=7:
                     if board[a][b].islower() :
                            block_wdir=3
                            wblockpieces = board[a][b]
                            break
                     elif board[a][b][0]=='Q' or board[a][b][0]=='B':
                            ch=1
                            wdir=3
                            CHECKPIECE[0]=a
                            CHECKPIECE[1]=b
                            break
                     elif board[a][b].isupper():
                            break
                     else:
                            a=a-1
                            b=b+1
              if block_wdir!=0:
                     a=a-1
                     b=b+1
                     while 0 <= a and b <= 7:
                            if board[a][b].islower():
                                   block_wdir=0
                                   wblockpieces=0
                                   break
                            elif board[a][b][0]=='Q' or board[a][b][0]=='B':
                                   change_state(wblockpieces,block_wdir)
                                   block_wdir = 0
                                   wblockpieces = 0
                                   break
                            elif board[a][b].isupper():
                                   block_wdir = 0
                                   wblockpieces = 0
                                   break
                            else:
                                   a=a-1
                                   b=b+1
                     if block_wdir!=0:
                            block_wdir = 0
                            wblockpieces = 0
       a = wpos[15][0]
       b = wpos[15][1]
       b = b + 1
       while b <= 7:
              if board[a][b].islower():
                     block_wdir = 4
                     wblockpieces = board[a][b]
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'R':
                     ch = 1
                     wdir = 4
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
                     break
              elif board[a][b].isupper():
                     break
              else:
                     b = b + 1
       if block_wdir != 0:
              b = b + 1
              while b <= 7:
                     if board[a][b].islower():
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     elif board[a][b][0] == 'Q' or board[a][b][0] == 'R':
                            change_state(wblockpieces, block_wdir)
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     elif board[a][b].isupper():
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     else:
                            b= b + 1
              if block_wdir != 0:
                     block_wdir = 0
                     wblockpieces = 0
       a = wpos[15][0]
       b = wpos[15][1]
       a = a + 1
       b = b + 1
       while a <= 7 and b <= 7:
              if board[a][b].islower():
                     block_wdir = 5
                     wblockpieces = board[a][b]
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'B':
                     ch = 1
                     wdir = 5
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
                     break
              elif board[a][b].isupper():
                     break
              else:
                     a = a + 1
                     b = b + 1
       if block_wdir != 0:
              a = a + 1
              b = b + 1
              while a <= 7 and b <= 7:
                     if board[a][b].islower():
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     elif board[a][b][0] == 'Q' or board[a][b][0] == 'B':
                            change_state(wblockpieces, block_wdir)
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     elif board[a][b].isupper():
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     else:
                            a = a + 1
                            b = b + 1
              if block_wdir != 0:
                     block_wdir = 0
                     wblockpieces = 0
       a = wpos[15][0]
       b = wpos[15][1]
       a = a + 1
       while a <= 7:
              if board[a][b].islower():
                     block_wdir = 6
                     wblockpieces = board[a][b]
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'R':
                     ch = 1
                     wdir = 6
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
                     break
              elif board[a][b].isupper():
                     break
              else:
                     a = a + 1
       if block_wdir != 0:
              a = a + 1
              while a <= 7:
                     if board[a][b].islower():
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     elif board[a][b][0] == 'Q' or board[a][b][0] == 'R':
                            change_state(wblockpieces, block_wdir)
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     elif board[a][b].isupper():
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     else:
                            a = a + 1
              if block_wdir != 0:
                     block_wdir = 0
                     wblockpieces = 0
       a = wpos[15][0]
       b = wpos[15][1]
       a = a + 1
       b = b - 1
       while a <= 7 and 0 <= b:
              if board[a][b].islower():
                     block_wdir = 7
                     wblockpieces = board[a][b]
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'B':
                     ch = 1
                     wdir = 7
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
                     break
              elif board[a][b].isupper():
                     break
              else:
                     a = a + 1
                     b = b - 1
       if block_wdir != 0:
              a = a + 1
              b = b - 1
              while a <= 7 and 0 <= b:
                     if board[a][b].islower():
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     elif board[a][b][0] == 'Q' or board[a][b][0] == 'B':
                            change_state(wblockpieces, block_wdir)
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     elif board[a][b].isupper():
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     else:
                            a = a + 1
                            b = b - 1
              if block_wdir != 0:
                     block_wdir = 0
                     wblockpieces = 0
       a = wpos[15][0]
       b = wpos[15][1]
       b = b - 1
       while 0 <= b:
              if board[a][b].islower():
                     block_wdir = 8
                     wblockpieces = board[a][b]
                     break
              elif board[a][b][0] == 'Q' or board[a][b][0] == 'R':
                     ch = 1
                     wdir = 8
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
                     break
              elif board[a][b].isupper():
                     break
              else:
                     b = b - 1
       if block_wdir != 0:
              b = b - 1
              while 0 <= b:
                     if board[a][b].islower():
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     elif board[a][b][0] == 'Q' or board[a][b][0] == 'R':
                            change_state(wblockpieces, block_wdir)
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     elif board[a][b].isupper():
                            block_wdir = 0
                            wblockpieces = 0
                            break
                     else:
                            b = b - 1
              if block_wdir != 0:
                     block_wdir = 0
                     wblockpieces = 0
       a = wpos[15][0]
       b = wpos[15][1]
       a=a-1
       b=b-2
       if 0<=b and b<=7 and 0<=a and a<=7:
              if board[a][b][0]=='N':
                     ch=1
                     wdir=9
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
       a = a - 1
       b = b + 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     wdir = 9
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
       b = b + 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     wdir = 9
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
       a = a + 1
       b = b + 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     wdir = 9
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
       a = a + 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     wdir = 9
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
       b = b - 1
       a = a + 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     wdir = 9
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
       b = b - 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     wdir = 9
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
       a = a - 1
       b = b - 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'N':
                     ch = 1
                     wdir = 9
                     CHECKPIECE[0] = a
                     CHECKPIECE[1] = b
       return ch
def CHANGE_STATE(piece,dir):
       if piece=='P1':
              if dir==6:
                     bpos[0][2]=2
              elif dir==5:
                     bpos[0][2]=4
              elif dir==7:
                     bpos[0][2]=3
              elif dir==9:
                     bpos[0][2]=9
              else :
                     bpos[0][2]=0
       elif piece=='P2':
              if dir==6:
                     bpos[1][2]=2
              elif dir==5:
                     bpos[1][2]=4
              elif dir==7:
                     bpos[1][2]=3
              elif dir==9:
                     bpos[1][2]=9
              else:
                     bpos[1][2]=0
       elif piece=='P3':
              if dir==6:
                     bpos[2][2]=2
              elif dir==5:
                     bpos[2][2]=4
              elif dir==7:
                     bpos[2][2]=3
              elif dir==9:
                     bpos[2][2]=9
              else:
                     bpos[2][2]=0
       elif piece=='P4':
              if dir==6:
                     bpos[3][2]=2
              elif dir==5:
                     bpos[3][2]=4
              elif dir==7:
                     bpos[3][2]=3
              elif dir==9:
                     bpos[3][2]=9
              else:
                     bpos[3][2]=0
       elif piece=='P5':
              if dir==6:
                     bpos[4][2]=2
              elif dir==5:
                     bpos[4][2]=4
              elif dir==7:
                     bpos[4][2]=3
              elif dir==9:
                     bpos[4][2]=9
              else:
                     bpos[4][2]=0
       elif piece=='P6':
              if dir==6:
                     bpos[5][2]=2
              elif dir==5:
                     bpos[5][2]=4
              elif dir==7:
                     bpos[5][2]=3
              elif dir==9:
                     bpos[5][2]=9
              else:
                     bpos[5][2]=0
       elif piece=='P7':
              if dir==6:
                     bpos[6][2]=2
              elif dir==5:
                     bpos[6][2]=4
              elif dir==7:
                     bpos[6][2]=3
              elif dir==9:
                     bpos[6][2]=9
              else:
                     bpos[6][2]=0
       elif piece=='P8':
              if dir==6:
                     bpos[7][2]=2
              elif dir==5:
                     bpos[7][2]=4
              elif dir==7:
                     bpos[7][2]=3
              elif dir==9:
                     bpos[7][2]=9
              else:
                     bpos[7][2]=0
       elif piece=='N1':
              if dir==9:
                     bpos[10][2]=9
              else:
                     bpos[10][2]=0
       elif piece=='N2':
              if dir==9:
                     bpos[11][2]=9
              else:
                     bpos[11][2]=0
       elif piece=='R1':
              if dir==2 or dir==6:
                     bpos[8][2]=2
              elif dir == 4 or dir == 8:
                     bpos[8][2]=3
              elif dir==9:
                     bpos[8][2]=9
              else:
                     bpos[8][2]=0
       elif piece=='R2':
              if dir==2 or dir==6:
                     bpos[9][2]=2
              elif dir == 4 or dir == 8:
                     bpos[9][2]=3
              elif dir==9:
                     bpos[9][2]=9
              else:
                     bpos[9][2]=0
       elif piece=='B1':
              if dir==1 or dir==5:
                     bpos[12][2]=2
              elif dir==3 or dir==7:
                     bpos[12][2]=3
              elif dir==9:
                     bpos[12][2]=9
              else:
                     bpos[12][2]=0
       elif piece=='B2':
              if dir==1 or dir==5:
                     bpos[13][2]=2
              elif dir==3 or dir==7:
                     bpos[13][2]=3
              elif dir==9:
                     bpos[13][2]=9
              else:
                     bpos[13][2]=0
       elif piece=='Q1':
              if dir==2 or dir==6:
                     bpos[14][2]=4
              elif dir == 4 or dir == 8:
                     bpos[14][2]=5
              elif dir==1 or dir==5:
                     bpos[14][2]=2
              elif dir==3 or dir==7:
                     bpos[14][2]=3
              elif dir==9:
                     bpos[14][2]=9
       elif piece=='Q2':
              if dir==2 or dir==6:
                     bpos[16][2]=4
              elif dir == 4 or dir == 8:
                     bpos[16][2]=5
              elif dir==1 or dir==5:
                     bpos[16][2]=2
              elif dir==3 or dir==7:
                     bpos[16][2]=3
              elif dir==9:
                     bpos[16][2]=9
       elif piece=='Q3':
              if dir==2 or dir==6:
                     bpos[17][2]=4
              elif dir == 4 or dir == 8:
                     bpos[17][2]=5
              elif dir==1 or dir==5:
                     bpos[17][2]=2
              elif dir==3 or dir==7:
                     bpos[17][2]=3
              elif dir==9:
                     bpos[17][2]=9
       elif piece=='Q4':
              if dir==2 or dir==6:
                     bpos[18][2]=4
              elif dir == 4 or dir == 8:
                     bpos[18][2]=5
              elif dir==1 or dir==5:
                     bpos[18][2]=2
              elif dir==3 or dir==7:
                     bpos[18][2]=3
              elif dir==9:
                     bpos[18][2]=9
       elif piece=='Q5':
              if dir==2 or dir==6:
                     bpos[19][2]=4
              elif dir == 4 or dir == 8:
                     bpos[19][2]=5
              elif dir==1 or dir==5:
                     bpos[19][2]=2
              elif dir==3 or dir==7:
                     bpos[19][2]=3
              elif dir==9:
                     bpos[19][2]=9
       elif piece=='Q6':
              if dir==2 or dir==6:
                     bpos[20][2]=4
              elif dir == 4 or dir == 8:
                     bpos[20][2]=5
              elif dir==1 or dir==5:
                     bpos[20][2]=2
              elif dir==3 or dir==7:
                     bpos[20][2]=3
              elif dir==9:
                     bpos[20][2]=9
       elif piece=='Q7':
              if dir==2 or dir==6:
                     bpos[21][2]=4
              elif dir == 4 or dir == 8:
                     bpos[21][2]=5
              elif dir==1 or dir==5:
                     bpos[21][2]=2
              elif dir==3 or dir==7:
                     bpos[21][2]=3
              elif dir==9:
                     bpos[21][2]=9
       elif piece=='Q8':
              if dir==2 or dir==6:
                     bpos[22][2]=4
              elif dir == 4 or dir == 8:
                     bpos[22][2]=5
              elif dir==1 or dir==5:
                     bpos[22][2]=2
              elif dir==3 or dir==7:
                     bpos[22][2]=3
              elif dir==9:
                     bpos[22][2]=9
       elif piece=='Q9':
              if dir==2 or dir==6:
                     bpos[23][2]=4
              elif dir == 4 or dir == 8:
                     bpos[23][2]=5
              elif dir==1 or dir==5:
                     bpos[23][2]=2
              elif dir==3 or dir==7:
                     bpos[23][2]=3
              elif dir==9:
                     bpos[23][2]=9
def CHECK():
       ch = 0
       a = bpos[15][0]
       b = bpos[15][1]
       a = a - 1
       b = b - 1
       global bblockpieces
       global bdir
       global block_bdir
       while 0 <= a and 0 <= b:
              if board[a][b].isupper():
                     block_bdir = 1
                     bblockpieces = board[a][b]
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'b':
                     ch = 1
                     bdir = 1
                     checkpiece[0] = a
                     checkpiece[1] = b
                     break
              elif board[a][b].islower():
                     break
              else:
                     a = a - 1
                     b = b - 1
       if block_bdir != 0:
              a = a - 1
              b = b - 1
              while 0 <= a and 0 <= b:
                     if board[a][b].isupper():
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     elif board[a][b][0] == 'q' or board[a][b][0] == 'b':
                            CHANGE_STATE(bblockpieces, block_bdir)
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     elif board[a][b].islower():
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     else:
                            a = a - 1
                            b = b - 1
              if block_bdir != 0:
                     block_bdir = 0
                     bblockpieces = 0
       a = bpos[15][0]
       b = bpos[15][1]
       a = a - 1
       while 0 <= a:
              if board[a][b].isupper():
                     block_bdir = 2
                     bblockpieces = board[a][b]
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'r':
                     ch = 1
                     bdir = 2
                     checkpiece[0] = a
                     checkpiece[1] = b
                     break
              elif board[a][b].islower():
                     break
              else:
                     a = a - 1
       if block_bdir != 0:
              a = a - 1
              while 0 <= a:
                     if board[a][b].isupper():
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     elif board[a][b][0] == 'q' or board[a][b][0] == 'r':
                            CHANGE_STATE(bblockpieces, block_bdir)
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     elif board[a][b].islower():
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     else:
                            a = a - 1
              if block_bdir != 0:
                     block_bdir = 0
                     bblockpieces = 0
       a = bpos[15][0]
       b = bpos[15][1]
       a = a - 1
       b = b + 1
       while 0 <= a and b <= 7:
              if board[a][b].isupper():
                     block_bdir = 3
                     bblockpieces = board[a][b]
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'b':
                     ch = 1
                     bdir = 3
                     checkpiece[0] = a
                     checkpiece[1] = b
                     break
              elif board[a][b].islower():
                     break
              else:
                     a = a - 1
                     b = b + 1
       if block_bdir != 0:
              a = a - 1
              b = b + 1
              while 0 <= a and b <= 7:
                     if board[a][b].isupper():
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     elif board[a][b][0] == 'q' or board[a][b][0] == 'b':
                            CHANGE_STATE(bblockpieces, block_bdir)
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     elif board[a][b].islower():
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     else:
                            a = a - 1
                            b = b + 1
              if block_bdir != 0:
                     block_bdir = 0
                     bblockpieces = 0
       a = bpos[15][0]
       b = bpos[15][1]
       b = b + 1
       while b <= 7:
              if board[a][b].isupper():
                     block_bdir = 4
                     bblockpieces = board[a][b]
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'r':
                     ch = 1
                     bdir = 4
                     checkpiece[0] = a
                     checkpiece[1] = b
                     break
              elif board[a][b].islower():
                     break
              else:
                     b = b + 1
       if block_bdir != 0:
              b = b + 1
              while b <= 7:
                     if board[a][b].isupper():
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     elif board[a][b][0] == 'q' or board[a][b][0] == 'r':
                            CHANGE_STATE(bblockpieces, block_bdir)
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     elif board[a][b].islower():
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     else:
                            b = b + 1
              if block_bdir != 0:
                     block_bdir = 0
                     bblockpieces = 0
       a = bpos[15][0]
       b = bpos[15][1]
       a = a + 1
       b = b + 1
       if a<=7 and b<=7 and board[a][b][0]=='p':
              ch=1
              bdir=5
              checkpiece[0]=a
              checkpiece[1]=b
       else:
              while a <= 7 and b <= 7:
                     if board[a][b].isupper():
                            block_bdir = 5
                            bblockpieces = board[a][b]
                            break
                     elif board[a][b][0] == 'q' or board[a][b][0] == 'b':
                            ch = 1
                            bdir = 5
                            checkpiece[0] = a
                            checkpiece[1] = b
                            break
                     elif board[a][b].islower():
                            break
                     else:
                            a = a + 1
                            b = b + 1
              if block_bdir != 0:
                     a = a + 1
                     b = b + 1
                     while a <= 7 and b <= 7:
                            if board[a][b].isupper():
                                   block_bdir = 0
                                   bblockpieces = 0
                                   break
                            elif board[a][b][0] == 'q' or board[a][b][0] == 'b':
                                   CHANGE_STATE(bblockpieces, block_bdir)
                                   block_bdir = 0
                                   bblockpieces = 0
                                   break
                            elif board[a][b].islower():
                                   block_bdir = 0
                                   bblockpieces = 0
                                   break
                            else:
                                   a = a + 1
                                   b = b + 1
                     if block_bdir != 0:
                            block_bdir = 0
                            bblockpieces = 0
       a = bpos[15][0]
       b = bpos[15][1]
       a = a + 1
       while a <= 7:
              if board[a][b].isupper():
                     block_bdir = 6
                     bblockpieces = board[a][b]
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'r':
                     ch = 1
                     bdir = 6
                     checkpiece[0] = a
                     checkpiece[1] = b
                     break
              elif board[a][b].islower():
                     break
              else:
                     a = a + 1
       if block_bdir != 0:
              a = a + 1
              while a <= 7:
                     if board[a][b].isupper():
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     elif board[a][b][0] == 'q' or board[a][b][0] == 'r':
                            CHANGE_STATE(bblockpieces, block_bdir)
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     elif board[a][b].islower():
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     else:
                            a = a + 1
              if block_bdir != 0:
                     block_bdir = 0
                     bblockpieces = 0

       a = bpos[15][0]
       b = bpos[15][1]
       a = a + 1
       b = b - 1
       if a<=7 and 0<=b and board[a][b][0]=='p':
              ch=1
              bdir=7
              checkpiece[0]=a
              checkpiece[1]=b
       else:
              while a <= 7 and 0 <= b:
                     if board[a][b].isupper():
                            block_bdir = 7
                            bblockpieces = board[a][b]
                            break
                     elif board[a][b][0] == 'q' or board[a][b][0] == 'b':
                            ch = 1
                            bdir = 7
                            checkpiece[0] = a
                            checkpiece[1] = b
                            break
                     elif board[a][b].islower():
                            break
                     else:
                            a = a + 1
                            b = b - 1
              if block_bdir != 0:
                     a = a + 1
                     b = b - 1
                     while a <= 7 and 0 <= b:
                            if board[a][b].isupper():
                                   block_bdir = 0
                                   bblockpieces = 0
                                   break
                            elif board[a][b][0] == 'q' or board[a][b][0] == 'b':
                                   CHANGE_STATE(bblockpieces, block_bdir)
                                   block_bdir = 0
                                   bblockpieces = 0
                                   break
                            elif board[a][b].isupper():
                                   block_bdir = 0
                                   bblockpieces = 0
                                   break
                            else:
                                   a = a + 1
                                   b = b - 1
                     if block_bdir != 0:
                            block_bdir = 0
                            bblockpieces = 0
       a = bpos[15][0]
       b = bpos[15][1]
       b = b - 1
       while 0 <= b:
              if board[a][b].isupper():
                     block_bdir = 8
                     bblockpieces = board[a][b]
                     break
              elif board[a][b][0] == 'q' or board[a][b][0] == 'r':
                     ch = 1
                     bdir = 8
                     checkpiece[0] = a
                     checkpiece[1] = b
                     break
              elif board[a][b].islower():
                     break
              else:
                     b = b - 1
       if block_bdir != 0:
              b = b - 1
              while 0 <= b:
                     if board[a][b].isupper():
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     elif board[a][b][0] == 'q' or board[a][b][0] == 'r':
                            CHANGE_STATE(bblockpieces, block_bdir)
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     elif board[a][b].islower():
                            block_bdir = 0
                            bblockpieces = 0
                            break
                     else:
                            b = b - 1
              if block_bdir != 0:
                     block_bdir = 0
                     bblockpieces = 0
       a = bpos[15][0]
       b = bpos[15][1]
       a = a - 1
       b = b - 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     bdir = 9
                     checkpiece[0] = a
                     checkpiece[1] = b
       a = a - 1
       b = b + 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     bdir = 9
                     checkpiece[0] = a
                     checkpiece[1] = b
       b = b + 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     bdir = 9
                     checkpiece[0] = a
                     checkpiece[1] = b
       a = a + 1
       b = b + 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     bdir = 9
                     checkpiece[0] = a
                     checkpiece[1] = b
       a = a + 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     bdir = 9
                     checkpiece[0] = a
                     checkpiece[1] = b
       b = b - 1
       a = a + 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     bdir = 9
                     checkpiece[0] = a
                     checkpiece[1] = b
       b = b - 2
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     bdir = 9
                     checkpiece[0] = a
                     checkpiece[1] = b
       a = a - 1
       b = b - 1
       if 0 <= b and b <= 7 and 0 <= a and a <= 7:
              if board[a][b][0] == 'n':
                     ch = 1
                     bdir = 9
                     checkpiece[0] = a
                     checkpiece[1] = b
       return ch
def pathcheck(a,b):
       pathclear=1
       if bdir==1:
              if test(a,b,1)==1:
                     pathclear=0
              if testpawnc(a,b,1)==1:
                     pathclear = 0
              a = a + 1
              b = b + 1
              while board[a][b]!='K':
                     if test(a, b, 1) == 1:
                            pathclear = 0
                     if testpawns(a, b) == 1:
                            pathclear = 0
                     a = a + 1
                     b = b + 1
       elif bdir==2:
              if test(a,b,1)==1:
                     pathclear=0
              if testpawnc(a,b,1)==1:
                     pathclear = 0
              a = a + 1
              while board[a][b]!='K':
                     if test(a, b, 1) == 1:
                            pathclear = 0
                     if testpawns(a, b) == 1:
                            pathclear = 0
                     a = a + 1
       elif bdir == 3:
              if test(a, b, 1) == 1:
                     pathclear = 0
              if testpawnc(a, b, 1) == 1:
                     pathclear = 0
              a = a + 1
              b = b - 1
              while board[a][b] != 'K':
                     if test(a, b, 1) == 1:
                            pathclear = 0
                     if testpawns(a, b) == 1:
                            pathclear = 0
                     a = a + 1
                     b = b - 1
       elif bdir == 4:
              if test(a, b, 1) == 1:
                     pathclear = 0
              if testpawnc(a, b, 1) == 1:
                     pathclear = 0
              b = b - 1
              while board[a][b] != 'K':
                     if test(a, b, 1) == 1:
                            pathclear = 0
                     if testpawns(a, b) == 1:
                            pathclear = 0
                     b = b - 1
       elif bdir == 5:
              if test(a, b, 1) == 1:
                     pathclear = 0
              if testpawnc(a, b, 1) == 1:
                     pathclear = 0
              a = a - 1
              b = b - 1
              while board[a][b] != 'K':
                     if test(a, b, 1) == 1:
                            pathclear = 0
                     if testpawns(a, b) == 1:
                            pathclear = 0
                     a = a - 1
                     b = b - 1
       elif bdir == 6:
              if test(a, b, 1) == 1:
                     pathclear = 0
              if testpawnc(a, b, 1) == 1:
                     pathclear = 0
              a = a - 1
              while board[a][b] != 'K':
                     if test(a, b, 1) == 1:
                            pathclear = 0
                     if testpawns(a, b) == 1:
                            pathclear = 0
                     a = a - 1
       elif bdir == 7:
              if test(a, b, 1) == 1:
                     pathclear = 0
              if testpawnc(a, b, 1) == 1:
                     pathclear = 0
              a = a - 1
              b = b + 1
              while board[a][b] != 'K':
                     if test(a, b, 1) == 1:
                            pathclear = 0
                     if testpawns(a, b) == 1:
                            pathclear = 0
                     a = a - 1
                     b = b + 1
       elif bdir == 8:
              if test(a, b, 1) == 1:
                     pathclear = 0
              if testpawnc(a, b, 1) == 1:
                     pathclear = 0
              b = b + 1
              while board[a][b] != 'K':
                     if test(a, b, 1) == 1:
                            pathclear = 0
                     if testpawns(a, b) == 1:
                            pathclear = 0
                     b = b + 1
       elif bdir==9:
              if test(a, b, 1) == 1:
                     pathclear = 0
              if testpawnc(a, b, 1) == 1:
                     pathclear = 0
       return pathclear
def PATHCHECK(a,b):
       pathclear=1
       if wdir==1:
              if TEST(a,b,1)==1:
                     pathclear=0
              if TESTPAWNC(a,b,1)==1:
                     pathclear = 0
              a = a + 1
              b = b + 1
              while board[a][b]!='k':
                     if TEST(a, b, 1) == 1:
                            pathclear = 0
                     if TESTPAWNS(a,b)==1:
                            pathclear = 0
                     a = a + 1
                     b = b + 1
       elif wdir==2:
              if TEST(a,b,1)==1:
                     pathclear=0
              if TESTPAWNC(a,b,1)==1:
                     pathclear=0
              a = a + 1
              while board[a][b]!='k':
                     if TEST(a, b, 1) == 1:
                            pathclear = 0
                     if TESTPAWNS(a, b) == 1:
                            pathclear = 0
                     a = a + 1
       elif wdir == 3:
              if TEST(a, b, 1) == 1:
                     pathclear = 0
              if TESTPAWNC(a, b, 1) == 1:
                     pathclear = 0
              a = a + 1
              b = b - 1
              while board[a][b] != 'k':
                     if TEST(a, b, 1) == 1:
                            pathclear = 0
                     if TESTPAWNS(a, b) == 1:
                            pathclear = 0
                     a = a + 1
                     b = b - 1
       elif wdir == 4:
              if TEST(a, b, 1) == 1:
                     pathclear = 0
              if TESTPAWNC(a, b, 1) == 1:
                     pathclear=0
              b = b - 1
              while board[a][b] != 'k':
                     if TEST(a, b, 1) == 1:
                            pathclear = 0
                     if TESTPAWNS(a, b) == 1:
                            pathclear = 0
                     b = b - 1
       elif wdir == 5:
              if TEST(a, b, 1) == 1:
                     pathclear = 0
              if TESTPAWNC(a, b, 1) == 1:
                     pathclear = 0
              a = a - 1
              b = b - 1
              while board[a][b] != 'k':
                     if TEST(a, b, 1) == 1:
                            pathclear = 0
                     if TESTPAWNS(a, b) == 1:
                            pathclear = 0
                     a = a - 1
                     b = b - 1
       elif wdir == 6:
              if TEST(a, b, 1) == 1:
                     pathclear = 0
              if TESTPAWNC(a, b, 1) == 1:
                     pathclear = 0
              a = a - 1
              while board[a][b] != 'k':
                     if TEST(a, b, 1) == 1:
                            pathclear = 0
                     if TESTPAWNS(a, b) == 1:
                            pathclear = 0
                     a = a - 1
       elif wdir == 7:
              if TEST(a, b, 1) == 1:
                     pathclear = 0
              if TESTPAWNC(a, b, 1) == 1:
                     pathclear = 0
              a = a - 1
              b = b + 1
              while board[a][b] != 'k':
                     if TEST(a, b, 1) == 1:
                            pathclear = 0
                     if TESTPAWNS(a, b) == 1:
                            pathclear = 0
                     a = a - 1
                     b = b + 1
       elif wdir == 8:
              if TEST(a, b, 1) == 1:
                     pathclear = 0
              if TESTPAWNC(a, b, 1) == 1:
                     pathclear = 0
              b = b + 1
              while board[a][b] != 'k':
                     if TEST(a, b, 1) == 0:
                            pathclear = 0
                     if TESTPAWNS(a, b) == 1:
                            pathclear = 0
                     b = b + 1
       elif wdir==9:
              if TEST(a, b, 1) == 1:
                     pathclear = 0
              if TESTPAWNC(a, b, 1) == 1:
                     pathclear = 0
       return pathclear
def stalemate():
       for i in range (24):
              if wpos[i][2]!=-1:
                     if board[wpos[i][0]][wpos[i][1]][0]=='p':
                            pawn(wpos[i][0],wpos[i][1],wpos[i][2],i,wem_passent[i])
                            pawnrestore(wpos[i][0],wpos[i][1],wpos[i][2],i)
                     elif board[wpos[i][0]][wpos[i][1]][0]=='r':
                            rook(wpos[i][0],wpos[i][1],wpos[i][2],i)
                            rookrestore(wpos[i][0], wpos[i][1], wpos[i][2], i)
                     elif board[wpos[i][0]][wpos[i][1]][0]=='b':
                            bishop(wpos[i][0], wpos[i][1], wpos[i][2], i)
                            bishoprestore(wpos[i][0], wpos[i][1], wpos[i][2], i)
                     elif board[wpos[i][0]][wpos[i][1]][0]=='n':
                            knight(wpos[i][0], wpos[i][1], wpos[i][2], i)
                            knightrestore(wpos[i][0], wpos[i][1], wpos[i][2], i)
                     elif board[wpos[i][0]][wpos[i][1]][0] == 'q':
                            queen(wpos[i][0], wpos[i][1], wpos[i][2], i)
                            queenrestore(wpos[i][0], wpos[i][1], wpos[i][2], i)
              if wsurround[i]==1:
                     break
       return wsurround[i]
def STALEMATE():
       for i in range (24):
              if bpos[i][2]!=-1:
                     if board[bpos[i][0]][bpos[i][1]][0]=='P':
                            PAWN(bpos[i][0],bpos[i][1],bpos[i][2],i,bem_passent[i],1)
                            PAWNRESTORE(bpos[i][0],bpos[i][1],bpos[i][2],i)
                     elif board[bpos[i][0]][bpos[i][1]][0]=='R':
                            ROOK(bpos[i][0],bpos[i][1],bpos[i][2],i,1)
                            rookrestore(bpos[i][0], bpos[i][1], bpos[i][2], i)
                     elif board[bpos[i][0]][bpos[i][1]][0]=='B':
                            BISHOP(bpos[i][0], bpos[i][1], bpos[i][2], i,1)
                            bishoprestore(bpos[i][0], bpos[i][1], bpos[i][2], i)
                     elif board[bpos[i][0]][bpos[i][1]][0]=='N':
                            KNIGHT(bpos[i][0], bpos[i][1], bpos[i][2], i,1)
                            knightrestore(bpos[i][0], bpos[i][1], bpos[i][2], i)
                     elif board[bpos[i][0]][bpos[i][1]][0] == 'Q':
                            QUEEN(bpos[i][0], bpos[i][1], bpos[i][2], i,1)
                            queenrestore(bpos[i][0], bpos[i][1], bpos[i][2], i)
              if bsurround[i]==1:
                     break
       return bsurround[i]
