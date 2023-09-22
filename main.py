
import model


def print_hi():
    k = 1
    while k == 1:
        code = input("""
                        0 - exit
                        3 - add
                        5 - change
                        7 - print 
                        ::: """)

        match code:
            case "0":
                print("exit")
                k = 0
            case "3":
                model.add_to_note()
            case "5":
                model.change_to_note()
            case "7":
                model.print_the_note()
            case "8":
                model.del_the_note()

if __name__ == '__main__':
    print_hi()


