def par_ou_impar(num):
    if num % 2 == 0:
        return "par"
    return "ímpar"

num = 100
resposta = par_ou_impar(num)

print(f"O número {num} é {resposta}")