# A와 B

if __name__ == "__main__":
    S = input()
    T = [t for t in input()]
    
    lens = len(T)-len(S)
    idx = -1
    for _ in range(lens):
        n = T.pop(idx)
        if n == 'B':
            if idx == -1: idx = 0
            else: idx = -1            
    
    T = "".join(T)
    if idx == 0: T = T[::-1]
    if S == T: print(1)
    else: print(0)