'''
    문제설명
        백준 15649 N과 M(1) (DFS, 재귀함수 이용)
        1부터 N까지의 자연수 중에서 중복 없이 M개를 고른 수열 모두 찾기
    해결전략
        상태트리를 그린다. 
        순열의 결과를 담는 res 리스트와 이 숫자를 사용했는지를 체크하는 ch 리스트를 만든다.
        DFS 함수에서 파라미터 L은 재귀함수의 깊이, 선택한 숫자의 개수, res 리스트의 인덱스를 의미한다.
        호출한 DFS의 L이 길이와 같아질 때 순열을 출력한다.
        그렇지 않으면 1부터 n까지 가지를 뻗는다.(기존 순열에 추가한다)
            1. 이 숫자를 앞에서 사용했는지 확인
            2. 사용하지 않았으면 사용했다고 표시하고 순열에 추가
            3. 이 순열을 기반으로 DFS를 재귀호출해 순열을 계속 추가한다.
            4. 재귀호출을 마친 뒤에는 체크 리스트를 다시 0으로 초기화해준다.
        DFS 함수 호출을 기준으로 위는 호출 전에 수행하는 것, 아래는 함수 수행을 마치고 리턴한 후에 수행하는 것임을 기억!
        여기서는 함수 리턴 후 체크리스트를 초기화해주는 것이 중요하다. 
'''
def DFS(L):
    if L == m:
        for j in range(m):
            print(res[j], end = ' ')
        print()
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0

n, m = map(int, input().split())
res = [0] * n
ch = [0] * (n+1)
DFS(0)