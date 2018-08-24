#!/usr/bin/env python3
import time2words
def main():
    lista=['11:55','00:00','15:55','09:55','10:55']
    for x in lista:print('{} -> {}'.format(x,time2words.t2w(x)))
if __name__=='__main__':main()
