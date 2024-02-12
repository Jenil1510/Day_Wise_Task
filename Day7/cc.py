from functools import wraps
# functools.wraps is a decorator that can be used to modify a function or method by updating its metadata.
import time

def executetime(func):
    @wraps(func)
    def timecounting(*args, **kwargs):
        time1=time.perf_counter()
        result=func(*args, **kwargs)
        time2=time.perf_counter()
        total=(time2-time1)
        print(f'Function {func.__name__}{args} {kwargs} Took {total:.4f} seconds')
        return result
    return timecounting

@executetime

def calculate(num):
    sum1=sum((x for x in range(0,num**2)))
    return sum1

if __name__=='__main__':
    calculate(10)
    calculate(100)
    calculate(1000)