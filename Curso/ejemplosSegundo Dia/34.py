#!/usr/bin/env python3
import sys,os,random,datetime
def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.getenv('USERNAME'))
    print(os.getenv('HOSTNAME'))
    print(os.urandom(8).hex())
    print(random.randint(1,1000))
    print(datetime.datetime.now())
    print(datetime.datetime.now().year)
    print(datetime.datetime.now().month)
if __name__ == '__main__': main()
