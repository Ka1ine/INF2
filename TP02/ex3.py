from timeit import timeit

def fibonacci_recursif(n):
    if n == 0:
        return n
    elif n==1:
        return n
    else:
        return fibonacci_recursif(n-1) + fibonacci_recursif(n-2)

#le temps entre répétitions n'est pas linéaire, la fonction commence a consommer beaucoup de temps pour un haut nombre de répétitions.

def fibonacci_iteratif(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        j = 0
        k = 1
        for i in range(n-1) :
            temp = j
            j = k
            k = temp + k
        return k

def cache(f):
    caches = {}
    def wrapper(*args, **kwargs):
        cle =(args, tuple(kwargs.items()))
        if cle in caches:
            return caches[cle]
        else :
            caches[cle] = f(*args, **kwargs)
            return caches[cle]
    return wrapper

@cache
def fibonacci_cache(n):
    if n == 0:
        return n
    elif n==1:
        return n
    else:
        return fibonacci_cache(n-1) + fibonacci_cache(n-2)

def main() :
    print("Recursif(35): ", timeit("fibonacci_recursif(35)", globals=globals(), number=1))
    print("Recursif(36): ", timeit("fibonacci_recursif(36)", globals=globals(), number=1))
    print("Iteratif(35): ", timeit("fibonacci_iteratif(35)", globals=globals(), number=1))
    print("Iteratif(36): ", timeit("fibonacci_iteratif(36)", globals=globals(), number=1))
    print("Cache(35): ", timeit("fibonacci_cache(35)", globals=globals(), number=1))
    print("Cache(36): ", timeit("fibonacci_cache(36)", globals=globals(), number=1))

if __name__ == "__main__":
    main()

#on remarque que les temps sont de l'ordre de x10e-6 plus rapides pour la fonction iterative

#Avec le décorateur cache, on peut observer que la fonction récursive devient aussi rapide que l’itérative,
#contrairement à la récursive simple qui croît de façon exponentielle et devient lente pour des grands n.
