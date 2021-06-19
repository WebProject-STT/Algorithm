# 암호 만들기

def make_word(cur_string, idx, count1, count2): # count1 = 자음, count2 = 모음
    if len(cur_string) == L:
        if count1 < 2 or count2 < 1: return
        
        print(cur_string)
        return
    
    for i in range(idx, C):
        if not visited[i]:
            visited[i] = 1
            if alpha[i] == 'a' or alpha[i] == 'e' or alpha[i] == 'i' or alpha[i]=='o' or alpha[i] == 'u':
                make_word(cur_string+alpha[i], i+1, count1, count2+1)
            else:
                make_word(cur_string+alpha[i], i+1, count1+1, count2)
            visited[i] = 0

if __name__ == "__main__":
    L, C = map(int, input().split())
    alpha = input().split()
    
    visited = [0]*C
    alpha.sort()
    make_word('', 0, 0, 0)
