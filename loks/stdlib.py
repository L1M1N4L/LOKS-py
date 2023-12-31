from .types import Nil, String, Number, Array, Boolean
from .error import TypeErr, ValueErr
from typing import Union


def loks_print(argList: list) -> Nil:
    output: str = str(argList[0])

    if type(argList[0]).__name__ == "String":
        output = output[1:-1]

    print(output, end='')
    return Nil()


def loks_println(argList: list) -> Nil:
    output: str = str(argList[0])

    if type(argList[0]).__name__ == "String":
        output = output[1:-1]

    print(output)
    return Nil()


def loks_input(argList: list) -> String:
    inpstr = argList[0].value
    return String(input(inpstr))


def loks_len(el: list) -> Number:
    e: Union[String, Array] = el[0]
    if type(e).__name__ == "String":
        return Number(len(e.value))

    if type(e).__name__ == "Array":
        return Number(len(e._arr))

    raise TypeErr(f"Invalid argument type for len, '{type(e).__name__}'")


def loks_int(el: list) -> Number:
    s = el[0].value
    if type(el[0]).__name__ == "Boolean":
        if s == "true":
            s = 1
        if s == "false":
            s = 0

    try:
        int(s)
    except:
        raise ValueErr(f"Invalid literal for conversion to int, '{s}'")
    
    return Number(int(s))


def loks_str(el: list) -> String:
    return String(str(el[0]))


def loks_isinteger(el: list) -> Boolean:
    if type(el[0]).__name__ != "String":
        raise TypeErr("Argument for 'isinteger' must be of type String")

    def getBoolObj(b) -> Boolean:
        if b:
            return Boolean("true")
        else:
            return Boolean("false")

    s = el[0].value

    if len(s) == 0:
        return Boolean("false")
    
    if s[0] in ('-', '+'):
        return getBoolObj(s[1:].isdigit())

    return getBoolObj(s.isdigit())


builtinFunctionTable = {
    "print" : loks_print,
    "println" : loks_println,
    "input" : loks_input,
    "len" : loks_len,
    "int" : loks_int,
    "str" : loks_str,
    "isinteger" : loks_isinteger
}

# <function name> : (<index>, <argc>)
builtinFunctionInfo = {
    "print" : (0, 1),
    "println" : (1, 1),
    "input" : (2, 1),
    "len" : (3, 1),
    "int" : (4, 1),
    "str" : (5, 1),
    "isinteger" : (6, 1)
}

builtinFunctionIndex = {
    0: "print",
    1: "println",
    2: "input",
    3: "len",
    4: "int",
    5: "str",
    6: "isinteger"
}
