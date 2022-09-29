from argparse import ArgumentParser

args=ArgumentParser(description="cmdline args")

#now we have to add the arguments into it 

args.add_argument("--num1",type=int,default=0,help="add a number")
args.add_argument("--num2",type=int,default=0,help="add a number")
args.add_argument("--opt",type=str,default="+",help="provide the operation")

#now we have to iterate through the args
all_args=args.parse_args()
if all_args.opt=="+":
    print(all_args.num1+all_args.num2)

