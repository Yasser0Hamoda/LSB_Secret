import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(freq=node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]


def build_huffman_codes(tree):
    codes = {}

    def generate_codes(node, current_code=""):
        if node:
            if node.char is not None:
                codes[node.char] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")

    generate_codes(tree)
    return codes


def huffman_encode(text):
    tree = build_huffman_tree(text)
    codes = build_huffman_codes(tree)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, tree, codes


# Example usage (can be removed when importing as a module)
if __name__ == "__main__":
    input_text = input("Enter text to encode using Huffman: ")
    encoded, tree, codes = huffman_encode(input_text)
    print("Encoded binary:", encoded)
    print("Huffman codes:", codes)