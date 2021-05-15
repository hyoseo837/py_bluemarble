import os

city_list = ["타이페이","홍콩","마닐라","싱가포르","카이로","이스탄불",\
    "아테네", "코펜하겐","스톡홀름","취리히","베를린","몬트리올",\
    "부에노스 아이레스","상파울로", "시드니","하와이", "리스본", "마드리드",\
    "도쿄","파리","로마","런던","뉴욕"]
city_cost = [(5,0.2),(8,0.4),(8,0.4),(10,0.6),(10,0.6),(12,0.8),\
    (14,1),(16,1.2),(16,1.2),(18,1.4),(18,1.4),(20,1.6),\
    (22,1.8),(24,2),(24,2),(26,2.2),(26,2.2),(28,2.4),\
    (30,2.6),(32,2.8),(32,2.8),(35,3.5),(35,3.5)]

korea_list = ["제주도","부산","서울"]
korea_cost = [(20,30),(50,60),(100,200)]

ride_list = ["콩코드 여객기","퀸 엘리자베스 호","콜럼비아 호"]
ride_cost = [(20,30),(30,25),(45,40)]


def prt_board(board, players,turn):
    os.system("cls")
    c = 0
    for i in board:
        print(i , "| ",end="")
        try:
            if i.owner == players[0].name:
                b = players[0].mark
            elif i.owner == players[1].name:
                b = players[1].mark
            else:
                b = " "
        except:
            b = " "
        print(f"{b}",end="| ")
        for k in players:
            if k.location == c:
                print(k.mark,end=" ")
        print()
        c += 1
        if c % 10 == 0:
            print(" "*21 + "|  | ")
    print()
    print("="*5 +f"{players[turn].name:=<5}"+f"{round(players[turn].money,1):=>10}"+" 만원")