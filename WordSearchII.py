# @author: sagarkar10@gmail.com

class TrieNode:
    def __init__(self):
        self.next = [None for i in xrange(26)]
        self.word = None


class Solution(object):
    def __init__(self):
        self.res = None
        self.m = None
        self.n = None

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0 or len(board[0]) == 0:
            return []
        root = TrieNode()
        self.res = []

        for word in words:
            curr = root
            for char in word:
                idx = ord(char) - 97
                if curr.next[idx] == None:
                    curr.next[idx] = TrieNode()
                curr = curr.next[idx]
            curr.word = word

        self.m, self.n = len(board), len(board[0])
        for i in xrange(self.m):
            for j in xrange(self.n):
                self.dfs(board, i, j, root)
        return self.res

    def dfs(self, board, i, j, curr_node):
        tmp = board[i][j]
        if tmp == '#' or curr_node.next[ord(tmp) - 97] == None:
            return
        board[i][j] = '#'
        curr_node = curr_node.next[ord(tmp) - 97]
        if curr_node.word != None:
            self.res.append(curr_node.word)
            curr_node.word = None
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for move in moves:
            if 0 <= i + move[0] < self.m and 0 <= j + move[1] < self.n:
                self.dfs(board, i + move[0], j + move[1], curr_node)
        board[i][j] = tmp

