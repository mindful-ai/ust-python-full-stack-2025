🧠 What is Huffman Coding?

    Huffman Coding is a lossless data compression algorithm.
    It reduces the number of bits required to store or transmit data by assigning shorter binary 
    codes to frequent characters and longer codes to rare characters.

    And at the core of it lies a Binary Tree, called a Huffman Tree.

🌳 How It Uses Trees

    Each unique character is treated as a leaf node in a tree.
    The frequency (occurrence count) of each character becomes its weight.

    Repeatedly:

    Pick two nodes with the smallest frequencies.
    Create a new internal node with a frequency equal to their sum.
    The two nodes become left and right children of the new node.
    The final single node is the root of the Huffman Tree.

    Assign:

    0 for the left edge
    1 for the right edge

The path from root to leaf becomes the character’s binary code.

⚙️ Real Industry Usage

| Domain                | Example                                               |
| --------------------- | ----------------------------------------------------- |
| **File compression**  | ZIP, GZIP use Huffman coding internally               |
| **Image compression** | JPEG uses Huffman for encoding quantized coefficients |
| **Audio compression** | MP3, FLAC                                             |
| **Video compression** | MPEG and H.264 use similar entropy coding             |
| **Networking**        | HTTP/2 header compression (HPACK) uses Huffman coding |

Core Concepts Needed to Understand Huffman Coding:

🧩 1️⃣ What Is a Heap?

    A heap is a special kind of binary tree where:
    The parent node is always smaller (min-heap) or larger (max-heap) than its children.
    It’s a complete binary tree (all levels are filled except possibly the last).
    In Huffman coding, we use a min-heap (smallest frequency has the highest priority).

🧠 2️⃣ Why Do We Use a Heap in Huffman?

    The Huffman algorithm needs to repeatedly pick two smallest frequency elements to merge them into one new node.
    If we used a normal list or array:
    We’d have to sort it or search for the smallest two items each time, which costs O(n log n) or worse.

    With a min-heap:

    We can efficiently extract the two smallest items in O(log n) time.
    Insert a new merged node back in O(log n) time.
    That efficiency makes heaps perfect for Huffman trees.

🔍 Quick Analogy

    Think of the heap as a priority line at the airport:
    Smallest-frequency characters get priority boarding.
    Two lowest ones are merged together (like forming one group).
    That group’s new frequency (sum) goes back in line.
    Repeat until only one group (root) is left — everyone is connected!

Pseudo-code:

function huffman_encode(text):
    freq = count_frequencies(text)
    heap = create_min_heap_of_leaf_nodes(freq)
    while heap.size > 1:
        L = heap.pop_min()
        R = heap.pop_min()
        P = new internal node with freq = L.freq + R.freq
        P.left = L; P.right = R
        heap.push(P)
    root = heap.pop()
    codes = traverse_tree_and_generate_codes(root)  # map symbol->bits
    encoded = "".join(codes[ch] for ch in text)
    return encoded, root   # must return or store root/codebook


function huffman_decode(encoded_bits, root):
    result = ""
    node = root
    for bit in encoded_bits:
        node = node.left if bit == '0' else node.right
        if node.is_leaf:
            result += node.symbol
            node = root
    return result
