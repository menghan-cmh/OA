def main(input):
    if input == "":
        return ""
    
    input = input.split("\n")
    output = []
    for line in input:
        temp = ""
        count = []
        for i in range(len(line)):
            if line[i] != "(" and line[i] != ")":
                temp += " "
            elif line[i] == "(":
                count.append(i)
                temp += "x"
            elif line[i] == ")":
                if len(count) == 0:
                    temp += "?"
                if len(count) > 0:
                    temp += " "
                    temp = temp[:count[-1]] + " " + temp[count[-1]+1:]
                    count.pop()
        output.append(line)
        output.append(temp)
    return "\n".join(output)
                


if __name__ == "__main__":
    # input = "bgs))))"
    # output = "bgs))))\n   ????"

    input = "(saf)))()((\n)))sdfa((("
    output = "(saf)))()((\n     ??  xx\n)))sdfa(((\n???    xxx"

    print(main(input))
    assert main(input) == output