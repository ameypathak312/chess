import pygame
from chess_func import *
from random import randint
from time import sleep
pygame.init()
display_width=800
display_height=700
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Chess')
clock=pygame.time.Clock()
off=False
stop=0
wpawnimg=pygame.image.load(r'chess images\wpawn.png')
bpawnimg=pygame.image.load(r'chess images\bpawn.png')
wbishopimg=pygame.image.load(r'chess images\wbishop.png')
bbishopimg=pygame.image.load(r'chess images\bbishop.png')
wknightimg=pygame.image.load(r'chess images\wknight.png')
bknightimg=pygame.image.load(r'chess images\bknight.png')
wrookimg=pygame.image.load(r'chess images\wrook.png')
brookimg=pygame.image.load(r'chess images\brook.png')
wqueenimg=pygame.image.load(r'chess images\wqueen.png')
bqueenimg=pygame.image.load(r'chess images\bqueen.png')
wkingimg=pygame.image.load(r'chess images\wking.png')
bkingimg=pygame.image.load(r'chess images\bking.png')

file1=open('help1.txt','r')
help1=file1.read()
white=(200,200,200)
brown=(165,137,70)
gold=(255,215,0)
red=(255,0,0)
blue=(51,171,249)
light_blue=(52,204,255)
pink=(248,24,148)
black=(0,0,0)
light_yellow=(240,230,140)
green=(0,170,0)
def chess_square(color,x,y,width):
    pygame.draw.rect(gamedisplay,color,(x,y,width,width))
