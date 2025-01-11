def print_diamond_shape():
    print("  __________")
    print(" /          \\")
    print("/            \\")
    print("\\            /")
    print(" \\          /")
    print("  \\        /")
    print("   \\      /")
    print("    \\    /")
    print("     \\  /")
    print("      \\/")


print_diamond_shape()

def print_custom_shape():
    n = 4 
    for i in range(n):
        if i == 0:
            print(" " * 5 + "*" * 6) 
        elif i == 1:
            print(" " * 3 + "*" + " " * 8 + "*") 
        elif i == 2:
            print(" " * 5 + "*" + " " * 4 + "*") 
        elif i == 3:
            print(" " * 8 + "*") 

print_custom_shape()

