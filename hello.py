@lambda _: _()
def func() -> str:
    def inner_func() -> str:
        print('Inner function was called')
        return 'innerfunction'
    print('Hii')
    return inner_func

print(func)
print(func())

print('Hi from Python')