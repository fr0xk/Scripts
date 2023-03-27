# Advanced Static Typing

from typing import List, Tuple

def function(a: int, b: str, c: List[float], d: Tuple[int, str]) -> bool:

    return True

# Pointers (via ctypes)

import ctypes

x = ctypes.c_int(5)

y = ctypes.c_int()

y_ptr = ctypes.pointer(y)

y_ptr.contents.value = x.value + 2

print("Value of y:", y.value)

# Bitwise operations

x = 0b11001100

y = 0b10101010

z = x & y

print(bin(z)) # Outputs 0b10001000

# Function pointers (via higher-order functions)

def add(a, b):

    return a + b

def subtract(a, b):

    return a - b

def apply_operation(func, a, b):

    return func(a, b)

print(apply_operation(add, 5, 3)) # Outputs 8

print(apply_operation(subtract, 5, 3)) # Outputs 2

# Memory allocation using the ctypes module

import ctypes

buffer = ctypes.create_string_buffer(10) # Allocates 10 bytes of memory

buffer.value = b"Hello"

print(buffer.raw) # Outputs b'Hello\x00\x00\x00\x00\x00'

# Function pointers (via ctypes)

import ctypes

libc = ctypes.CDLL(None)

add_func = libc.add

add_func.restype = ctypes.c_int

add_func.argtypes = [ctypes.c_int, ctypes.c_int]

result = add_func(5, 3)

print(result) # Outputs 8

# Inline Assembly (via the asmjit module)

import asmjit

code = asmjit.codegen.CodeHolder()

code.init_memory()

func = asmjit.Function(code, asmjit.call_conv.STDCALL, asmjit.TypeId.INT32, [asmjit.TypeId.INT32])

x = asmjit.x86.X86Assembler(code)

x.mov(asmjit.x86.rax, asmjit.Imm(42))

x.ret()

x.finalize()

code.sync()

func_ptr = code.get_func()

result = func_ptr(1)

print(result) # Outputs 42