def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()
def text_display(text,x,y,width,height):
    largeText = pygame.font.SysFont('comicsansms',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((x+width/2),(y+height/2))
    gamedisplay.blit(TextSurf, TextRect)
def text_display1(text,x,y,width,height):
    largeText = pygame.font.SysFont('comicsansms',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect = (x,y,width,height)
    gamedisplay.blit(TextSurf, TextRect)
game_start=0
mx=0
my=0
w=0
q=0
count=0
temp=0
while not off:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                if game_start == 0:
                    off =True
                else:
                    game_start=4
                    stop=1
            if game_start == 1:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mx,my=pygame.mouse.get_pos()
                    if mx >= 40 and mx <= 600 and my >= 40 and my <= 600:
                        if my >= 40 and my <= 110:
                            m = 0
                        elif my > 110 and my <= 180:
                            m = 1
                        elif my > 180 and my <= 250:
                            m = 2
                        elif my > 250 and my <= 320:
                            m = 3
                        elif my > 320 and my <= 390:
                            m = 4
                        elif my > 390 and my <= 460:
                            m = 5
                        elif my > 460 and my <= 530:
                            m = 6
                        elif my > 530 and my <= 600:
                            m = 7
                        if mx >= 40 and mx <= 110:
                            n = 0
                        elif mx > 110 and mx <= 180:
                            n = 1
                        elif mx > 180 and mx <= 250:
                            n = 2
                        elif mx > 250 and mx <= 320:
                            n = 3
                        elif mx > 320 and mx <= 390:
                            n = 4
                        elif mx > 390 and mx <= 460:
                            n = 5
                        elif mx > 460 and mx <= 530:
                            n = 6
                        elif mx > 530 and mx <= 600:
                            n = 7
                        print(m, n, count, board[m][n])
                        if count % 4 == 0 and stop==0:
                            w = m
                            q = n
                            for i in range(16):
                                wsurround[i]=0

                            if board[m][n] == 'p1':
                                temp = board[m][n]
                                pawn(m,n,wpos[0][2],0,wem_passent[0])
                                print('p1')
                                print(wpos[0][2])
                                if wsurround[0]==1:
                                    count+=1
                            elif board[m][n] == 'p2':
                                temp = board[m][n]
                                pawn(m,n,wpos[1][2],1,wem_passent[1])
                                if wsurround[1] == 1:
                                    count+=1
                            elif board[m][n] == 'p3':
                                temp = board[m][n]
                                pawn(m,n,wpos[2][2],2,wem_passent[2])
                                if wsurround[2] == 1:
                                    count+=1
                            elif board[m][n] == 'p4':
                                temp = board[m][n]
                                pawn(m,n,wpos[3][2],3,wem_passent[3])
                                if wsurround[3] == 1:
                                    count+=1
                            elif board[m][n] == 'p5':
                                temp = board[m][n]
                                pawn(m,n,wpos[4][2],4,wem_passent[4])
                                if wsurround[4] == 1:
                                    count+=1
                            elif board[m][n] == 'p6':
                                temp = board[m][n]
                                pawn(m,n,wpos[5][2],5,wem_passent[5])
                                if wsurround[5] == 1:
                                    count+=1
                            elif board[m][n] == 'p7':
                                temp = board[m][n]
                                pawn(m,n,wpos[6][2],6,wem_passent[6])
                                if wsurround[6] == 1:
                                    count+=1
                            elif board[m][n] == 'p8':
                                temp = board[m][n]
                                pawn(m,n,wpos[7][2],7,wem_passent[7])
                                if wsurround[7] == 1:
                                    count+=1
                            elif board[m][n] == 'b1':
                                temp = board[m][n]
                                bishop(m,n,wpos[12][2],12)
                                if wsurround[12] == 1:
                                    count+=1
                            elif board[m][n] == 'b2':
                                temp = board[m][n]
                                bishop(m,n,wpos[13][2],13)
                                if wsurround[13] == 1:
                                    count+=1
                            elif board[m][n] == 'r1':
                                temp = board[m][n]
                                rook(m, n,wpos[8][2],8)
                                if wsurround[8] == 1:
                                    count += 1
                            elif board[m][n] == 'r2':
                                temp = board[m][n]
                                rook(m, n,wpos[9][2],9)
                                if wsurround[9] == 1:
                                    count += 1
                            elif board[m][n] == 'n1':
                                temp = board[m][n]
                                knight(m, n,wpos[10][2],10)
                                if wsurround[10] == 1:
                                    count += 1
                            elif board[m][n] == 'n2':
                                temp = board[m][n]
                                knight(m, n,wpos[11][2],11)
                                if wsurround[11] == 1:
                                    count += 1
                            elif board[m][n] == 'q1':
                                temp = board[m][n]
                                queen(m, n,wpos[14][2],14)
                                if wsurround[14] == 1:
                                    count += 1
                            elif board[m][n] == 'k':
                                temp = board[m][n]
                                board[m][n]=' '
                                king(m, n, w_king_moved)
                                board[m][n] = 'k'
                                if wsurround[15] == 1:
                                    count += 1
                            elif board[m][n] == 'q2':
                                temp = board[m][n]
                                queen(m, n,wpos[16][2],16)
                                if wsurround[16] == 1:
                                    count += 1
                            elif board[m][n] == 'q3':
                                temp = board[m][n]
                                queen(m, n,wpos[17][2],17)
                                if wsurround[17] == 1:
                                    count += 1
                            elif board[m][n] == 'q4':
                                temp = board[m][n]
                                queen(m, n,wpos[18][2],18)
                                if wsurround[18] == 1:
                                    count += 1
                            elif board[m][n] == 'q5':
                                temp = board[m][n]
                                queen(m, n,wpos[19][2],19)
                                if wsurround[19] == 1:
                                    count += 1
                            elif board[m][n] == 'q6':
                                temp = board[m][n]
                                queen(m, n,wpos[20][2],20)
                                if wsurround[20] == 1:
                                    count += 1
                            elif board[m][n] == 'q7':
                                temp = board[m][n]
                                queen(m, n,wpos[21][2],21)
                                if wsurround[21] == 1:
                                    count += 1
                            elif board[m][n] == 'q8':
                                temp = board[m][n]
                                queen(m, n,wpos[22][2],22)
                                if wsurround[22] == 1:
                                    count += 1
                            elif board[m][n] == 'q9':
                                temp = board[m][n]
                                queen(m, n,wpos[23][2],23)
                                if wsurround[23] == 1:
                                    count += 1

                        elif count % 4 == 1 and stop==0:
                            if paths[m][n] == '*':
                                if temp[0] == 'p' and m == 0:
                                    k=find_num(temp)
                                    wpos[k][0]=wpos[k][1]=wpos[k][2]=-1
                                    temp = 'q'+str(w_queen_num)
                                    k=find_num(temp)
                                    wpos[k][2]=1
                                    print(temp)
                                    w_queen_num+=1
                                    print(w_queen_num)

                                if temp == 'k' and m == 7 and n == 2 and w == 7 and q == 4:
                                    board[7][3]='r1'
                                    board[7][0]=' '
                                    wpos[8][0]=7
                                    wpos[8][1]=3
                                if temp == 'k' and m == 7 and n == 6 and w == 7 and q == 4:
                                    board[7][5]='r2'
                                    board[7][7]=' '
                                    wpos[9][0]=7
                                    wpos[9][1]=5

                                if temp[0]=='p' and m == 4 and w == 6:
                                    if 0<n and board[m][n-1][0]=='P':
                                        k=find_num(board[m][n-1])
                                        bem_passent[k]=2
                                    if n<7 and board[m][n+1][0]=='P':
                                        k=find_num(board[m][n+1])
                                        bem_passent[k]=1

                                if temp[0]=='p' and board[m][n]==' ':
                                    if (m==w-1 and n==q-1) or (m==w-1 and n==q+1):
                                        k=find_num(board[m+1][n])
                                        bpos[k][0]=bpos[k][1]=bpos[k][2]=-1
                                        board[m+1][n]=' '

                                for i in bdefend_num:
                                    bdefend_pos[i].clear()
                                bdefend_num.clear()

                                wattack_piece.clear()

                                paths[wpos[15][0]][wpos[15][1]] = ' '

                                if board[m][n] == 'P1':
                                    bpos[0][0]=-1
                                    bpos[0][1]=-1
                                    bpos[0][2]=-1
                                elif board[m][n] == 'P2':
                                    bpos[1][0] = -1
                                    bpos[1][1] = -1
                                    bpos[1][2] = -1
                                elif board[m][n] == 'P3':
                                    bpos[2][0] = -1
                                    bpos[2][1] = -1
                                    bpos[2][2] = -1
                                elif board[m][n] == 'P4':
                                    bpos[3][0] = -1
                                    bpos[3][1] = -1
                                    bpos[3][2] = -1
                                elif board[m][n] == 'P5':
                                    bpos[4][0] = -1
                                    bpos[4][1] = -1
                                    bpos[4][2] = -1
                                elif board[m][n] == 'P6':
                                    bpos[5][0] = -1
                                    bpos[5][1] = -1
                                    bpos[5][2] = -1
                                elif board[m][n] == 'P7':
                                    bpos[6][0] = -1
                                    bpos[6][1] = -1
                                    bpos[6][2] = -1
                                elif board[m][n] == 'P8':
                                    bpos[7][0] = -1
                                    bpos[7][1] = -1
                                    bpos[7][2] = -1
                                elif board[m][n] == 'B1':
                                    bpos[12][0] = -1
                                    bpos[12][1] = -1
                                    bpos[12][2] = -1
                                elif board[m][n] == 'B2':
                                    bpos[13][0] = -1
                                    bpos[13][1] = -1
                                    bpos[13][2] = -1
                                elif board[m][n] == 'R1':
                                    bpos[8][0] = -1
                                    bpos[8][1] = -1
                                    bpos[8][2] = -1
                                elif board[m][n] == 'R2':
                                    bpos[9][0] = -1
                                    bpos[9][1] = -1
                                    bpos[9][2] = -1
                                elif board[m][n] == 'N1':
                                    bpos[10][0] = -1
                                    bpos[10][1] = -1
                                    bpos[10][2] = -1
                                elif board[m][n] == 'N2':
                                    bpos[11][0] = -1
                                    bpos[11][1] = -1
                                    bpos[11][2] = -1
                                elif board[m][n] == 'Q1':
                                    bpos[14][0] = -1
                                    bpos[14][1] = -1
                                    bpos[14][2] = -1
                                elif board[m][n] == 'Q2':
                                    bpos[16][0] = -1
                                    bpos[16][1] = -1
                                    bpos[16][2] = -1
                                elif board[m][n] == 'Q3':
                                    bpos[17][0] = -1
                                    bpos[17][1] = -1
                                    bpos[17][2] = -1
                                elif board[m][n] == 'Q4':
                                    bpos[18][0] = -1
                                    bpos[18][1] = -1
                                    bpos[18][2] = -1
                                elif board[m][n] == 'Q5':
                                    bpos[19][0] = -1
                                    bpos[19][1] = -1
                                    bpos[19][2] = -1
                                elif board[m][n] == 'Q6':
                                    bpos[20][0] = -1
                                    bpos[20][1] = -1
                                    bpos[20][2] = -1
                                elif board[m][n] == 'Q7':
                                    bpos[21][0] = -1
                                    bpos[21][1] = -1
                                    bpos[21][2] = -1
                                elif board[m][n] == 'Q8':
                                    bpos[22][0] = -1
                                    bpos[22][1] = -1
                                    bpos[22][2] = -1
                                elif board[m][n] == 'Q9':
                                    bpos[23][0] = -1
                                    bpos[23][1] = -1
                                    bpos[23][2] = -1
                                board[m][n] = temp
                                print(temp)
                                board[w][q] = ' '
                                if board[m][n] == 'p1':
                                    if wpos[0][2]!=-1:
                                        wpos[0][0] = m
                                        wpos[0][1] = n
                                        wem_passent[0] = 0
                                elif board[m][n] == 'p2':
                                    if wpos[1][2] != -1:
                                        wpos[1][0] = m
                                        wpos[1][1] = n
                                        wem_passent[1] = 0
                                elif board[m][n] == 'p3':
                                    if wpos[2][2] != -1:
                                        wpos[2][0] = m
                                        wpos[2][1] = n
                                        wem_passent[2] = 0
                                elif board[m][n] == 'p4':
                                    if wpos[3][2] != -1:
                                        wpos[3][0] = m
                                        wpos[3][1] = n
                                        wem_passent[3] = 0
                                elif board[m][n] == 'p5':
                                    if wpos[4][2] != -1:
                                        wpos[4][0] = m
                                        wpos[4][1] = n
                                        wem_passent[4] = 0
                                elif board[m][n] == 'p6':
                                    if wpos[5][2] != -1:
                                        wpos[5][0] = m
                                        wpos[5][1] = n
                                        wem_passent[5] = 0
                                elif board[m][n] == 'p7':
                                    if wpos[6][2] != -1:
                                        wpos[6][0] = m
                                        wpos[6][1] = n
                                        wem_passent[6] = 0
                                elif board[m][n] == 'p8':
                                    if wpos[7][2] != -1:
                                        wpos[7][0] = m
                                        wpos[7][1] = n
                                        wem_passent[7] = 0
                                elif board[m][n] == 'b1':
                                    wpos[12][0] = m
                                    wpos[12][1] = n
                                elif board[m][n] == 'b2':
                                    wpos[13][0] = m
                                    wpos[13][1] = n
                                elif board[m][n] == 'r1':
                                    wpos[8][0] = m
                                    wpos[8][1] = n
                                elif board[m][n] == 'r2':
                                    wpos[9][0] = m
                                    wpos[9][1] = n
                                elif board[m][n] == 'n1':
                                    wpos[10][0] = m
                                    wpos[10][1] = n
                                elif board[m][n] == 'n2':
                                    wpos[11][0] = m
                                    wpos[11][1] = n
                                elif board[m][n] == 'q1':
                                    wpos[14][0] = m
                                    wpos[14][1] = n
                                elif board[m][n] == 'k':
                                    wpos[15][0] = m
                                    wpos[15][1] = n
                                    w_king_moved = 1
                                elif board[m][n] == 'q2':
                                    wpos[16][0] = m
                                    wpos[16][1] = n
                                elif board[m][n] == 'q3':
                                    wpos[17][0] = m
                                    wpos[17][1] = n
                                elif board[m][n] == 'q4':
                                    wpos[18][0] = m
                                    wpos[18][1] = n
                                elif board[m][n] == 'q5':
                                    wpos[19][0] = m
                                    wpos[19][1] = n
                                elif board[m][n] == 'q6':
                                    wpos[20][0] = m
                                    wpos[20][1] = n
                                elif board[m][n] == 'q7':
                                    wpos[21][0] = m
                                    wpos[21][1] = n
                                elif board[m][n] == 'q8':
                                    wpos[22][0] = m
                                    wpos[22][1] = n
                                elif board[m][n] == 'q9':
                                    wpos[23][0] = m
                                    wpos[23][1] = n
                                print(wpos)
                                count+=1
                            else:
                                count-=1
                            if temp == 'p1':
                                pawnrestore(w,q,wpos[0][2],0)
                            elif temp == 'p2':
                                pawnrestore(w,q,wpos[1][2],1)
                            elif temp == 'p3':
                                pawnrestore(w,q,wpos[2][2],2)
                            elif temp == 'p4':
                                pawnrestore(w,q,wpos[3][2],3)
                            elif temp == 'p5':
                                pawnrestore(w,q,wpos[4][2],4)
                            elif temp == 'p6':
                                pawnrestore(w,q,wpos[5][2],5)
                            elif temp == 'p7':
                                pawnrestore(w,q,wpos[6][2],6)
                            elif temp == 'p8':
                                pawnrestore(w,q,wpos[7][2],7)
                            elif temp == 'b1':
                                bishoprestore(w,q,wpos[12][2],12)
                            elif temp == 'b2':
                                bishoprestore(w,q,wpos[13][2],13)
                            elif temp == 'r1':
                                rookrestore(w,q,wpos[8][2],8)
                            elif temp == 'r2':
                                rookrestore(w,q,wpos[9][2],9)
                            elif temp == 'n1':
                                knightrestore(w,q,wpos[10][2],10)
                            elif temp == 'n2':
                                knightrestore(w,q,wpos[11][2],11)
                            elif temp == 'q1':
                                queenrestore(w,q,wpos[14][2],14)
                            elif temp == 'k':
                                kingrestore(w,q)
                            elif temp == 'q2':
                                queenrestore(w,q,wpos[16][2],16)
                            elif temp == 'q3':
                                queenrestore(w,q,wpos[17][2],17)
                            elif temp == 'q4':
                                queenrestore(w,q,wpos[18][2],18)
                            elif temp == 'q5':
                                queenrestore(w,q,wpos[19][2],19)
                            elif temp == 'q6':
                                queenrestore(w,q,wpos[20][2],20)
                            elif temp == 'q7':
                                queenrestore(w,q,wpos[21][2],21)
                            elif temp == 'q8':
                                queenrestore(w,q,wpos[22][2],22)
                            elif temp == 'q9':
                                queenrestore(w,q,wpos[23][2],23)

                            for i in range (24):
                                if bpos[i][2]!=-1:
                                    bpos[i][2]=1

                            find_kingneighbour(wpos[15][0], wpos[15][1])

                            bsurround[15]=0
                            king_involved[0]=0
                            board[bpos[15][0]][bpos[15][1]] = ' '
                            KING(bpos[15][0], bpos[15][1],b_king_moved,1)
                            kingrestore(bpos[15][0], bpos[15][1])
                            board[bpos[15][0]][bpos[15][1]] = 'K'

                            if CHECK()==1:
                                print('CHECK!')
                                paths[bpos[15][0]][bpos[15][1]] = '$'
                                if pathcheck(checkpiece[0],checkpiece[1])==1 and bsurround[15]==0:
                                    for pos in wattack_piece:
                                        paths[pos[0]][pos[1]]='!'
                                    paths[checkpiece[0]][checkpiece[1]]='!'
                                    if king_involved[0] == 1:
                                        paths[wpos[15][0]][wpos[15][1]]='!'
                                    stop=1
                                    print('CHECKMATE!')

                                for i in range(24):
                                    if bpos[i][2] != -1 and bpos[i][2]!=9:
                                        bpos[i][2] = 0
                            elif bsurround[15]==0 and STALEMATE()==0:
                                for pos in wattack_piece:
                                    paths[pos[0]][pos[1]] = '!'
                                if king_involved[0] == 1:
                                    paths[wpos[15][0]][wpos[15][1]] = '!'
                                stop = 1
                                print('STALEMATE!')
                        elif count % 4 == 2 and stop==0:
                            w = m
                            q = n
                            for i in range(16):
                                bsurround[i]=0
                            if board[m][n] == 'P1':
                                temp = board[m][n]
                                PAWN(m,n,bpos[0][2],0,bem_passent[0],game_start)
                                if bsurround[0]==1:
                                    count+=1
                            elif board[m][n] == 'P2':
                                temp = board[m][n]
                                PAWN(m,n,bpos[1][2],1,bem_passent[1],game_start)
                                if bsurround[1] == 1:
                                    count+=1
                            elif board[m][n] == 'P3':
                                temp = board[m][n]
                                PAWN(m,n,bpos[2][2],2,bem_passent[2],game_start)
                                if bsurround[2] == 1:
                                    count+=1
                            elif board[m][n] == 'P4':
                                temp = board[m][n]
                                PAWN(m,n,bpos[3][2],3,bem_passent[3],game_start)
                                if bsurround[3] == 1:
                                    count+=1
                            elif board[m][n] == 'P5':
                                temp = board[m][n]
                                PAWN(m,n,bpos[4][2],4,bem_passent[4],game_start)
                                if bsurround[4] == 1:
                                    count+=1
                            elif board[m][n] == 'P6':
                                temp = board[m][n]
                                PAWN(m,n,bpos[5][2],5,bem_passent[5],game_start)
                                if bsurround[5] == 1:
                                    count+=1
                            elif board[m][n] == 'P7':
                                temp = board[m][n]
                                PAWN(m,n,bpos[6][2],6,bem_passent[6],game_start)
                                if bsurround[6] == 1:
                                    count+=1
                            elif board[m][n] == 'P8':
                                temp = board[m][n]
                                PAWN(m,n,bpos[7][2],7,bem_passent[7],game_start)
                                if bsurround[7] == 1:
                                    count+=1
                            elif board[m][n] == 'B1':
                                temp = board[m][n]
                                BISHOP(m,n,bpos[12][2],12,game_start)
                                if bsurround[12] == 1:
                                    count+=1
                            elif board[m][n] == 'B2':
                                temp = board[m][n]
                                BISHOP(m,n,bpos[13][2],13,game_start)
                                if bsurround[13] == 1:
                                    count+=1
                            elif board[m][n] == 'R1':
                                temp = board[m][n]
                                ROOK(m, n,bpos[8][2],8,game_start)
                                if bsurround[8] == 1:
                                    count += 1
                            elif board[m][n] == 'R2':
                                temp = board[m][n]
                                ROOK(m, n,bpos[9][2],9,game_start)
                                if bsurround[9] == 1:
                                    count += 1
                            elif board[m][n] == 'N1':
                                temp = board[m][n]
                                KNIGHT(m, n,bpos[10][2],10,game_start)
                                if bsurround[10] == 1:
                                    count += 1
                            elif board[m][n] == 'N2':
                                temp = board[m][n]
                                KNIGHT(m, n,bpos[11][2],11,game_start)
                                if bsurround[11] == 1:
                                    count += 1
                            elif board[m][n] == 'Q1':
                                temp = board[m][n]
                                QUEEN(m, n,bpos[14][2],14,game_start)
                                if bsurround[14] == 1:
                                    count += 1
                            elif board[m][n] == 'K':
                                temp = board[m][n]
                                board[m][n]=' '
                                KING(m, n, b_king_moved,game_start)
                                board[m][n]='K'
                                if bsurround[15] == 1:
                                    count += 1
                            elif board[m][n] == 'Q2':
                                temp = board[m][n]
                                QUEEN(m, n,bpos[16][2],16,game_start)
                                if bsurround[16] == 1:
                                    count += 1
                            elif board[m][n] == 'Q3':
                                temp = board[m][n]
                                QUEEN(m, n,bpos[17][2],17,game_start)
                                if bsurround[17] == 1:
                                    count += 1
                            elif board[m][n] == 'Q4':
                                temp = board[m][n]
                                QUEEN(m, n,bpos[18][2],18,game_start)
                                if bsurround[18] == 1:
                                    count += 1
                            elif board[m][n] == 'Q5':
                                temp = board[m][n]
                                QUEEN(m, n,bpos[19][2],19,game_start)
                                if bsurround[19] == 1:
                                    count += 1
                            elif board[m][n] == 'Q6':
                                temp = board[m][n]
                                QUEEN(m, n,bpos[20][2],20,game_start)
                                if bsurround[20] == 1:
                                    count += 1
                            elif board[m][n] == 'Q7':
                                temp = board[m][n]
                                QUEEN(m, n,bpos[21][2],21,game_start)
                                if bsurround[21] == 1:
                                    count += 1
                            elif board[m][n] == 'Q8':
                                temp = board[m][n]
                                QUEEN(m, n,bpos[22][2],22,game_start)
                                if bsurround[22] == 1:
                                    count += 1
                            elif board[m][n] == 'Q9':
                                temp = board[m][n]
                                QUEEN(m, n,bpos[23][2],23,game_start)
                                if bsurround[23] == 1:
                                    count += 1

                        elif count % 4 == 3 and stop==0:
                            if paths[m][n] == '*' :
                                if temp[0] == 'P' and m == 7:
                                    k=find_num(temp)
                                    bpos[k][0]=bpos[k][1]=bpos[k][2]=-1
                                    temp = 'Q'+str(b_queen_num)
                                    print(temp)
                                    k = find_num(temp)
                                    bpos[k][2] = 1
                                    b_queen_num+=1
                                    print(b_queen_num)
                                if temp == 'K' and m == 0 and n == 2 and w == 0 and q == 4:
                                    board[0][3]='R1'
                                    board[0][0]=' '
                                    bpos[8][0]=0
                                    bpos[8][1]=3
                                if temp == 'K' and m == 0 and n == 6 and w == 0 and q == 4:
                                    board[0][5]='R2'
                                    board[0][7]=' '
                                    bpos[9][0]=0
                                    bpos[9][1]=5

                                if temp[0]=='P' and m == 3 and w == 1:
                                    if 0<n and board[m][n-1][0]=='p':
                                        k=find_num(board[m][n-1])
                                        wem_passent[k]=2
                                    if n<7 and board[m][n+1][0]=='p':
                                        k=find_num(board[m][n+1])
                                        wem_passent[k]=1

                                if temp[0]=='P' and board[m][n]==' ':
                                    if (m==w+1 and n==q-1) or (m==w+1 and n==q+1):
                                        k=find_num(board[m-1][n])
                                        wpos[k][0]=wpos[k][1]=wpos[k][2]=-1
                                        board[m-1][n]=' '

                                for i in wdefend_num:
                                    wdefend_pos[i].clear()
                                wdefend_num.clear()

                                paths[bpos[15][0]][bpos[15][1]]=' '

                                battack_piece.clear()
                                if board[m][n] == 'p1':
                                    wpos[0][0] = -1
                                    wpos[0][1] = -1
                                    wpos[0][2] = -1
                                elif board[m][n] == 'p2':
                                    wpos[1][0] = -1
                                    wpos[1][1] = -1
                                    wpos[1][2] = -1
                                elif board[m][n] == 'p3':
                                    wpos[2][0] = -1
                                    wpos[2][1] = -1
                                    wpos[2][2] = -1
                                elif board[m][n] == 'p4':
                                    wpos[3][0] = -1
                                    wpos[3][1] = -1
                                    wpos[3][2] = -1
                                elif board[m][n] == 'p5':
                                    wpos[4][0] = -1
                                    wpos[4][1] = -1
                                    wpos[4][2] = -1
                                elif board[m][n] == 'p6':
                                    wpos[5][0] = -1
                                    wpos[5][1] = -1
                                    wpos[5][2] = -1
                                elif board[m][n] == 'p7':
                                    wpos[6][0] = -1
                                    wpos[6][1] = -1
                                    wpos[6][2] = -1
                                elif board[m][n] == 'p8':
                                    wpos[7][0] = -1
                                    wpos[7][1] = -1
                                    wpos[7][2] = -1
                                elif board[m][n] == 'b1':
                                    wpos[12][0] = -1
                                    wpos[12][1] = -1
                                    wpos[12][2] = -1
                                elif board[m][n] == 'b2':
                                    wpos[13][0] = -1
                                    wpos[13][1] = -1
                                    wpos[13][2] = -1
                                elif board[m][n] == 'r1':
                                    wpos[8][0] = -1
                                    wpos[8][1] = -1
                                    wpos[8][2] = -1
                                elif board[m][n] == 'r2':
                                    wpos[9][0] = -1
                                    wpos[9][1] = -1
                                    wpos[9][2] = -1
                                elif board[m][n] == 'n1':
                                    wpos[10][0] = -1
                                    wpos[10][1] = -1
                                    wpos[10][2] = -1
                                elif board[m][n] == 'n2':
                                    wpos[11][0] = -1
                                    wpos[11][1] = -1
                                    wpos[11][2] = -1
                                elif board[m][n] == 'q1':
                                    wpos[14][0] = -1
                                    wpos[14][1] = -1
                                    wpos[14][2] = -1
                                elif board[m][n] == 'q2':
                                    wpos[16][0] = -1
                                    wpos[16][1] = -1
                                    wpos[16][2] = -1
                                elif board[m][n] == 'q3':
                                    wpos[17][0] = -1
                                    wpos[17][1] = -1
                                    wpos[17][2] = -1
                                elif board[m][n] == 'q4':
                                    wpos[18][0] = -1
                                    wpos[18][1] = -1
                                    wpos[18][2] = -1
                                elif board[m][n] == 'q5':
                                    wpos[19][0] = -1
                                    wpos[19][1] = -1
                                    wpos[19][2] = -1
                                elif board[m][n] == 'q6':
                                    wpos[20][0] = -1
                                    wpos[20][1] = -1
                                    wpos[20][2] = -1
                                elif board[m][n] == 'q7':
                                    wpos[21][0] = -1
                                    wpos[21][1] = -1
                                    wpos[21][2] = -1
                                elif board[m][n] == 'q8':
                                    wpos[22][0] = -1
                                    wpos[22][1] = -1
                                    wpos[22][2] = -1
                                elif board[m][n] == 'q9':
                                    wpos[23][0] = -1
                                    wpos[23][1] = -1
                                    wpos[23][2] = -1
                                board[m][n] = temp
                                board[w][q] = ' '
                                if board[m][n] == 'P1':
                                    if bpos[0][2]!=-1:
                                        bpos[0][0] = m
                                        bpos[0][1] = n
                                        bem_passent[0]=0
                                elif board[m][n] == 'P2':
                                    if bpos[1][2] != -1:
                                        bpos[1][0] = m
                                        bpos[1][1] = n
                                        bem_passent[1] = 0
                                elif board[m][n] == 'P3':
                                    if bpos[2][2] != -1:
                                        bpos[2][0] = m
                                        bpos[2][1] = n
                                        bem_passent[2] = 0
                                elif board[m][n] == 'P4':
                                    if bpos[3][2] != -1:
                                        bpos[3][0] = m
                                        bpos[3][1] = n
                                        bem_passent[3] = 0
                                elif board[m][n] == 'P5':
                                    if bpos[4][2] != -1:
                                        bpos[4][0] = m
                                        bpos[4][1] = n
                                        bem_passent[4] = 0
                                elif board[m][n] == 'P6':
                                    if bpos[5][2] != -1:
                                        bpos[5][0] = m
                                        bpos[5][1] = n
                                        bem_passent[5] = 0
                                elif board[m][n] == 'P7':
                                    if bpos[6][2] != -1:
                                        bpos[6][0] = m
                                        bpos[6][1] = n
                                        bem_passent[6] = 0
                                elif board[m][n] == 'P8':
                                    if bpos[7][2] != -1:
                                        bpos[7][0] = m
                                        bpos[7][1] = n
                                        bem_passent[7] = 0
                                elif board[m][n] == 'B1':
                                    bpos[12][0] = m
                                    bpos[12][1] = n
                                elif board[m][n] == 'B2':
                                    bpos[13][0] = m
                                    bpos[13][1] = n
                                elif board[m][n] == 'R1':
                                    bpos[8][0] = m
                                    bpos[8][1] = n
                                elif board[m][n] == 'R2':
                                    bpos[9][0] = m
                                    bpos[9][1] = n
                                elif board[m][n] == 'N1':
                                    bpos[10][0] = m
                                    bpos[10][1] = n
                                elif board[m][n] == 'N2':
                                    bpos[11][0] = m
                                    bpos[11][1] = n
                                elif board[m][n] == 'Q1':
                                    bpos[14][0] = m
                                    bpos[14][1] = n
                                elif board[m][n] == 'K':
                                    bpos[15][0] = m
                                    bpos[15][1] = n
                                    b_king_moved = 1
                                elif board[m][n] == 'Q2':
                                    bpos[16][0] = m
                                    bpos[16][1] = n
                                elif board[m][n] == 'Q3':
                                    bpos[17][0] = m
                                    bpos[17][1] = n
                                elif board[m][n] == 'Q4':
                                    bpos[18][0] = m
                                    bpos[18][1] = n
                                elif board[m][n] == 'Q5':
                                    bpos[19][0] = m
                                    bpos[19][1] = n
                                elif board[m][n] == 'Q6':
                                    bpos[20][0] = m
                                    bpos[20][1] = n
                                elif board[m][n] == 'Q7':
                                    bpos[21][0] = m
                                    bpos[21][1] = n
                                elif board[m][n] == 'Q8':
                                    bpos[22][0] = m
                                    bpos[22][1] = n

                                print(bpos)
                                count+=1
                            else:
                                count-=1
                            if temp == 'P1':
                                PAWNRESTORE(w,q,bpos[0][2],16)
                            elif temp == 'P2':
                                PAWNRESTORE(w,q,bpos[1][2],17)
                            elif temp == 'P3':
                                PAWNRESTORE(w,q,bpos[2][2],18)
                            elif temp == 'P4':
                                PAWNRESTORE(w,q,bpos[3][2],19)
                            elif temp == 'P5':
                                PAWNRESTORE(w,q,bpos[4][2],20)
                            elif temp == 'P6':
                                PAWNRESTORE(w,q,bpos[5][2],21)
                            elif temp == 'P7':
                                PAWNRESTORE(w,q,bpos[6][2],22)
                            elif temp == 'P8':
                                PAWNRESTORE(w,q,bpos[7][2],23)
                            elif temp == 'B1':
                                bishoprestore(w,q,bpos[12][2],28)
                            elif temp == 'B2':
                                bishoprestore(w,q,bpos[13][2],29)
                            elif temp == 'R1':
                                rookrestore(w,q,bpos[8][2],24)
                            elif temp == 'R2':
                                rookrestore(w,q,bpos[9][2],25)
                            elif temp == 'N1':
                                knightrestore(w,q,bpos[10][2],26)
                            elif temp == 'N2':
                                knightrestore(w,q,bpos[11][2],27)
                            elif temp == 'Q1':
                                queenrestore(w,q,bpos[14][2],30)
                            elif temp == 'K':
                                kingrestore(w,q)
                            elif temp == 'Q2':
                                queenrestore(w,q,bpos[16][2],32)
                            elif temp == 'Q3':
                                queenrestore(w,q,bpos[17][2],33)
                            elif temp == 'Q4':
                                queenrestore(w,q,bpos[18][2],34)
                            elif temp == 'Q5':
                                queenrestore(w,q,bpos[19][2],35)
                            elif temp == 'Q6':
                                queenrestore(w,q,bpos[20][2],36)
                            elif temp == 'Q7':
                                queenrestore(w,q,bpos[21][2],37)
                            elif temp == 'Q8':
                                queenrestore(w,q,bpos[22][2],38)
                            elif temp == 'Q9':
                                queenrestore(w,q,bpos[23][2],39)

                            for i in range (24):
                                if wpos[i][2]!=-1 :
                                    wpos[i][2]=1

                            FIND_KINGNEIGHBOUR(bpos[15][0],bpos[15][1])

                            wsurround[15]=0
                            king_involved[0]=0
                            board[wpos[15][0]][wpos[15][1]] = ' '
                            king(wpos[15][0], wpos[15][1], w_king_moved)
                            kingrestore(wpos[15][0], wpos[15][1])
                            board[wpos[15][0]][wpos[15][1]] = 'k'

                            if check()==1:
                                print('check!')
                                paths[wpos[15][0]][wpos[15][1]] = '$'
                                if PATHCHECK(CHECKPIECE[0],CHECKPIECE[1])==1 and wsurround[15]==0:
                                    print('checkmate!')
                                    for pos in battack_piece:
                                        paths[pos[0]][pos[1]]='!'
                                    paths[CHECKPIECE[0]][CHECKPIECE[1]]='!'
                                    if king_involved[0] == 1:
                                        paths[bpos[15][0]][bpos[15][1]]='!'
                                    stop=1
                                for i in range(24):
                                    if wpos[i][2] != -1 and wpos[i][2]!=9:
                                        wpos[i][2] = 0
                            elif wsurround[15]==0 and stalemate()==0:
                                for pos in battack_piece:
                                    paths[pos[0]][pos[1]] = '!'
                                if king_involved[0] == 1:
                                    paths[bpos[15][0]][bpos[15][1]] = '!'
                                stop = 1
                                print('stalemate!')


            elif game_start == 2:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mx >= 40 and mx <= 600 and my >= 40 and my <= 600:
                        if my >= 40 and my <= 110:
                            m = 0
                        elif my > 110 and my <= 180:
                            m = 1
                        elif my > 180 and my <= 250:
                            m = 2
                        elif my > 250 and my <= 320:
                            m = 3
                        elif my > 320 and my <= 390:
                            m = 4
                        elif my > 390 and my <= 460:
                            m = 5
                        elif my > 460 and my <= 530:
                            m = 6
                        elif my > 530 and my <= 600:
                            m = 7
                        if mx >= 40 and mx <= 110:
                            n = 0
                        elif mx > 110 and mx <= 180:
                            n = 1
                        elif mx > 180 and mx <= 250:
                            n = 2
                        elif mx > 250 and mx <= 320:
                            n = 3
                        elif mx > 320 and mx <= 390:
                            n = 4
                        elif mx > 390 and mx <= 460:
                            n = 5
                        elif mx > 460 and mx <= 530:
                            n = 6
                        elif mx > 530 and mx <= 600:
                            n = 7
                        print(m, n, count, board[m][n])
                        if count % 3 == 0 and stop==0:
                            w = m
                            q = n
                            for i in range(16):
                                wsurround[i]=0

                            if board[m][n] == 'p1':
                                temp = board[m][n]
                                pawn(m,n,wpos[0][2],0,wem_passent[0])
                                if wsurround[0]==1:
                                    count+=1
                            elif board[m][n] == 'p2':
                                temp = board[m][n]
                                pawn(m,n,wpos[1][2],1,wem_passent[1])
                                if wsurround[1] == 1:
                                    count+=1
                            elif board[m][n] == 'p3':
                                temp = board[m][n]
                                pawn(m,n,wpos[2][2],2,wem_passent[2])
                                if wsurround[2] == 1:
                                    count+=1
                            elif board[m][n] == 'p4':
                                temp = board[m][n]
                                pawn(m,n,wpos[3][2],3,wem_passent[3])
                                if wsurround[3] == 1:
                                    count+=1
                            elif board[m][n] == 'p5':
                                temp = board[m][n]
                                pawn(m,n,wpos[4][2],4,wem_passent[4])
                                if wsurround[4] == 1:
                                    count+=1
                            elif board[m][n] == 'p6':
                                temp = board[m][n]
                                pawn(m,n,wpos[5][2],5,wem_passent[5])
                                if wsurround[5] == 1:
                                    count+=1
                            elif board[m][n] == 'p7':
                                temp = board[m][n]
                                pawn(m,n,wpos[6][2],6,wem_passent[6])
                                if wsurround[6] == 1:
                                    count+=1
                            elif board[m][n] == 'p8':
                                temp = board[m][n]
                                pawn(m,n,wpos[7][2],7,wem_passent[7])
                                if wsurround[7] == 1:
                                    count+=1
                            elif board[m][n] == 'b1':
                                temp = board[m][n]
                                bishop(m,n,wpos[12][2],12)
                                if wsurround[12] == 1:
                                    count+=1
                            elif board[m][n] == 'b2':
                                temp = board[m][n]
                                bishop(m,n,wpos[13][2],13)
                                if wsurround[13] == 1:
                                    count+=1
                            elif board[m][n] == 'r1':
                                temp = board[m][n]
                                rook(m, n,wpos[8][2],8)
                                if wsurround[8] == 1:
                                    count += 1
                            elif board[m][n] == 'r2':
                                temp = board[m][n]
                                rook(m, n,wpos[9][2],9)
                                if wsurround[9] == 1:
                                    count += 1
                            elif board[m][n] == 'n1':
                                temp = board[m][n]
                                knight(m, n,wpos[10][2],10)
                                if wsurround[10] == 1:
                                    count += 1
                            elif board[m][n] == 'n2':
                                temp = board[m][n]
                                knight(m, n,wpos[11][2],11)
                                if wsurround[11] == 1:
                                    count += 1
                            elif board[m][n] == 'q1':
                                temp = board[m][n]
                                queen(m, n,wpos[14][2],14)
                                if wsurround[14] == 1:
                                    count += 1
                            elif board[m][n] == 'k':
                                temp = board[m][n]
                                board[m][n]=' '
                                king(m, n, w_king_moved)
                                board[m][n] = 'k'
                                if wsurround[15] == 1:
                                    count += 1
                            elif board[m][n] == 'q2':
                                temp = board[m][n]
                                queen(m, n,wpos[16][2],16)
                                if wsurround[16] == 1:
                                    count += 1
                            elif board[m][n] == 'q3':
                                temp = board[m][n]
                                queen(m, n,wpos[17][2],17)
                                if wsurround[17] == 1:
                                    count += 1
                            elif board[m][n] == 'q4':
                                temp = board[m][n]
                                queen(m, n,wpos[18][2],18)
                                if wsurround[18] == 1:
                                    count += 1
                            elif board[m][n] == 'q5':
                                temp = board[m][n]
                                queen(m, n,wpos[19][2],19)
                                if wsurround[19] == 1:
                                    count += 1
                            elif board[m][n] == 'q6':
                                temp = board[m][n]
                                queen(m, n,wpos[20][2],20)
                                if wsurround[20] == 1:
                                    count += 1
                            elif board[m][n] == 'q7':
                                temp = board[m][n]
                                queen(m, n,wpos[21][2],21)
                                if wsurround[21] == 1:
                                    count += 1
                            elif board[m][n] == 'q8':
                                temp = board[m][n]
                                queen(m, n,wpos[22][2],22)
                                if wsurround[22] == 1:
                                    count += 1
                            elif board[m][n] == 'q9':
                                temp = board[m][n]
                                queen(m, n,wpos[23][2],23)
                                if wsurround[23] == 1:
                                    count += 1

                        elif count % 3 == 1 and stop==0:
                            if paths[m][n] == '*' :
                                if temp[0] == 'p' and m == 0:
                                    k=find_num(temp)
                                    wpos[k][0]=wpos[k][1]=wpos[k][2]=-1
                                    temp = 'q'+str(w_queen_num)
                                    k=find_num(temp)
                                    wpos[k][2]=1
                                    print(temp)
                                    w_queen_num+=1
                                    print(w_queen_num)

                                if temp == 'k' and m == 7 and n == 2 and w == 7 and q == 4:
                                    board[7][3]='r1'
                                    board[7][0]=' '
                                    wpos[8][0]=7
                                    wpos[8][1]=3
                                if temp == 'k' and m == 7 and n == 6 and w == 7 and q == 4:
                                    board[7][5]='r2'
                                    board[7][7]=' '
                                    wpos[9][0]=7
                                    wpos[9][1]=5

                                if temp[0]=='p' and m == 4 and w == 6:
                                    if 0<n and board[m][n-1][0]=='P':
                                        k=find_num(board[m][n-1])
                                        bem_passent[k]=2
                                    if n<7 and board[m][n+1][0]=='P':
                                        k=find_num(board[m][n+1])
                                        bem_passent[k]=1

                                if temp[0]=='p' and board[m][n]==' ':
                                    if (m==w-1 and n==q-1) or (m==w-1 and n==q+1):
                                        k=find_num(board[m+1][n])
                                        bpos[k][0]=bpos[k][1]=bpos[k][2]=-1
                                        board[m+1][n]=' '

                                for i in bdefend_num:
                                    bdefend_pos[i].clear()
                                bdefend_num.clear()

                                wattack_piece.clear()

                                paths[wpos[15][0]][wpos[15][1]] = ' '

                                if board[m][n] == 'P1':
                                    bpos[0][0]=-1
                                    bpos[0][1]=-1
                                    bpos[0][2]=-1
                                elif board[m][n] == 'P2':
                                    bpos[1][0] = -1
                                    bpos[1][1] = -1
                                    bpos[1][2] = -1
                                elif board[m][n] == 'P3':
                                    bpos[2][0] = -1
                                    bpos[2][1] = -1
                                    bpos[2][2] = -1
                                elif board[m][n] == 'P4':
                                    bpos[3][0] = -1
                                    bpos[3][1] = -1
                                    bpos[3][2] = -1
                                elif board[m][n] == 'P5':
                                    bpos[4][0] = -1
                                    bpos[4][1] = -1
                                    bpos[4][2] = -1
                                elif board[m][n] == 'P6':
                                    bpos[5][0] = -1
                                    bpos[5][1] = -1
                                    bpos[5][2] = -1
                                elif board[m][n] == 'P7':
                                    bpos[6][0] = -1
                                    bpos[6][1] = -1
                                    bpos[6][2] = -1
                                elif board[m][n] == 'P8':
                                    bpos[7][0] = -1
                                    bpos[7][1] = -1
                                    bpos[7][2] = -1
                                elif board[m][n] == 'B1':
                                    bpos[12][0] = -1
                                    bpos[12][1] = -1
                                    bpos[12][2] = -1
                                elif board[m][n] == 'B2':
                                    bpos[13][0] = -1
                                    bpos[13][1] = -1
                                    bpos[13][2] = -1
                                elif board[m][n] == 'R1':
                                    bpos[8][0] = -1
                                    bpos[8][1] = -1
                                    bpos[8][2] = -1
                                elif board[m][n] == 'R2':
                                    bpos[9][0] = -1
                                    bpos[9][1] = -1
                                    bpos[9][2] = -1
                                elif board[m][n] == 'N1':
                                    bpos[10][0] = -1
                                    bpos[10][1] = -1
                                    bpos[10][2] = -1
                                elif board[m][n] == 'N2':
                                    bpos[11][0] = -1
                                    bpos[11][1] = -1
                                    bpos[11][2] = -1
                                elif board[m][n] == 'Q1':
                                    bpos[14][0] = -1
                                    bpos[14][1] = -1
                                    bpos[14][2] = -1
                                elif board[m][n] == 'Q2':
                                    bpos[16][0] = -1
                                    bpos[16][1] = -1
                                    bpos[16][2] = -1
                                elif board[m][n] == 'Q3':
                                    bpos[17][0] = -1
                                    bpos[17][1] = -1
                                    bpos[17][2] = -1
                                elif board[m][n] == 'Q4':
                                    bpos[18][0] = -1
                                    bpos[18][1] = -1
                                    bpos[18][2] = -1
                                elif board[m][n] == 'Q5':
                                    bpos[19][0] = -1
                                    bpos[19][1] = -1
                                    bpos[19][2] = -1
                                elif board[m][n] == 'Q6':
                                    bpos[20][0] = -1
                                    bpos[20][1] = -1
                                    bpos[20][2] = -1
                                elif board[m][n] == 'Q7':
                                    bpos[21][0] = -1
                                    bpos[21][1] = -1
                                    bpos[21][2] = -1
                                elif board[m][n] == 'Q8':
                                    bpos[22][0] = -1
                                    bpos[22][1] = -1
                                    bpos[22][2] = -1
                                elif board[m][n] == 'Q9':
                                    bpos[23][0] = -1
                                    bpos[23][1] = -1
                                    bpos[23][2] = -1
                                board[m][n] = temp
                                print(temp)
                                board[w][q] = ' '
                                if board[m][n] == 'p1':
                                    if wpos[0][2]!=-1:
                                        wpos[0][0] = m
                                        wpos[0][1] = n
                                        wem_passent[0] = 0
                                elif board[m][n] == 'p2':
                                    if wpos[1][2] != -1:
                                        wpos[1][0] = m
                                        wpos[1][1] = n
                                        wem_passent[1] = 0
                                elif board[m][n] == 'p3':
                                    if wpos[2][2] != -1:
                                        wpos[2][0] = m
                                        wpos[2][1] = n
                                        wem_passent[2] = 0
                                elif board[m][n] == 'p4':
                                    if wpos[3][2] != -1:
                                        wpos[3][0] = m
                                        wpos[3][1] = n
                                        wem_passent[3] = 0
                                elif board[m][n] == 'p5':
                                    if wpos[4][2] != -1:
                                        wpos[4][0] = m
                                        wpos[4][1] = n
                                        wem_passent[4] = 0
                                elif board[m][n] == 'p6':
                                    if wpos[5][2] != -1:
                                        wpos[5][0] = m
                                        wpos[5][1] = n
                                        wem_passent[5] = 0
                                elif board[m][n] == 'p7':
                                    if wpos[6][2] != -1:
                                        wpos[6][0] = m
                                        wpos[6][1] = n
                                        wem_passent[6] = 0
                                elif board[m][n] == 'p8':
                                    if wpos[7][2] != -1:
                                        wpos[7][0] = m
                                        wpos[7][1] = n
                                        wem_passent[7] = 0
                                elif board[m][n] == 'b1':
                                    wpos[12][0] = m
                                    wpos[12][1] = n
                                elif board[m][n] == 'b2':
                                    wpos[13][0] = m
                                    wpos[13][1] = n
                                elif board[m][n] == 'r1':
                                    wpos[8][0] = m
                                    wpos[8][1] = n
                                elif board[m][n] == 'r2':
                                    wpos[9][0] = m
                                    wpos[9][1] = n
                                elif board[m][n] == 'n1':
                                    wpos[10][0] = m
                                    wpos[10][1] = n
                                elif board[m][n] == 'n2':
                                    wpos[11][0] = m
                                    wpos[11][1] = n
                                elif board[m][n] == 'q1':
                                    wpos[14][0] = m
                                    wpos[14][1] = n
                                elif board[m][n] == 'k':
                                    wpos[15][0] = m
                                    wpos[15][1] = n
                                    w_king_moved = 1
                                elif board[m][n] == 'q2':
                                    wpos[16][0] = m
                                    wpos[16][1] = n
                                elif board[m][n] == 'q3':
                                    wpos[17][0] = m
                                    wpos[17][1] = n
                                elif board[m][n] == 'q4':
                                    wpos[18][0] = m
                                    wpos[18][1] = n
                                elif board[m][n] == 'q5':
                                    wpos[19][0] = m
                                    wpos[19][1] = n
                                elif board[m][n] == 'q6':
                                    wpos[20][0] = m
                                    wpos[20][1] = n
                                elif board[m][n] == 'q7':
                                    wpos[21][0] = m
                                    wpos[21][1] = n
                                elif board[m][n] == 'q8':
                                    wpos[22][0] = m
                                    wpos[22][1] = n
                                elif board[m][n] == 'q9':
                                    wpos[23][0] = m
                                    wpos[23][1] = n
                                print(wpos)
                                count+=1
                            else:
                                count-=1
                            if temp == 'p1':
                                pawnrestore(w,q,wpos[0][2],0)
                            elif temp == 'p2':
                                pawnrestore(w,q,wpos[1][2],1)
                            elif temp == 'p3':
                                pawnrestore(w,q,wpos[2][2],2)
                            elif temp == 'p4':
                                pawnrestore(w,q,wpos[3][2],3)
                            elif temp == 'p5':
                                pawnrestore(w,q,wpos[4][2],4)
                            elif temp == 'p6':
                                pawnrestore(w,q,wpos[5][2],5)
                            elif temp == 'p7':
                                pawnrestore(w,q,wpos[6][2],6)
                            elif temp == 'p8':
                                pawnrestore(w,q,wpos[7][2],7)
                            elif temp == 'b1':
                                bishoprestore(w,q,wpos[12][2],12)
                            elif temp == 'b2':
                                bishoprestore(w,q,wpos[13][2],13)
                            elif temp == 'r1':
                                rookrestore(w,q,wpos[8][2],8)
                            elif temp == 'r2':
                                rookrestore(w,q,wpos[9][2],9)
                            elif temp == 'n1':
                                knightrestore(w,q,wpos[10][2],10)
                            elif temp == 'n2':
                                knightrestore(w,q,wpos[11][2],11)
                            elif temp == 'q1':
                                queenrestore(w,q,wpos[14][2],14)
                            elif temp == 'k':
                                kingrestore(w,q)
                            elif temp == 'q2':
                                queenrestore(w,q,wpos[16][2],16)
                            elif temp == 'q3':
                                queenrestore(w,q,wpos[17][2],17)
                            elif temp == 'q4':
                                queenrestore(w,q,wpos[18][2],18)
                            elif temp == 'q5':
                                queenrestore(w,q,wpos[19][2],19)
                            elif temp == 'q6':
                                queenrestore(w,q,wpos[20][2],20)
                            elif temp == 'q7':
                                queenrestore(w,q,wpos[21][2],21)
                            elif temp == 'q8':
                                queenrestore(w,q,wpos[22][2],22)
                            elif temp == 'q9':
                                queenrestore(w,q,wpos[23][2],23)

                            for i in range (24):
                                if bpos[i][2]!=-1:
                                    bpos[i][2]=1

                            find_kingneighbour(wpos[15][0], wpos[15][1])

                            bsurround[15]=0
                            king_involved[0]=0
                            board[bpos[15][0]][bpos[15][1]] = ' '
                            KING(bpos[15][0], bpos[15][1],b_king_moved,1)
                            kingrestore(bpos[15][0], bpos[15][1])
                            board[bpos[15][0]][bpos[15][1]] = 'K'

                            if CHECK()==1:
                                print('CHECK!')
                                paths[bpos[15][0]][bpos[15][1]] = '$'
                                if pathcheck(checkpiece[0],checkpiece[1])==1 and bsurround[15]==0:
                                    for pos in wattack_piece:
                                        paths[pos[0]][pos[1]]='!'
                                    paths[checkpiece[0]][checkpiece[1]]='!'
                                    if king_involved[0] == 1:
                                        paths[wpos[15][0]][wpos[15][1]]='!'
                                    stop=1
                                    print('CHECKMATE!')

                                for i in range(24):
                                    if bpos[i][2] != -1 and bpos[i][2]!=9:
                                        bpos[i][2] = 0
                            elif bsurround[15]==0 and STALEMATE()==0:
                                for pos in wattack_piece:
                                    paths[pos[0]][pos[1]] = '!'
                                if king_involved[0] == 1:
                                    paths[wpos[15][0]][wpos[15][1]] = '!'
                                stop = 1
                                print('STALEMATE!')
                            disp_pass=1
                if count%3==2 and stop == 0 and disp_pass==0:
                        sleep(0.5)
                        for j in range(24):
                            if bpos[j][2]!=-1:
                                alive.append(bpos[j])
                        print("A",alive)
                        for i in range(24):
                            bsurround[i] = 0
                        while True:
                            ran_num = randint(0, len(alive) - 1)
                            w = alive[ran_num][0]
                            q = alive[ran_num][1]
                            if board[w][q] == 'P1':
                                temp = board[w][q]
                                PAWN(w, q, bpos[0][2], 0, bem_passent[0], game_start)
                                if bsurround[0] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[0][2]])
                            elif board[w][q] == 'P2':
                                temp = board[w][q]
                                PAWN(w, q, bpos[1][2], 1, bem_passent[1], game_start)
                                if bsurround[1] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[1][2]])
                            elif board[w][q] == 'P3':
                                temp = board[w][q]
                                PAWN(w, q, bpos[2][2], 2, bem_passent[2], game_start)
                                if bsurround[2] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[2][2]])
                            elif board[w][q] == 'P4':
                                temp = board[w][q]
                                PAWN(w, q, bpos[3][2], 3, bem_passent[3], game_start)
                                if bsurround[3] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[3][2]])
                            elif board[w][q] == 'P5':
                                temp = board[w][q]
                                PAWN(w, q, bpos[4][2], 4, bem_passent[4], game_start)
                                if bsurround[4] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[4][2]])
                            elif board[w][q] == 'P6':
                                temp = board[w][q]
                                PAWN(w, q, bpos[5][2], 5, bem_passent[5], game_start)
                                if bsurround[5] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[5][2]])
                            elif board[w][q] == 'P7':
                                temp = board[w][q]
                                PAWN(w, q, bpos[6][2], 6, bem_passent[6], game_start)
                                if bsurround[6] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[6][2]])
                            elif board[w][q] == 'P8':
                                temp = board[w][q]
                                PAWN(w, q, bpos[7][2], 7, bem_passent[7], game_start)
                                if bsurround[7] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[7][2]])
                            elif board[w][q] == 'B1':
                                temp = board[w][q]
                                BISHOP(w, q, bpos[12][2], 12, game_start)
                                if bsurround[12] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[12][2]])
                            elif board[w][q] == 'B2':
                                temp = board[w][q]
                                BISHOP(w, q, bpos[13][2], 13, game_start)
                                if bsurround[13] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[13][2]])
                            elif board[w][q] == 'R1':
                                temp = board[w][q]
                                ROOK(w, q, bpos[8][2], 8, game_start)
                                if bsurround[8] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[8][2]])
                            elif board[w][q] == 'R2':
                                temp = board[w][q]
                                ROOK(w, q, bpos[9][2], 9, game_start)
                                if bsurround[9] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[9][2]])
                            elif board[w][q] == 'N1':
                                temp = board[w][q]
                                KNIGHT(w, q, bpos[10][2], 10, game_start)
                                if bsurround[10] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[10][2]])
                            elif board[w][q] == 'N2':
                                temp = board[w][q]
                                KNIGHT(w, q, bpos[11][2], 11, game_start)
                                if bsurround[11] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[11][2]])
                            elif board[w][q] == 'Q1':
                                temp = board[w][q]
                                QUEEN(w, q, bpos[14][2], 14, game_start)
                                if bsurround[14] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[14][2]])
                            elif board[w][q] == 'K':
                                temp = board[w][q]
                                board[w][q] = ' '
                                KING(w, q, b_king_moved, game_start)
                                board[w][q] = 'K'
                                if bsurround[15] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[15][2]])
                            elif board[w][q] == 'Q2':
                                temp = board[w][q]
                                QUEEN(w, q, bpos[16][2], 16, game_start)
                                if bsurround[16] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[16][2]])
                            elif board[w][q] == 'Q3':
                                temp = board[w][q]
                                QUEEN(w, q, bpos[17][2], 17, game_start)
                                if bsurround[17] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[17][2]])
                            elif board[w][q] == 'Q4':
                                temp = board[w][q]
                                QUEEN(w, q, bpos[18][2], 18, game_start)
                                if bsurround[18] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[18][2]])
                            elif board[w][q] == 'Q5':
                                temp = board[w][q]
                                QUEEN(w, q, bpos[19][2], 19, game_start)
                                if bsurround[19] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[19][2]])
                            elif board[w][q] == 'Q6':
                                temp = board[w][q]
                                QUEEN(w, q, bpos[20][2], 20, game_start)
                                if bsurround[20] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[20][2]])
                            elif board[w][q] == 'Q7':
                                temp = board[w][q]
                                QUEEN(w, q, bpos[21][2], 21, game_start)
                                if bsurround[21] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[21][2]])
                            elif board[w][q] == 'Q8':
                                temp = board[w][q]
                                QUEEN(w, q, bpos[22][2], 22, game_start)
                                if bsurround[22] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[22][2]])
                            elif board[w][q] == 'Q9':
                                temp = board[w][q]
                                QUEEN(w, q, bpos[23][2], 23, game_start)
                                if bsurround[23] == 1:
                                    break
                                else:
                                    alive.remove([w,q,bpos[23][2]])
                        print(temp)
                        ran_num1 = randint(0, len(valid_pos) - 1)
                        m = valid_pos[ran_num1][0]
                        n = valid_pos[ran_num1][1]
                        print('w,q=',w,',',q)
                        print('m,n=',m,',',n)
                        if temp[0] == 'P' and m == 7:
                            k = find_num(temp)
                            bpos[k][0] = bpos[k][1] = bpos[k][2] = -1
                            temp = 'Q' + str(b_queen_num)
                            print(temp)
                            k = find_num(temp)
                            bpos[k][2] = 1
                            b_queen_num += 1
                            print(b_queen_num)
                        if temp == 'K' and m == 0 and n == 2 and w == 0 and q == 4:
                            board[0][3] = 'R1'
                            board[0][0] = ' '
                            bpos[8][0] = 0
                            bpos[8][1] = 3
                        if temp == 'K' and m == 0 and n == 6 and w == 0 and q == 4:
                            board[0][5] = 'R2'
                            board[0][7] = ' '
                            bpos[9][0] = 0
                            bpos[9][1] = 5

                        if temp[0] == 'P' and m == 3 and w == 1:
                            if 0 < n and board[m][n - 1][0] == 'p':
                                k = find_num(board[m][n - 1])
                                wem_passent[k] = 2
                            if n < 7 and board[m][n + 1][0] == 'p':
                                k = find_num(board[m][n + 1])
                                wem_passent[k] = 1

                        if temp[0] == 'P' and board[m][n] == ' ':
                            if (m == w + 1 and n == q - 1) or (m == w + 1 and n == q + 1):
                                k = find_num(board[m - 1][n])
                                wpos[k][0] = wpos[k][1] = wpos[k][2] = -1
                                board[m - 1][n] = ' '

                        for i in wdefend_num:
                            wdefend_pos[i].clear()
                        wdefend_num.clear()

                        paths[bpos[15][0]][bpos[15][1]] = ' '

                        battack_piece.clear()
                        if board[m][n] == 'p1':
                            wpos[0][0] = -1
                            wpos[0][1] = -1
                            wpos[0][2] = -1
                        elif board[m][n] == 'p2':
                            wpos[1][0] = -1
                            wpos[1][1] = -1
                            wpos[1][2] = -1
                        elif board[m][n] == 'p3':
                            wpos[2][0] = -1
                            wpos[2][1] = -1
                            wpos[2][2] = -1
                        elif board[m][n] == 'p4':
                            wpos[3][0] = -1
                            wpos[3][1] = -1
                            wpos[3][2] = -1
                        elif board[m][n] == 'p5':
                            wpos[4][0] = -1
                            wpos[4][1] = -1
                            wpos[4][2] = -1
                        elif board[m][n] == 'p6':
                            wpos[5][0] = -1
                            wpos[5][1] = -1
                            wpos[5][2] = -1
                        elif board[m][n] == 'p7':
                            wpos[6][0] = -1
                            wpos[6][1] = -1
                            wpos[6][2] = -1
                        elif board[m][n] == 'p8':
                            wpos[7][0] = -1
                            wpos[7][1] = -1
                            wpos[7][2] = -1
                        elif board[m][n] == 'b1':
                            wpos[12][0] = -1
                            wpos[12][1] = -1
                            wpos[12][2] = -1
                        elif board[m][n] == 'b2':
                            wpos[13][0] = -1
                            wpos[13][1] = -1
                            wpos[13][2] = -1
                        elif board[m][n] == 'r1':
                            wpos[8][0] = -1
                            wpos[8][1] = -1
                            wpos[8][2] = -1
                        elif board[m][n] == 'r2':
                            wpos[9][0] = -1
                            wpos[9][1] = -1
                            wpos[9][2] = -1
                        elif board[m][n] == 'n1':
                            wpos[10][0] = -1
                            wpos[10][1] = -1
                            wpos[10][2] = -1
                        elif board[m][n] == 'n2':
                            wpos[11][0] = -1
                            wpos[11][1] = -1
                            wpos[11][2] = -1
                        elif board[m][n] == 'q1':
                            wpos[14][0] = -1
                            wpos[14][1] = -1
                            wpos[14][2] = -1
                        elif board[m][n] == 'q2':
                            wpos[16][0] = -1
                            wpos[16][1] = -1
                            wpos[16][2] = -1
                        elif board[m][n] == 'q3':
                            wpos[17][0] = -1
                            wpos[17][1] = -1
                            wpos[17][2] = -1
                        elif board[m][n] == 'q4':
                            wpos[18][0] = -1
                            wpos[18][1] = -1
                            wpos[18][2] = -1
                        elif board[m][n] == 'q5':
                            wpos[19][0] = -1
                            wpos[19][1] = -1
                            wpos[19][2] = -1
                        elif board[m][n] == 'q6':
                            wpos[20][0] = -1
                            wpos[20][1] = -1
                            wpos[20][2] = -1
                        elif board[m][n] == 'q7':
                            wpos[21][0] = -1
                            wpos[21][1] = -1
                            wpos[21][2] = -1
                        elif board[m][n] == 'q8':
                            wpos[22][0] = -1
                            wpos[22][1] = -1
                            wpos[22][2] = -1
                        elif board[m][n] == 'q9':
                            wpos[23][0] = -1
                            wpos[23][1] = -1
                            wpos[23][2] = -1
                        board[m][n] = temp
                        board[w][q] = ' '
                        if board[m][n] == 'P1':
                            if bpos[0][2] != -1:
                                bpos[0][0] = m
                                bpos[0][1] = n
                                bem_passent[0] = 0
                        elif board[m][n] == 'P2':
                            if bpos[1][2] != -1:
                                bpos[1][0] = m
                                bpos[1][1] = n
                                bem_passent[1] = 0
                        elif board[m][n] == 'P3':
                            if bpos[2][2] != -1:
                                bpos[2][0] = m
                                bpos[2][1] = n
                                bem_passent[2] = 0
                        elif board[m][n] == 'P4':
                            if bpos[3][2] != -1:
                                bpos[3][0] = m
                                bpos[3][1] = n
                                bem_passent[3] = 0
                        elif board[m][n] == 'P5':
                            if bpos[4][2] != -1:
                                bpos[4][0] = m
                                bpos[4][1] = n
                                bem_passent[4] = 0
                        elif board[m][n] == 'P6':
                            if bpos[5][2] != -1:
                                bpos[5][0] = m
                                bpos[5][1] = n
                                bem_passent[5] = 0
                        elif board[m][n] == 'P7':
                            if bpos[6][2] != -1:
                                bpos[6][0] = m
                                bpos[6][1] = n
                                bem_passent[6] = 0
                        elif board[m][n] == 'P8':
                            if bpos[7][2] != -1:
                                bpos[7][0] = m
                                bpos[7][1] = n
                                bem_passent[7] = 0
                        elif board[m][n] == 'B1':
                            bpos[12][0] = m
                            bpos[12][1] = n
                        elif board[m][n] == 'B2':
                            bpos[13][0] = m
                            bpos[13][1] = n
                        elif board[m][n] == 'R1':
                            bpos[8][0] = m
                            bpos[8][1] = n
                        elif board[m][n] == 'R2':
                            bpos[9][0] = m
                            bpos[9][1] = n
                        elif board[m][n] == 'N1':
                            bpos[10][0] = m
                            bpos[10][1] = n
                        elif board[m][n] == 'N2':
                            bpos[11][0] = m
                            bpos[11][1] = n
                        elif board[m][n] == 'Q1':
                            bpos[14][0] = m
                            bpos[14][1] = n
                        elif board[m][n] == 'K':
                            bpos[15][0] = m
                            bpos[15][1] = n
                            b_king_moved = 1
                        elif board[m][n] == 'Q2':
                            bpos[16][0] = m
                            bpos[16][1] = n
                        elif board[m][n] == 'Q3':
                            bpos[17][0] = m
                            bpos[17][1] = n
                        elif board[m][n] == 'Q4':
                            bpos[18][0] = m
                            bpos[18][1] = n
                        elif board[m][n] == 'Q5':
                            bpos[19][0] = m
                            bpos[19][1] = n
                        elif board[m][n] == 'Q6':
                            bpos[20][0] = m
                            bpos[20][1] = n
                        elif board[m][n] == 'Q7':
                            bpos[21][0] = m
                            bpos[21][1] = n
                        elif board[m][n] == 'Q8':
                            bpos[22][0] = m
                            bpos[22][1] = n

                        print(bpos)
                        count += 1
                        for i in range (24):
                            if wpos[i][2]!=-1 :
                                wpos[i][2]=1

                        FIND_KINGNEIGHBOUR(bpos[15][0],bpos[15][1])

                        wsurround[15]=0
                        king_involved[0]=0
                        board[wpos[15][0]][wpos[15][1]] = ' '
                        king(wpos[15][0], wpos[15][1], w_king_moved)
                        kingrestore(wpos[15][0], wpos[15][1])
                        board[wpos[15][0]][wpos[15][1]] = 'k'

                        if check()==1:
                            print('check!')
                            paths[wpos[15][0]][wpos[15][1]] = '$'
                            if PATHCHECK(CHECKPIECE[0],CHECKPIECE[1])==1 and wsurround[15]==0:
                                print('checkmate!')
                                for pos in battack_piece:
                                    paths[pos[0]][pos[1]]='!'
                                paths[CHECKPIECE[0]][CHECKPIECE[1]]='!'
                                if king_involved[0] == 1:
                                    paths[bpos[15][0]][bpos[15][1]]='!'
                                stop=1
                            for i in range(24):
                                if wpos[i][2] != -1 and wpos[i][2]!=9:
                                    wpos[i][2] = 0
                        elif wsurround[15]==0 and stalemate()==0:
                            for pos in battack_piece:
                                paths[pos[0]][pos[1]] = '!'
                            if king_involved[0] == 1:
                                paths[bpos[15][0]][bpos[15][1]] = '!'
                            stop = 1
                            print('stalemate!')
                        alive.clear()
                        valid_pos.clear()

            elif game_start == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mx>=320 and mx<=520 and my>=190 and my<=240:
                        game_start = 1
                    if mx>=320 and mx<=520 and my>=270 and my<=320:
                        game_start = 2
                    if mx>=320 and mx<=520 and my>=350 and my<=400:
                        game_start = 3




            mouse=pygame.mouse.get_pos()
            if game_start == 1 or game_start == 2:
                pygame.draw.rect(gamedisplay, black, (0, 0, display_width, display_height))
                disp_pass=0
                y=40
                for i in range(0,8):
                    x=40
                    for j in range(0,8):
                        if mouse[0] >= x and mouse[0] <= x+70 and mouse[1] >= y and mouse[1] <= y+70 and stop==0:
                            chess_square(gold,x,y,70)
                        elif paths[i][j]=='*' and board[i][j]!=' ':
                            chess_square(red,x,y,70)
                        elif paths[i][j]=='$':
                            chess_square(red, x, y, 70)
                        elif paths[i][j] == '*' and board[i][j] == ' ':
                            if (i+j)%2 == 0 :
                                chess_square(light_blue, x, y, 70)
                            else:
                                chess_square(blue,x,y,70)
                        elif paths[i][j]=='!':
                            chess_square(pink, x, y, 70)
                        else:
                            if (i+j) % 2 == 0:
                                chess_square(white, x, y,70)
                            else:
                                chess_square(brown, x, y, 70)
                        if board[i][j][0] == 'R':
                            gamedisplay.blit(brookimg, (x,y))
                        elif board[i][j][0] == 'N':
                            gamedisplay.blit(bknightimg, (x, y))
                        elif board[i][j][0] == 'B':
                            gamedisplay.blit(bbishopimg, (x, y))
                        elif board[i][j][0] == 'Q':
                            gamedisplay.blit(bqueenimg, (x, y))
                        elif board[i][j] == 'K':
                            gamedisplay.blit(bkingimg, (x, y))
                        elif board[i][j][0] == 'b':
                            gamedisplay.blit(wbishopimg, (x, y))
                        elif board[i][j][0] == 'n':
                            gamedisplay.blit(wknightimg, (x, y))
                        elif board[i][j][0] == 'r':
                            gamedisplay.blit(wrookimg, (x, y))
                        elif board[i][j] == 'k':
                            gamedisplay.blit(wkingimg, (x, y))
                        elif board[i][j][0] == 'q':
                            gamedisplay.blit(wqueenimg, (x, y))
                        elif board[i][j][0] == 'P':
                            gamedisplay.blit(bpawnimg, (x, y))
                        elif board[i][j][0] == 'p':
                            gamedisplay.blit(wpawnimg, (x, y))
                        x += 70
                    y += 70

            elif game_start == 0:
                pygame.draw.rect(gamedisplay, black, (0, 0, display_width, display_height))
                if mouse[0]>=320 and mouse[0]<=520 and mouse[1]>=190 and mouse[1]<=240:
                    pygame.draw.rect(gamedisplay, blue, (320,190, 200, 50))
                    text_display('player vs player',320,190,200,50)
                else:
                    pygame.draw.rect(gamedisplay, light_blue, (320, 190, 200, 50))
                    text_display('player vs player', 320, 190, 200, 50)

                if mouse[0]>=320 and mouse[0]<=520 and mouse[1]>=270 and mouse[1]<=320:
                    pygame.draw.rect(gamedisplay, blue, (320,270, 200, 50))
                    text_display('player vs computer',320,270,200,50)
                else:
                    pygame.draw.rect(gamedisplay, light_blue, (320, 270, 200, 50))
                    text_display('player vs computer', 320, 270, 200, 50)

                if mouse[0]>=320 and mouse[0]<=520 and mouse[1]>=350 and mouse[1]<=400:
                    pygame.draw.rect(gamedisplay, blue, (320,350, 200, 50))
                    text_display('Help',320,350,200,50)
                else:
                    pygame.draw.rect(gamedisplay, light_blue, (320, 350, 200, 50))
                    text_display('Help', 320, 350, 200, 50)

            elif game_start == 3:
                pygame.draw.rect(gamedisplay, black, (0, 0, display_width,display_height))
                if mouse[0]>=320 and mouse[0]<=420 and mouse[1]>=350 and mouse[1]<=400:
                    pygame.draw.rect(gamedisplay, blue, (320,350, 100, 50))
                    text_display('back',320,350,100,50)
                else:
                    pygame.draw.rect(gamedisplay, light_blue, (320, 350, 100, 50))
                    text_display('back', 320, 350, 100, 50)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse[0] >= 320 and mouse[0] <= 420 and mouse[1] >= 350 and mouse[1] <= 400:
                        game_start=0
                d=0
                f=0
                for letter in help1:
                    if letter == '\n':
                        d=0
                        f=f+20
                    text_display1(letter,d,f,display_width,display_height)
                    if letter=='l' or letter=='i' or letter=='r' or letter=='t' or letter=='f':
                        d=d+8
                    elif letter=='m':
                        d=d+16
                    else:
                        d=d+13
            elif game_start==4:
                pygame.draw.rect(gamedisplay, green, (280, 300, 400, 180))
                text_display('Do you want to play again?', 50, 270, 800, 300)
                if mouse[0]>=320 and mouse[0]<=420 and mouse[1]>=350 and mouse[1]<=400:
                    pygame.draw.rect(gamedisplay, blue, (320,350, 100, 50))
                    text_display('yes',320,350,100,50)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        reset1()
                        from chess_func import *
                        mx = 0
                        my = 0
                        w = 0
                        q = 0
                        count = 0
                        temp = 0
                        game_start=0
                        stop=0
                        print(paths)
                        print(board)
                else:
                    pygame.draw.rect(gamedisplay, light_blue, (320, 350, 100, 50))
                    text_display('yes', 320, 350, 100, 50)
                if mouse[0] >= 520 and mouse[0] <= 620 and mouse[1] >= 350 and mouse[1] <= 400:
                    pygame.draw.rect(gamedisplay, blue, (520, 350, 100, 50))
                    text_display('no', 520, 350, 100, 50)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        off=True
                else:
                    pygame.draw.rect(gamedisplay, light_blue, (520, 350, 100, 50))
                    text_display('no', 520, 350, 100, 50)



        pygame.display.update()
        clock.tick(60)
pygame.quit()