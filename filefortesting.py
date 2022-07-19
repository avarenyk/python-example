def test(*args):
    args = list(args)
    args.sort()
    return args

print (test(5,6,4,7))