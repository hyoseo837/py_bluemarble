import os

city_list = ["타이페이","홍콩","마닐라","싱가포르","카이로","이스탄불",\
    "아테네", "코펜하겐","스톡홀름","취리히","베를린","몬트리올",\
    "부에노스 아이레스","상파울로", "시드니","하와이", "리스본", "마드리드",\
    "도쿄","파리","로마","런던","뉴욕"]
city_cost = [(5,0.2,1,9,25),(8,0.4,2,18,45),(8,0.4,2,18,45),(10,0.6,3,27,55),(10,0.6,3,27,55),(12,0.8,4,30,60),\
    (14,1,5,45,75),(16,1.2,6,50,90),(16,1.2,6,50,90),(18,1.4,7,50,95),(18,1.4,7,50,95),(20,1.6,8,55,100),\
    (22,1.8,9,70,105),(24,2,10,75,110),(24,2,10,75,110),(26,2.2,11,80,115),(26,2.2,11,80,115),(28,2.4,12,85,120),\
    (30,2.6,13,90,127),(32,2.8,15,100,140),(32,2.8,15,100,140),(35,3.5,17,110,150),(35,3.5,17,110,150)]
korea_list = ["제주도","부산","서울"]
korea_cost = [(20,30),(50,60),(100,200)]

ride_list = ["콩코드 여객기","퀸 엘리자베스 호","콜럼비아 호"]
ride_cost = [(20,30),(30,25),(45,40)]


def prt_board(board, players,turn,donation):
    os.system("cls")
    c = 0
    for i in players:
        print(f"{i}  {i.mark}| 돈: {round(i.money,1)}만원   아이템:{i.item}")
    print("_"*25)
    print(f"사회복지기금 모금액 : {donation}")
    print("_"*25)
    print()
    for i in board:
        print(i , "| ",end="")
        try:
            m = " "
            for v in players:
                if i.owner == v.name:
                    m = v.mark
        except:
            pass

        try:
            if i.build == "mention":
                b = "■"
            elif i.build == "building":
                b = "▦"
            elif i.build == "hotel":
                b = "▥"
            else:
                b = " "
        except:
            b = " "

        print(f"{m} | {b}",end="| ")
        for k in players:
            if k.location == c:
                print(k.mark,end=" ")
        print()
        c += 1
        if c % 10 == 0:
            print(" "*21 + "|   |  |  ")
    print()
    print("="*5 +f"{players[turn].name:=<10}"+f"{round(players[turn].money,1):=>15}"+" 만원")