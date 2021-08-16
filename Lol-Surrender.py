print('\'찬성\'과 \'반대\'로만 입력해주세요.')
time = int(input('지금이 몇분인가요?: '))

vote_list = [] # 찬, 반을 담을 list 생성

if 15 <= time <= 20:
    for i in range(1, 6):
        vote = input(f'{i}번째 투표해주세요.: ')
        if vote == '찬성' or vote == '반대':
            vote_list.append(vote)
            if vote_list.count('반대') <= 1:
                pass
            else:
                print('항복이 부결되었습니다.')
                break
elif time <= 15:
    print('-' * 44)
    print(f'''15분을 넘지 않으므로 투표를 할 수 없습니다.
앞으로 {15-time}분 남았습니다.''')
    print('-' * 44)
else:
    for i in range(1, 6):
        vote = input(f'{i}번째 투표해주세요.: ')
        if vote == '찬성' or vote == '반대':
            vote_list.append(vote)
            if vote_list.count('반대') <= 2:
                pass
            else:
                print('항복이 부결되었습니다.')
                break