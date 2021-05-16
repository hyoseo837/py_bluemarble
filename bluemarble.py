from citys import *
import random,time
from classes import *
from gold_key import *

def roll_dice():
    return random.randrange(1,7) + random.randrange(1,7)


class player():
    def __init__(self, name, money, mark, location = 0):
        self.name = name
        self.location = location
        self.money = money
        self.mark = mark
        self.own = []
        self.island = 0
        self.item = []
        self.space_trip = 0
        self.hotel = 0
        self.building = 0
        self.mention = 0
    
    def __str__(self):
        ln = len(self.name)
        string = self.name + " "*(6 - ln*2 + self.name.count(" "))
        return string

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
# ============================================= 게임 준비 ======================================================
key_deck = key_list.copy()
random.shuffle(key_deck)

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
        board.append(space_trip("우주 여행 승강장",i))

players.append(player("횩서",351,"@"))
players.append(player("유야호",351,"$"))

# =============================================================================================================


# ============================================= 게임 시작 ======================================================
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
            if "무인도 탈출권" in ply.item:
                if input("무인도 탈출권이 있습니다. 사용하시겠습니까? (y/n): ") == "y":
                    ply.item.remove("무인도 탈출권")
                    ply.island = 0
                    pass
                else:
                    ply.island -= 1
                    input("\n\n턴 종료 ")
                    continue
            else:
                ply.island -= 1
                input("\n\n턴 종료 ")
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
    
    if board[spot].type == 4: # 황금 열쇠 사용
        print("=====[ 황금열쇠 ]=====")
        key = key_deck.pop()
        if key in key_list[-3:]:
            print(f"{key} 를 획득 하였습니다. 보관후 나중에 사용할 수 있습니다.")
            ply.item.append(key)
        else:
            use_key(players,ply,key,board)
            key_deck += [key]
        input()
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
            print(f"'{board[spot].name}'은 당신의 사유지입니다.")
            if board[spot].type == 2 or board[spot].build != None:
                input("\n\n턴 종료 ")
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
                        if ply.money >= 5 * (spot//10 + 1):
                            ply.money -= 5 * (spot//10 + 1)
                            ply.mention += 1
                            board[spot].build = "mention"
                            board[spot].value += board[spot].b_cost[0]
                            break
                    elif cio == "2":
                        if ply.money >= 15 * (spot//10 + 1):
                            ply.money -= 15 * (spot//10 + 1)
                            ply.building += 1
                            board[spot].build = "building"
                            board[spot].value += board[spot].b_cost[1]
                            break
                    elif cio == "3":
                        if ply.money >= 25 * (spot//10 + 1):
                            ply.money -= 25 * (spot//10 + 1)
                            ply.hotel += 1
                            board[spot].build = "hotel"
                            board[spot].value += board[spot].b_cost[2]
                            break
                elif coi == "2":
                    break
        
        elif board[spot].owner != ply.name: # 통행료 받기 (추가 작업 필요)
            print(f"{board[spot].name}은 {board[spot].owner}님의 사유지입니다.")
            print(f"통행료 {board[spot].hipass} 만원을 내야 합니다.")
            input()
            payment(ply,board[spot].hipass,board[spot].owner,players)

    elif board[spot].type == 3:
        print("무인도에 남겨졌습니다.")
        ply.island = 3

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
            print(f"사회복지기금을 수령하십시오 ({donation}만원)")
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

    input("\n\n턴 종료 ")
