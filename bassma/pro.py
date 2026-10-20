codigoHtto = int(input())
if codigoHtto == 400:
    mensajeError = "Bad Request"

elif codigoHtto == 400 :
    mensajeError = "Not found"
elif codigoHtto == 401 or codigoHtto == 403 or codigoHtto == 407:
    mensajeError = "Not allowed"
else:
    mensajeError = "somethingwentwrong"
print(mensajeError)
