def fn():   # 1번 특징
    fn2()

def fn2():  # 2번 특징
    # global a
    a = 2
    print(a)

a = 1       # 3번 특징

fn()
print(a)
