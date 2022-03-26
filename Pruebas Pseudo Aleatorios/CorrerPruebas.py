from PruebasMedias import prueba_medias
from PruebaUniformidad import prueba_uniformidad
from PruebaVarianza import prueba_varianza

alpha = 0.05

# Lista de numeros pseudoaleatorios
nums = [
    0.6034,
    0.5546,
    0.3434,
    0.5830,
    0.9123,
    0.9237,
    0.7811,
    0.1641,
    0.4896,
    0.6680,
    0.9662,
    0.8574,
    0.6817,
    0.1158,
    0.9804,
    0.4198,
    0.4851,
    0.2688,
    0.4760,
    0.4761,
    0.4872,
    0.1100,
    0.7279,
    0.2262,
    0.9524,
    0.8251,
    0.0230,
    0.4878,
    0.3484,
    0.8185,
    0.9872,
    0.8522,
    0.2345,
    0.6355,
    0.8500,
    0.7830,
    0.5847,
    0.3545,
    0.8875,
    0.8190,
    0.4839,
    0.8531,
    0.6504,
    0.7990,
    0.6416,
    0.7571,
    0.6415,
    0.3290,
    0.5613,
    0.0375,
]


media = prueba_medias(nums)
varianza = prueba_varianza(nums, alpha)
uniformidad = prueba_uniformidad(nums, alpha)
