
# Operation code to mnemonic dictionary
# You can use this to lookup the machine code
# and translate it to the mnemonic instruction
INS_REF = {
    1: "ADD",
    2: "SUB",
    3: "STA",
    5: "LDA",
    6: "BRA",
    7: "BRZ",
    8: "BRP"
}

def disassemble(operation_code):
    # this function should take in an integer operation code
    # and convert it to a LMC mnemonic instruction and return
    # it as a string
    code = str(operation_code)
    string = ""
    if (code[0] == "0"):
        string = "HLT"
    if (code[0] == "1"):
        string = "ADD" + " " + code[1] + code[2]
    if (code[0] == "2"):
        string = "SUB" + " " + code[1] + code[2]
    if (code[0] == "3"):
        string = "STA" + " " + code[1] + code[2]
    if (code[0] == "5"):
        string = "LDA" + " " + code[1] + code[2]
    if (code[0] == "6"):
        string = "BRA" + " " + code[1] + code[2]
    if (code[0] == "7"):
        string = "BRZ" + " " + code[1] + code[2]
    if (code[0] == "8"):
        string = "BRP" + " " + code[1] + code[2]
    if (code[0] == "9"):
        if (code[2] == "1"):
            string = "INP"
        if (code[2] == "2"):
            string = "OUT"
    return string

def main():
    # The main function should read all operation codes from the
    # user until the HLT instruction is read. Once it is read,
    # all operation codes should be disassembled using "disasassembled"
    # and then printed out to the user
    dict_list = []
    operation_code = ""
    print("Input")
    while not(operation_code == 000):
        operation_code = int(input(""))
        instruct = disassemble(operation_code)
        dict_list.append(instruct)
    print("Output")
    for i in range(len(dict_list)):
        print(dict_list[i])
