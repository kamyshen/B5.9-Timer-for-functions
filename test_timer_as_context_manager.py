from timer import Timer
import time

def fib_func(top):
    """
    Функция создает список из чисел Фибоначчи, начиная с 1 и 2, где последнее число меньше
    указанного параметра top, и распечатывает этот список, а потом список только четных чисел
    из первого списка
    """
    fib = []
    fib.append(1)
    fib.append(2)
    i = 2
    while True:
        fib.append(fib[i-2]+fib[i-1])
        if fib[i] >= top:
            fib.pop()
            break
        i += 1
    print(f"Это весь список чисел Фибоначчи от 1 до {top}: {fib}\n")
    print(f"Это четные числа из нашего списка: {[x for x in fib if x%2 == 0]}\n")


with Timer():
    print("testing our Timer as a context manager...\n")
    fib_func(100000000)
    time.sleep(1)
    #чтобы хоть какое-то время увидеть, отличное от нуля, вставил задержку на 1 секунду

    
