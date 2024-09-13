from math import isqrt

#### Fonction secondaire


def isprime(p):
    n=isqrt(p)
    v=True
    for i in range(1,n):
        if p%i==0:
            v=False
            break
    return(v)

    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
