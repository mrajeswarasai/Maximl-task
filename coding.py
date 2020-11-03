def subString(line):
    n = len(line)
    n_d = len(list(set(line)))
    n_l = n
    
    for i in range(n):
        for j in range(n):
            ss = line[i:j]
            ss_l = len(ss)
            ss_d = len(list(set(ss)))
            
            if ss_l < n_l and n_d == ss_d:
                n_l = ss_l
    return n_l

def main():
    line = input()
    print(subString(line))

if __name__ == '__main__':
    main()