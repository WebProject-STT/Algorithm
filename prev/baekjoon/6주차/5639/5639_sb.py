# 이진검색트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) # 최대 재귀 깊이 설정 (python에서만 먹힘)

def post_order(start, end) :
    if start > end : # start가 더 크면 index 범위를 넘어가므로 return
        return
    
    split = end + 1 # 분할 할 위치 저장
    for i in range(start + 1, split) : # 분할 할 위치 찾기
        if tree[start] < tree[i] : # start를 root라 했을 때 그것보다 크면 오른쪽 노드임
            split = i # 오른쪽 노드의 위치를 분할 할 위치로 지정
            break
    
    post_order(start + 1, split - 1) # 왼쪽 노드 검사
    post_order(split, end) # 오른쪽 노드 검사
    
    print(tree[start]) # root 위치를 출력

if __name__ == "__main__" :
    tree = []
    while True :
        try :
            tree.append(int(input()))
        except :
            break
    post_order(0, len(tree)-1)

'''
# pypy3로 통과하는 코드

class Node :
    def __init__(self, data) :
        self.data = data
        self.left = self.right = None
    
class BST :
    def __init__(self) :
        self.root = None
    
    def insert(self, data) :
        if self.root == None :
            self.root = Node(data)
        else :
            node = self.root
            while True :
                if node.data > data :
                    if node.left == None :
                        node.left = Node(data)
                        break
                    node = node.left
                else :
                    if node.right == None :
                        node.right = Node(data)
                        break
                    node = node.right
    
    def post_order(self, node) :
        s = []
        while True :
            while node :
                if node.right :
                    s.append(node.right)
                s.append(node)
                node = node.left
            node = s.pop()
            if node.right and (s[-1] if len(s) else None) == node.right :
                s.pop()
                s.append(node)
                node = node.right
            else :
                print(node.data)
                node = None
            if not s :
                break

if __name__ == "__main__" :
    bst = BST()
    while True :
        try :
            data =int(input())
            bst.insert(data)
        except :
            break
    bst.post_order(bst.root)
'''

''' python 기준 시간 초과, pypy 기준 런타임에러
class Node :
    def __init__(self, data) :
        self.data = data # 노드 값
        self.left = self.right = None # 좌우 노드

class BST : # BinarySearchTree Class
    def __init__(self) :
        self.root = None # 비어있는 트리로 초기화
    
    def insert(self, data) :
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    
    def _insert_value(self, node, data) :
        if node is None :
            node = Node(data)
        else :
            if data <= node.data :
                if node.left != None :
                    node.left = self._insert_value(node.left, data)
                else :
                    node.left = Node(data)
            else :
                if node.right != None :
                    node.right = self._insert_value(node.right, data)
                else :
                    node.right = Node(data)
        return node
    
    def post_order(self):
        def _post_order(root):
            if root is None:
                pass
            else:
                _post_order(root.left)
                _post_order(root.right)
                print(root.data)
        _post_order(self.root)
        
if __name__ == "__main__" :
    
    bst = BST()
    
    while True :
        try :
            data = int(input())
        except :
            break
        bst.insert(data)
    
    bst.post_order()
'''