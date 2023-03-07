MORSE_CODE = { 
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',

    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    
    '9': '----.', ' ': '/'
} #Morse code dictionary 



class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_tree(node, level=0, label='/'):
    if node is not None:
        print_tree(node.right, level+1, '/')
        print(' ' * 4 * level + label + str(node.val))
        print_tree(node.left, level+1, '\\')

root = Node(4)
root.left = Node(6)
root.left.left = Node(7)
root.left.right = Node(5)
root.right = Node(2)
root.right.left = Node(3)  
root.right.right = Node(1)

print_tree(root)


def encode(msg: str) -> str:
    encoded_msg = []
    for char in msg.upper():
        if char in MORSE_CODE:
            encoded_msg.append(MORSE_CODE[char])
    return ' '.join(encoded_msg)

def decode(msg: str) -> str:
    decoded_msg = []
    for code in msg.split():
        for char, morse in MORSE_CODE.items():
            if morse == code:
                decoded_msg.append(char)
    return ''.join(decoded_msg)

# User Input 
while True:
    choice = input("Do you wish to encode (e) or decode (d): ").upper()
    if choice == 'E':
        msg = input("Message to encode: ")
        encoded_msg = encode(msg)
        print("Here is your encoded message:", encoded_msg)
        break
    elif choice == 'D':
        msg = input("Message to decode: ")
        decoded_msg = decode(msg)
        print("Here is your decoded message:", decoded_msg)
        break

    else:
        print("Invalid Input")
