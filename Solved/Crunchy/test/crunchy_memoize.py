#!/usr/bin/env python3
import functools

@functools.lru_cache(maxsize=1000)  # for memoization
def crunchy(n):
    if n < 2: return n
    return (6 * crunchy(n - 1)%100000007 + crunchy(n - 2)%100000007)%100000007


g = 17665922529512695488143524113273224470194093921285273353477875204196603230641896039854934719468650093602325707751568

'''
# testing
for x in range(100):
    print(f"crunchy({x})", (crunchy(x)), (crunchy(x)%100000007))
'''

stored_pattern = []
@functools.lru_cache(maxsize=1000)  # for memoization
def calculate_next(fn, fn_minus):
    fn_plus = (6 * fn + fn_minus) % 100000007
    return fn_plus

n = 100
fn = crunchy(n)
fn_minus = crunchy(n-1)
assert (6 * fn + fn_minus) % 100000007 == crunchy(n+1) % 100000007

while n < g:
    # calculate next
    fn_plus = calculate_next(fn, fn_minus)
    
    # shift variables
    n += 1
    fn_minus = fn
    fn = fn_plus

    # store pattern until there is a repetition
    #if fn in stored_pattern:
    '''
    if fn in stored_pattern:
        repeated_n = stored_pattern.index(fn)
        if stored_pattern[repeated_n-1] == fn_minus:
            print('Pattern:', stored_pattern)
            print('Repeat of fn_minus:', fn_minus)
            print('Repeat of fn:', fn)
            fn_plus = calculate_next(fn, fn_minus)
            print('Repeat of fn_plus:', fn_plus)
            print('n:', n)
            break
    '''

    if fn in stored_pattern:
        print('Pattern at?:', n)
        index = stored_pattern.index(fn)
        fn_plus = calculate_next(fn, fn_minus)
        if stored_pattern[index+1] == fn_plus:
            print('Pattern:', stored_pattern)
            print('Repeat of fn_minus:', fn_minus)
            print('Repeat of fn:', fn)
            print('Repeat of fn_plus:', fn_plus)
            print('n:', n)
            break

    stored_pattern.append(fn)

# calculate equivalent index of g using the repetition knowledge
pattern_start_index = stored_pattern.index(fn)
pattern_length = len(stored_pattern) - pattern_start_index

g_offset = (g - n) - pattern_start_index
g_offset_index = (g_offset % pattern_length) + pattern_start_index

print("crunchy(g-1): INSA{%d}" % stored_pattern[g_offset_index]-1)
print("crunchy(g): INSA{%d}" % stored_pattern[g_offset_index])
print("crunchy(g+1): INSA{%d}" % stored_pattern[g_offset_index+1])
quit()


# f(n) = 6*f(n-1)+f(n-2)
# f(n) = 6*(6*f(n-2)+f(n-3))+f(n-2)

# f(n) = 36*f(n-2) + 6*f(n-3) + f(n-2)
# f(n) = 37*f(n-2) + 6*f(n-3)
# f(n-3) = 37*f(n-5) + 6*f(n-6)
# f(n-2) = 37*f(n-4) + 6*f(n-5)


# f(n+2) = 37*f(n) + 6*f(n-1)

'''
n = 10
fn = crunchy(n)
fn_minus = crunchy(n-1)
assert (37 * fn + 6 * fn_minus) % 100000007 == crunchy(n+2) % 100000007


@functools.lru_cache(maxsize=None)  # for memoization
def calculate_next(fn, fn_minus):
    fn_plus2 = (37 * fn + 6 * fn_minus) % 100000007
    return fn_plus2

while n < g:
    # calculate next
    fn_plus2 = calculate_next(fn, fn_minus)
    # shift variables
    n += 2
    fn_minus = fn
    fn = fn_plus2
'''


print("Your flag is: INSA{%d}"%(crunchy(g)%100000007))
