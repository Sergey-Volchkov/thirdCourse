import sys
import argparse

def Parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--poly', default='Havent arguments')
    param_value = parser.parse_args(sys.argv[1:]) 
    param_value = param_value.poly 
    masParams = param_value.split(',')
    return masParams
def convertToFloat(masParams):
    for i in range(len(masParams)):
        masParams[i] = float(masParams[i])
    n=0
    #print(masParams)
    while n < len(masParams):
        #print(masParams)
        #print(n)
        if masParams[n] == 0:
            del masParams[n]
        else:n+=1
    #print(masParams)
    return masParams

def main():
    masParams = Parser()
    masParams = convertToFloat(masParams)
    print(sum(list(map(lambda masParams: 1 / masParams * 3, masParams))))
if __name__ == '__main__':
    main()