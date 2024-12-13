# from numba import cuda
# import numpy as np
# from numba import cuda
# import time
#
# start_time = time.time()
# cuda.detect()
#
# @cuda.jit
# def add_arrays_gpu(a, b, result):
#     idx = cuda.grid(1)
#     if idx < result.size:
#         result[idx] = a[idx] + b[idx]
#
# # Daten initialisieren
# n = 100000
# a = np.random.rand(n).astype(np.float32)
# b = np.random.rand(n).astype(np.float32)
# result = np.zeros_like(a)
#
# # GPU Berechnung starten
# threadsperblock = 256
# blockspergrid = (a.size + (threadsperblock - 1)) // threadsperblock
# add_arrays_gpu[blockspergrid, threadsperblock](a, b, result)
#
# print(result)
# # Dein GPU-Code
# end_time = time.time()
# print(f"GPU execution time: {end_time - start_time} seconds")

import pyopencl as cl
import numpy as np

# Erstelle Kontext und Warteschlange
platform = cl.get_platforms()[0]  # Nimm die erste Plattform
device = platform.get_devices()[0]  # Nimm das erste Gerät
context = cl.Context([device])  # Erstelle einen Kontext für das Gerät
queue = cl.CommandQueue(context)  # Erstelle eine Warteschlange für den Kontext

# Erstelle einige Daten auf der CPU
a_np = np.random.rand(50000).astype(np.float32)
b_np = np.random.rand(50000).astype(np.float32)

# Erstelle Puffer auf der GPU
mf = cl.mem_flags
a_g = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
b_g = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)
result_g = cl.Buffer(context, mf.WRITE_ONLY, b_np.nbytes)

# Erstelle und baue das Kernel-Programm
program = cl.Program(context, """
__kernel void sum(__global const float *a, __global const float *b, __global float *result) {
    int gid = get_global_id(0);
    result[gid] = a[gid] + b[gid];
}
""").build()

# Führe den Kernel aus
program.sum(queue, a_np.shape, None, a_g, b_g, result_g)

# Hole das Ergebnis zurück auf die CPU
result_np = np.empty_like(a_np)
cl.enqueue_copy(queue, result_np, result_g)

# Überprüfe das Ergebnis
