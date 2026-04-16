from time import sleep

#metodo iterativo
def countdown(n):
    while n >= 0 :
        print(n)
        sleep(1) #pausa di 1 secondo
        n -= 1

#metodo ricorsivo
def countdown_recursive(n):
    # condizione terminale
    if n == 0:
        print("Stop")
    # condizione non terminale
    else:
        print(n)
        sleep(1)
        countdown_recursive(n-1)


if __name__ == "__main__":
    N = 4
    countdown_recursive(N)