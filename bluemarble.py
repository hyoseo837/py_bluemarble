from citys import *
import random,time
from classes import *

def roll_dice():
    return random.randrange(1,7) + random.randrange(1,7)

def payment(player,cost,to,players):
    player.pay(cost)
    for w in players:
        if w.name == to:
            w.money += cost
    print(f"{player.name} => {cost} 만원 => {to}")

class player():
    def __init__(self, order, money, mark):
        self.name = "여행자 " + str(order)
        self.location = 0
        self.money = money
        self.mark = mark
        self.own = []
        self.island = 0
        self.item = []
        self.space_trip = 0
    
    def __str__(self):
        return self.name

    def pay(self,cost):
        if self.money >= cost:
            self.money -= cost

board = []
players = []
running = True
turn = 1

donation = 0
citicount = 0
koreacount = 0
ridecount = 0

for i in range(40):
    if i not in [0,2,5,7,10,12,15,17,20,22,25,28,30,32,35,38,39]:
        board.append(city(city_list[citicount],i,city_cost[citicount]))
        citicount += 1
    elif i in [5,25,39]:
        board.append(korea(korea_list[koreacount],i,korea_cost[koreacount]))
        koreacount += 1
    elif i in [15,28,32]:
        board.append(ride(ride_list[ridecount],i,ride_cost[ridecount]))
        ridecount += 1
    elif i in [2,7,12,17,22,35]:
        board.append(golden_key("황금 열쇠",i))
    elif i == 38:
        board.append(donate_box("사회복지기금 접수처",i))
    elif i == 0:
        board.append(start("출발",i))
    elif i == 10:
        board.append(island("무인도",i))
    elif i == 20:
        board.append(donate_hub("사회복지기금 수령처",i))
    elif i == 30:
        board.append(space_trip("우주 여행",i))


players.append(player(1,100,"@"))
players.append(player(2,100,"$"))

while running:
    turn += 1
    if turn > len(players)-1:
        turn -= len(players)
    prt_board(board,players,turn)
    ply = players[turn]

    if ply.island > 0: # 무인도
        input(f"탈출 시도 ({4-ply.island}/3)")
        a = random.randrange(1,7)
        b = random.randrange(1,7)
        print(a,b)
        if a == b:
            ply.island = 0
            pass
        else:
            ply.island -= 1
            input("턴 종료 ")
            continue
    
    if ply.space_trip == 1:
        ply.space_trip = 0
        print("우주 여행을 합니다. 몇칸을 더 가고 싶으신가요? (1~39)")
        while True:
            try:
                k = int(input())
                if k > 0 and k < 40:
                    break
                print("값이 너무 작거나 큽니다")
            except:
                print("다시 입력해주세요")
                pass
    else:
        input("주사위 굴리기 ")
        k = roll_dice()
    print(k)
    ply.location += k
    if ply.location >= 40: # 월급 
        print("출발지를 지나 월급 20 만원을 획득합니다.")
        ply.money += 20
        time.sleep(0.5)
        ply.location -= 40
    time.sleep(0.5)

    prt_board(board,players,turn)

    spot = ply.location
    
    if board[spot].type in [1,2]:

        if board[spot].owner == None: # 땅 사기
            prt_board(board,players,turn)
            print(f"'{board[spot].name}'은 사유지가 아닙니다. 가격 : {board[spot].cost} \n1. 구매하기\n2. 넘어가기")

            while True:
                coi = input()
                if coi == "1":
                    if ply.money >= board[spot].cost:
                        board[spot].owner = ply.name
                        ply.money -= board[spot].cost
                        ply.own.append(spot)
                        break
                    print("돈이 부족합니다")
                elif coi == "2":
                    break

        elif board[spot].owner == ply.name: # 건물 건설 (작업 필요)
            prt_board(board,players,turn)
            print(f"'{board[spot]}'은 당신의 사유지입니다.")
            if board[spot].type == 2:
                continue
            print("1. 건물 건설하기\n2. 넘어가기")
            while True: 
                coi = input()
                if coi == "1":
                    print()
                    print("어떤 건물을 건설하실 건가요?\n1. 별장 \n2. 빌딩\n3. 호텔")
                    while True:
                        cio = input()
                        if cio in ["1","2","3"]:
                            break
                    
                    if cio == "1":
                        break
                elif coi == "2":
                    break
        
        elif board[spot].owner != ply.name: # 통행료 받기 (추가 작업 필요)
            print(f"{board[spot].owner}의 사유지에 침범하였습니다.")
            print(f"통행료 {board[spot].hipass} 만원을 내야 합니다.")
            input()
            payment(ply,board[spot].hipass,board[spot].owner,players)

    elif board[spot].type == 3:
        print("무인도에 남겨졌습니다.")
        input()
        ply.island = 3

    elif board[spot].type == 4: # 황금 열쇠 (작업 필요)
        pass

    elif board[spot].type == 5:
        print("사회복지기금에 기부해주세요 (15 만원)")
        input()
        if ply.money >= 15:
            ply.money -= 15
            donation += 15
        else:
            donation += ply.money
            ply.money = 0

    elif board[spot].type == 6:
        if donation > 0:
            print(f"사회복지기금을 수령하십시오 {donation}만원")
            ply.money += donation
            donation = 0
            input()

    elif board[spot].type == 7:
        ply.space_trip = 1
        print("다음턴에 우주여행을 할수 있습니다.")
        if board[32].owner != None:
            continue
        elif board[32].owner in [players[0].name,players[1].name]:
            payment(ply,20,board[32].owner,players)

    prt_board(board,players,turn)
    input("턴 종료 ")