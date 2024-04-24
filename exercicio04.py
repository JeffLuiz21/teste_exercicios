import time

lampadas = [False, False, False] 

def verificar_lampadas():
    for i, lampada in enumerate(lampadas):
        if lampada:
            print(f"Lâmpada {i+1} está acesa.")
        else:
            print(f"Lâmpada {i+1} está apagada.")

lampadas[0] = True
print("Primeiro interruptor ligado.")
verificar_lampadas()

time.sleep(2)

lampadas[0] = False
lampadas[1] = True
print("\nPrimeiro interruptor desligado e segundo interruptor ligado.")
verificar_lampadas()

time.sleep(2)

print("\nVamos entrar na sala para verificar o estado das lâmpadas.")
print("Se uma lâmpada estiver acesa, então o segundo interruptor controla essa lâmpada.")
print("Se uma lâmpada estiver apagada e ainda estiver fria ao toque, então o terceiro interruptor controla essa lâmpada.")
print("Se uma lâmpada estiver apagada, mas estiver quente ao toque, então o primeiro interruptor controla essa lâmpada.")
