import argparse

if __name__ == '__main__':
    parser= argparse.ArgumentParser()
    parser.add_argument("--num1",type=int,help="provide a number",default=10)
    parser.add_argument("--num2",type=int,help="provide another number",default=20)
    parser.add_argument("--operation",help="provide an operation",default="add")
    all_args=parser.parse_args()
    # print(all_args)

    def foo(a,b):
        return a+b
    
    if all_args.operation=="add":
        print(foo(int(all_args.num1),int(all_args.num2)))   

