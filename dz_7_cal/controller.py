import model
import view
import re

def oper(o):
    if o == "+":
        return model.summa()
    elif o == "-":
        return model.raznica()


def start():
    view.showinfo("hello welcome to calculator!")
    a = view.get_num("Введите значение один --> ")
    b = view.get_num("Введите значение два --> ")
    operant = view.get_num("введите оперант + или - : --> ")

    model.init(a,b)
    view.showinfo(oper(operant))
