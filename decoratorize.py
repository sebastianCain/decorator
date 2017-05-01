from time import time
def time_decorate(f):
    def get_time(*args):
        t1 = time()*1000
        f(*args)
        t2 = time()*1000
        print("ms to run: " + str(t2-t1))
    return get_time


def arg_decorate(f):
    def get_args(*args):
        for a in args:
            print f.__name__ + ": (" + str(a) + ")"
        f(*args)
    return get_args

@arg_decorate
@time_decorate
def funcy(r, s):
    for i in range(r, s):
        i = i ** 4
        print i

funcy(100, 200)

