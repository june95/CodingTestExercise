def solution(board):
    ''' 프로그래머스 혼자서 하는 틱택톡 풀이'''
    answer = 1
    cnt_O = 0
    cnt_X = 0
    tmp_board = []
    
		# tmp_board에 '.'일 경우 0, 'O'일 경우 1, 'X'일 경우 10 형태로 숫자로 채워 넣기
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '.':
                tmp_board.append(0)
            elif board[i][j] == 'O':
                tmp_board.append(1)
                cnt_O += 1                # O의 개수
            else:
                tmp_board.append(10)
                cnt_X += 1                # X의 개수
    
		# X의 개수가 많거나, O의 개수가 2개 이상 많으면 잘못된 틱택토
    if cnt_X > cnt_O or cnt_O - cnt_X >= 2:
        return 0
    
    for i in range(0, len(board)):
				# 각 열이 O로 이긴 경우, X가 한 번 더 두었을 때
        if sum(tmp_board[i::3]) == 3 and cnt_O - cnt_X == 0:
            return 0
				# 각 열이 X로 이긴 경우, O가 한 번 더 두었을 때
        if sum(tmp_board[i::3]) == 30 and cnt_O - cnt_X == 1:
            return 0
				# 왼쪽 위부터 내려오는 대각선 O로 이긴 경우, X가 한 번 더 두었을 때
        if i == 0 and sum(tmp_board[i::4]) == 3 and cnt_O - cnt_X == 0:
            return 0
				# 왼쪽 위부터 내려오는 대각선 X로 이긴 경우, O가 한 번 더 두었을 때
        if i == 0 and sum(tmp_board[i::4])  == 30 and cnt_O - cnt_X == 1:
            return 0
				# 오른쪽 위부터 내려오는 대각선 O로 이긴 경우, X가 한 번 더 두었을 때
        if i == 2 and sum(tmp_board[i:-2:2]) == 3 and cnt_O - cnt_X == 0:
            return 0
				# 오른쪽 위부터 내려오는 대각선 X로 이긴 경우, O가 한 번 더 두었을 때
        if i == 2 and sum(tmp_board[i:-2:2])  == 30 and cnt_O - cnt_X == 1:
            return 0
        
    for i in range(0, len(tmp_board), 3):
				# 각 행이 O로 이긴 경우, X가 한 번 더 두었을 때
        if sum(tmp_board[i:i+3]) == 3 and cnt_O - cnt_X == 0:
            return 0
				# 각 행이 X로 이긴 경우, O가 한 번 더 두었을 때
        if sum(tmp_board[i:i+3])  == 30 and cnt_O - cnt_X == 1:
            return 0
        
    return answer