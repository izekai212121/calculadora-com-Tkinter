import tkinter as tk

# window principal gay
janela = tk.Tk()
janela.title("calculadora gay lgbtqiapn+")
janela.geometry("300x250")

# armazen lgbt de calculus matematicus
primeiro_numero = ""
operacao = ""
display_texto = ""

# numeros no display
def adicionar_numero(numero):
    global display_texto
    display_texto += numero
    entrada.delete(0, tk.END)
    entrada.insert(0, display_texto)

# operasao supreme gay
def definir_operacao(op):
    global primeiro_numero, operacao, display_texto
    if display_texto:
        primeiro_numero = display_texto
        operacao = op
        display_texto = ""
        entrada.delete(0, tk.END)

# funcao de calculara gayzisse
def calcular():
    global primeiro_numero, operacao, display_texto
    if primeiro_numero and operacao and display_texto:
        try:
            num1 = float(primeiro_numero)
            num2 = float(display_texto)
            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    entrada.delete(0, tk.END)
                    entrada.insert(0, "Erro: Divisão por 0")
                    return
                resultado = num1 / num2
            entrada.delete(0, tk.END)
            entrada.insert(0, str(resultado))
            display_texto = str(resultado)
            primeiro_numero = ""
            operacao = ""
        except ValueError:
            entrada.delete(0, tk.END)
            entrada.insert(0, "Erro")
            display_texto = ""

# limpar o display
def limpar():
    global primeiro_numero, operacao, display_texto
    primeiro_numero = ""
    operacao = ""
    display_texto = ""
    entrada.delete(0, tk.END)
    entrada.insert(0, "0")

# entry
entrada = tk.Entry(janela, width=20, font=("Arial", 16), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entrada.insert(0, "0")

# butoinhs
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for texto, linha, coluna in botoes:
    if texto == "C":
        botao = tk.Button(janela, text=texto, font=("Arial", 14), width=5, command=limpar)
    elif texto == "=":
        botao = tk.Button(janela, text=texto, font=("Arial", 14), width=5, command=calcular)
    elif texto in ["+", "-", "*", "/"]:
        botao = tk.Button(janela, text=texto, font=("Arial", 14), width=5, command=lambda op=texto: definir_operacao(op))
    else:
        botao = tk.Button(janela, text=texto, font=("Arial", 14), width=5, command=lambda num=texto: adicionar_numero(num))
    botao.grid(row=linha, column=coluna, padx=5, pady=5)

# loop
janela.mainloop()
