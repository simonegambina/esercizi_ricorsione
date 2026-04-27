import copy
from functools import lru_cache


# caso con liste

def anagrammi(parola):
    soluzioni = []

    ricorsione([], parola, soluzioni)
    return soluzioni

def ricorsione(parziale: list, rimanenti: str, soluzioni: list) -> list:
    # caso terminale
    if len(rimanenti) == 0:
        soluzioni.append(copy.deepcopy(parziale))

    # caso ricorsivo
    else:
        for i in range(len(rimanenti)):     # DOG
            parziale.append(rimanenti[i])       # D
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i+1:]       # OG
            ricorsione(parziale, nuovi_rimanenti, soluzioni)
            parziale.pop()



# caso con stringhe

def anagrammi_str(parola):
    soluzioni = set()       # per evitare che si ripetano soluzioni uguali

    ricorsione_str("", parola, soluzioni)
    return soluzioni



def ricorsione_str(parziale: str, rimanenti: str, soluzioni):
    # caso terminale
    if len(rimanenti) == 0:
        soluzioni.add(copy.deepcopy(parziale))

    # caso ricorsivo
    else:
        for i in range(len(rimanenti)):  # DOG
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i + 1:]  # OG
            ricorsione_str(parziale + rimanenti[i], nuovi_rimanenti, soluzioni)


# terza versione

def anagrammi_str2(parola):
    soluzioni = set()       # per evitare che si ripetano soluzioni uguali

    ricorsione_str2("", parola)

@lru_cache(maxsize=None)        # questo mi consente di stampare una volta sola le parole uguali,
#ma per farlo gli argomenti delle funzioni devono essere hashable

def ricorsione_str2(parziale: str, rimanenti: str):
    # caso terminale
    if len(rimanenti) == 0:
        print(parziale)

    # caso ricorsivo
    else:
        for i in range(len(rimanenti)):  # DOG
            nuovi_rimanenti = rimanenti[:i] + rimanenti[i + 1:]  # OG
            ricorsione_str2(parziale + rimanenti[i], nuovi_rimanenti)



if __name__ == '__main__':
    print(anagrammi('casa'))

    print(anagrammi_str('casa'))

    anagrammi_str2("aaaa")