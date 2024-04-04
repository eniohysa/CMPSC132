def main():
    pass


def repeat_message(times):
    if times > 0:
        for i in range(times):
            print('Hello world')


def recursive_message(times):
    if times > 0:
        print('Hello world!')
        recursive_message(times-1)


def factorial(n):
    if n > 0:
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)
