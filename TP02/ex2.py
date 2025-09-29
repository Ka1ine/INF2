from time import sleep

def cache(f):
    caches={}
    def wrapper(*args, **kwargs):
        cle =(args, tuple(kwargs.items()))
        if cle in caches:
            print('Résultat du cache')
            return caches[cle]
        else :
            print('Calculant résultat')
            caches[cle] = f(*args, **kwargs)
            return caches[cle]
    return wrapper

@cache
def fonction(x):
    sleep(3)
    x = x + 1
    return x

def main():
    x=fonction(2)
    print(x)
    x=fonction(2)
    print(x)

if __name__ == '__main__':
    main()