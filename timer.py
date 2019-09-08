import time
class Timer:
    """
    Собственно, класс для расчета времени выполнения функции. Можно
    использовать и как декоратор, и как контекстный менеджер.
    """
    def __init__(self):
    #При создании экземпляра класса никаких агрументов не передаем
        pass
        
    def __enter__(self):
    #При использовании как контекстный менеджер замеряет время входа в него
        self.t0 = time.time()
        return self
    
    def __call__(self, num_runs=10):
    #Используется при вызове как функции (то есть для декоратора); передаем
    #аргументом количество прогонов для исследуемой функции (по умолчанию 10)
        def decorator(func):
            def wrap(param):
                total_time = 0
                for i in range(num_runs):
                    t0 = time.time()
                    func(param)
                    t1 = time.time()
                    total_time += (t1 - t0)
                print("Total execution took {:.10f} seconds".format(total_time))
                print("Average execution time was {:.10f} seconds".format(total_time/num_runs))
            return wrap
        return decorator
    
    def __str__(self):
    #На всякий случай, если захочется узнать, что этот класс делает.
        return "This is a timer for other functions"
    
    def __exit__(self, *args):
    #Замеряет время выхода из контекстного менеджера и печатает, сколько времени
    #выполнялись команды в теле
        t1 = time.time()
        print("Total execution took {:.10f} seconds".format(t1-self.t0))
        return self
        
        

