
# Para gerar o executavel do app:
# pip install pyinstaller
# pip install pillow
# flet pack nome_arquivo.py --icon nome_icone.png

import flet as ft

def main(page: ft.Page):
    def calcular(e):
         # Cálculo do imc
        try:
            peso_valor = float(peso.value)
            altura_valor = float(altura.value)
            imc = peso_valor / (altura_valor ** 2)
            result.value = f"IMC de {nome.value} é: {imc:.2f}, portanto " + interpretar_imc(imc)
        except:
            result.value = "Por favor, insira valores válidos."
        page.update()
        
    def interpretar_imc(imc):
        if imc < 18.5:
            return "abaixo do peso."
        elif 18.5 <= imc < 24.9:
            return "peso normal."
        elif 25 <= imc < 29.9:
            return "sobrepeso."
        else:
            return "obesidade."
        
    def pular_peso(e):
            peso.focus()

    def pular_altura(e):
            altura.focus()
            
    page.update()
        
    page.title = 'IMC'
    page.scroll = 'adaptive'
    page.theme_mode = ft.ThemeMode.DARK
     
     # entrada de dados
    nome = ft.TextField(label='Nome', on_submit=pular_peso)
    peso = ft.TextField(label='Peso', suffix_text='kg', on_submit=pular_altura)
    altura = ft.TextField(label='Altura', suffix_text='metros', on_submit=calcular)
    btn = ft.ElevatedButton("Calcular IMC", on_click=calcular)
    result = ft.Text(size=30)
     
    page.add(
        ft.Row(
            [ft.Text('Calculadora IMC', size=35, weight='bold', color='purple')],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [nome],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [altura],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [peso],
            alignment=ft.MainAxisAlignment.CENTER
        ),
         ft.Row(
            [ft.ElevatedButton('Calcular IMC')],
            alignment=ft.MainAxisAlignment.CENTER
        ),
         ft.Row(
            [btn],
            alignment=ft.MainAxisAlignment.CENTER
        ),
         ft.Row(
            [result],
            alignment=ft.MainAxisAlignment.CENTER
        )
     )
        
        
           
    page.update()
    
ft.app(main)