from greenlet import greenlet


def printer():
    while True:
        data = g_cons.switch()
        print(data)


def consumer():
    while True:
        g_print.switch(input("введи ченить: "))


if __name__ == "__main__":
    g_cons = greenlet(consumer)
    g_print = greenlet(printer)
    g_print.switch()
