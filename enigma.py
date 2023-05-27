import tkinter

def initial_setup():
    global roter_used
    global roters
    for i in range(3):
        while True:
            msg = "ENTER ROTER", i + 1, "(INPUT NUMBER BETWEEN 1 TO 5):"
            x = int(input(msg))
            if x not in (1, 2, 3, 4, 5):
                print("INVALID INPUT. TRY AGAIN.")
            else:
                roters_used.append(roters[i-1])
                break
    

def encrypt_roter(roter, ch):
    ch_index = ord(ch) - 65
    return roter[ch_index]

def reflect(ch):
    if ch in reflector[0]:
        index = reflector[0].index(ch)
        return reflector[1][index]
    else:
        index = reflector[1].index(ch)
        return reflector[0][index]
    
def rev_encrypt(roter, ch):
    ch_index = roter.index(ch)
    ch_found = chr(65 + ch_index)
    return ch_found

def rotate_1():
    global roter1
    rot1 = roter1[:1]
    rot2 = roter1[1:]
    roter1 = rot2 + rot1
def rotate_2():
    global roter2
    rot1 = roter2[:1]
    rot2 = roter2[1:]
    roter2 = rot2 + rot1
def rotate_3():
    global roter3
    rot1 = roter1[:1]
    rot2 = roter1[1:]
    roter3 = rot2 + rot1

roter1 = "XULEYABTQWHFSZGOKRCVINMDJP"
roter2 = "BEYCJZXDLGRSUPVMIKWOHFANTQ"
roter3 = "PJGXLNWHIDMBTVFUARKQZYOSCE"
roter4 = "JBWNEVCOUTZFSGKLDIRMAYXQHP"
roter5 = "WRZTILNJXOUSGECQDKYMHBPAVF"
roters = [roter1, roter2, roter3, roter4, roter5]
roters_used = []

reflector = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'],
             ['O', 'S', 'W', 'Y', 'R', 'Z', 'Q', 'T', 'X', 'P', 'U', 'V', 'N']]

#initial_setup()

msg = input("Enter message to be encrypted:")
encrypt_msg = ""
for ch in msg:
    rotate_1()
    en_ch = encrypt_roter(roter1, ch)
    en_ch = encrypt_roter(roter2, en_ch)
    en_ch = encrypt_roter(roter3, en_ch)
    en_ch = reflect(en_ch)
    en_ch = rev_encrypt(roter3, en_ch)
    en_ch = rev_encrypt(roter2, en_ch)
    en_ch = rev_encrypt(roter1, en_ch)
    encrypt_msg = encrypt_msg + en_ch

print(encrypt_msg)
