from classes import *
key_list = ["항공여행","관광 여행","고속도로","서울여행","부산여행","제주도여행","2칸 뒤로","3칸 뒤로","무인도로 가시오","사회복지기금 배당","세계일주","우주여행","우주여행",\
    "노벨 평화상", "노후연금", "복권당첨" ,"생일 축하", "자동차 경주 우승","장학금",\
    "건물 방범비","건물 수리비","건물 정기종합소득세","과속운전","병원비","해외유학",\
    "반액대매출","반액대매출","무인도 탈출권","우대권","우대권"]


def use_key(players,ply,key,board):
    no = key_list.index(key)
    if no == 0:
        print("[ 항공여행 ]\n콩코드 여객기를 타고 타이베이로 떠난다.")
        if 15 < ply.location:
            ply.money += 20
        ply.money += 20
        if board[15].owner != None:
            payment(ply,board[15].hipass,board[15].owner,players)
        ply.location = 1
    elif no == 1:
        print("[ 관광 여행 ]\n퀸 엘리자베스 호를 타고 홍콩 으로 떠난다.")
        if 28 < ply.location:
            ply.money += 20
        ply.money += 20
        if board[28].owner != None:
            payment(ply,board[28].hipass,board[28].owner,players)
        ply.location = 3
    elif no == 2:
        print("[ 고속도로 ]\n출발지로 이동한다.")
        if 0 < ply.location:
            ply.money += 20
        ply.location = 0
    elif no == 3:
        print("[ 서울여행 ]\n서울로 이동한다.")
        if 39 < ply.location:
            ply.money += 20
        ply.location = 39
    elif no == 4:
        print("[ 부산여행 ]\n부산으로 이동한다.")
        if 25 < ply.location:
            ply.money += 20
        ply.location = 25
    elif no == 5:
        print("[ 제주도여행 ]\n제주도로 이동한다.")
        if 5 < ply.location:
            ply.money += 20
        ply.location = 5
    elif no == 6:
        print("[ 2칸 뒤로 ]\n2칸 뒤로 이동한다.")
        ply.location -= 2
    elif no == 7:
        print("[ 3칸 뒤로 ]\n3칸 뒤로 이동한다.")
        ply.location -= 3
    elif no == 8:
        print("[ 무인도로 가시오 ]\n무인도로 이동한다.")
        if 10 < ply.location:
            ply.money += 20
        ply.location = 10
    elif no == 9:
        print("[ 사회복지기금 배당 ]\n사회복지기금 수령처로 이동한다.")
        if 20 < ply.location:
            ply.money += 20
        ply.location = 20
    elif no == 10:
        print("[ 세계일주 ]\n한바퀴 돌아 제자리로 돌아온다.")
        ply.money += 20
    elif no == 11 or no == 12:
        print("[ 우주여행 ]\n우주여행 승강장으로 이동한다.")
        if 30 < ply.location:
            ply.money += 20
        ply.location = 30
    
    elif no == 13:
        print("[ 노벨 평화상 ]\n30만원을 획득합니다.")
        ply.money += 30
    elif no == 14:
        print("[ 노후연금 ]\n5만원을 획득합니다.")
        ply.money += 5
    elif no == 15:
        print("[ 복권당첨 ]\n20만원을 획득합니다.")
        ply.money += 20
    elif no == 16:
        print("[ 생일 축하 ]\n모두에게서 1만원을 획득합니다.")
        for l in players:
            payment(l,1,ply,players)
    elif no == 17:
        print("[ 자동차 경주 우승 ]\n10만원을 획득합니다.")
        ply.money += 10
    elif no == 18:
        print("[ 장학금 ]\n10만원을 획득합니다.")
        ply.money += 10

    elif no == 19:
        print("[ 건물 방범비 ]\n건물의 방범비를 지불해야 합니다.")
        print(f"당신의 호텔수 : {ply.hotel}")
        print(f"당신의 빌딩수 : {ply.building}")
        print(f"당신의 별장수 : {ply.mention}")
        print(f"총 금액 : ({(5 * ply.hotel + 3 * ply.building + 1 * ply.mention)})")
        ply.money -= (5 * ply.hotel + 3 * ply.building + 1 * ply.mention)
    elif no == 20:
        print("[ 건물 수리비 ]\n건물의 수리비를 지불해야 합니다.")
        print(f"당신의 호텔수 : {ply.hotel}")
        print(f"당신의 빌딩수 : {ply.building}")
        print(f"당신의 별장수 : {ply.mention}")
        print(f"총 금액 : ({(10 * ply.hotel + 6 * ply.building + 3 * ply.mention)})")
        ply.money -= (10 * ply.hotel + 6 * ply.building + 3 * ply.mention)
    elif no == 21:
        print("[ 건물 방범비 ]\n건물의 방범비를 지불해야 합니다.")
        print(f"당신의 호텔수 : {ply.hotel}")
        print(f"당신의 빌딩수 : {ply.building}")
        print(f"당신의 별장수 : {ply.mention}")
        print(f"총 금액 : ({(15 * ply.hotel + 10 * ply.building + 5 * ply.mention)})")
        ply.money -= (15 * ply.hotel + 10 * ply.building + 5 * ply.mention)
    elif no == 22:
        print("[ 과속운전 ]\n5만원을 지불합니다.")
        ply.money += 10
    elif no == 23:
        print("[ 병원비 ]\n5만원을 지불합니다.")
        ply.money += 10
    elif no == 24:
        print("[ 해외유학 ]\n10만원을 지불합니다.")
        ply.money += 10

    elif no == 25 or no == 26: # 건물 판매 수정 필요
        print("[ 반액대매출 ]\n자신이 가진 가장 비싼 부동산을 반값으로 매각해야 합니다.")
        max_value = 0
        for b in ply.own:
            if board[b].value > max_value:
                max_value = board[b].value
                max_value_city = b
        board[max_value_city].owner = None
        ply.money += board[max_value_city].value /2
        ply.own.remove(max_value_city)
        