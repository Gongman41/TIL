T = int(input())
for test_case in range(1, T + 1):
    sudoku_numbers = [list(map(int, input().split())) for _ in range(9)]  # 전체 스도쿠 그리드 읽기
    is_valid = True

    # 각 행에 대한 중복 확인
    for row in sudoku_numbers:
        if len(set(row)) != 9:
            is_valid = False
            break

    # 각 열에 대한 중복 확인
    for col in zip(*sudoku_numbers):
        if len(set(col)) != 9:
            is_valid = False
            break
        '''
        for col in zip(*sudoku_numbers)는 스도쿠의 각 열에 대한 반복문입니다.

zip(*sudoku_numbers)는 sudoku_numbers 리스트의 각 행을 튜플로 묶어주는 역할을 합니다.
zip 함수에 *를 사용하면, 리스트의 각 행을 풀어서(언패킹) 전달하게 됩니다. 따라서 zip(*sudoku_numbers)는 스도쿠의 각 열에 대한 튜플들을 생성합니다.
이후에는 if len(set(col)) != 9를 통해 현재 열에 중복된 숫자가 있는지 확인합니다. set(col)은 현재 열의 원소들을 중복을 제거하고 유일한 값들의 집합(set)으로 만듭니다. 따라서 만약 중복된 숫자가 있다면, set의 길이는 9보다 작아집니다. 이 경우에는 is_valid를 False로 설정하고 루프를 종료합니다.


        '''

    # 3x3 서브그리드에 대한 중복 확인
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [sudoku_numbers[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(subgrid)) != 9:
                is_valid = False
                break

    if is_valid:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
