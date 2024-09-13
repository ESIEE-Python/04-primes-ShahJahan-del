""" importation de isqrt pour utilisation dans isprime """
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Teste la primalité de p

    Args:
        p: valeur entière positive
    
    Returns:
        isprime(p): True or False
    """
    v=True
    for i in range(2,int(sqrt(p))):
        if p%i==0:
            v=False
    return v


#### Fonction principale



def main():
    """
    Appels à la fonction isprime

    Args:
        pas d'argument
    Returns:
        main(): tous les nombres premiers de 1 à 100
    
    """

    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()

$ git pull
$ git add .
$ git commit -m "fonction isprime"
$ git push
