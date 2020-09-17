# started in : 08:35 - 27/08/2020

def operations(num1, num2):
    sume = num1 + num2
    subt = num1 - num2
    mult = num1 * num2
    divi = num1 / num2
    expo = num1 ** num2
    sqrt = num1 ** (num2**-1)
    return print(sume, subt, mult, divi, expo, sqrt)
    pass

operations.num1 = int(input("Primeiro numero: "))
operations.num2 = int(input("Segundo numero: "))
operations(operations.num1, operations.num2)

def leitura(arg1, arg2, arg3):
    arg1 = ["Developer", 9.5, "Eng.Elet"]
    arg2 = ("Anonymous", 8.0, "Eng.Comp")
    arg3 = {"Name": "Brazilian",
            "Note": 7.5,
            "Course": "Info.System"}
    return print(len(leitura.arg1))
    pass