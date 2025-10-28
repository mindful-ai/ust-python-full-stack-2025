import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

class Huffman:

    def build_huffman_tree(self, text):
        freq = Counter(text)
        heap = [Node(ch, fr, None, None) for ch, fr in freq.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = Node(None, left.freq + right.freq, left, right)
            heapq.heappush(heap, merged)

        return heap[0]

    def generate_codes(self, node, code="", code_map={}):
        if node is None:
            return
        if node.char is not None:
            code_map[node.char] = code
        self.generate_codes(node.left, code + "0", code_map)
        self.generate_codes(node.right, code + "1", code_map)
        return code_map

    def encode(self, text, codes):
        return ''.join(codes[ch] for ch in text)

    def decode(self, encoded, root):
        decoded_text = ""
        current = root
        for bit in encoded:
            current = current.left if bit == "0" else current.right

            # when the lead node is reached
            if current.char is not None:
                decoded_text += current.char
                current = root

        return decoded_text

if __name__ == "__main__":

    def test_huffman(text):
    
        print("-"*80)

        h = Huffman()

        root = h.build_huffman_tree(text)
        codes = h.generate_codes(root)

        print("Character Codes: ")
        for ch, code in codes.items():
            print(f"{ch}   -> {code}")

        encoded = h.encode(text, codes)

        print("\nEncoded Bitstring: ", encoded)
        print("Original Bits:", len(text) * 8)
        print("Compressent Bits: ", len(encoded))
        print("Compression Ratio: ", len(encoded)/len(text)*8)

        decoded = h.decode(encoded, root)
        print("\nDecoded Text: ", decoded)

        print("\nSuccessful Decompression: ", (decoded == text))

    test_huffman(text = "Huffman coding is the best compression algorithm")
    test_huffman(text = "Test another piece of text for compression with huffman coding")
    test_huffman(text = " lkadjsfoieowqfncvaskdncv;akjfn;aksdj;jtrkngvam,ngdv;adskljfqgerfnv,zxvn  ")
