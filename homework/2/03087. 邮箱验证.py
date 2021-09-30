while True:
    try:
        address = input()
        if address.count("@") == 1 and address[0] not in r"@." and address[-1] not in r"@." and address[
            address.index("@") - 1] != ".":
            after_at = address[address.index("@") + 1:]
            if r"." in after_at and after_at[0] != r".":
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    except EOFError:
        break
