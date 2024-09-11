import streamlit as st
import datetime 
import contrato


def main():
    st.title("Sistema de CRM e Vendas")

    email = st.text_input('Campo de texto para inserção do e-mail do vendendor:')
    data = st.date_input("Data da compra: ",format="DD/MM/YYYY")
    hora = st.time_input("Campo para selecionar a hora da venda: ",datetime.datetime.now())
    valor_venda = st.number_input("Campo para o valor da venda: ",min_value=0.0, format="%.2f")
    qtd_produto = st.number_input("quantidade de vendas: ",min_value=1,step=1)
    produto = st.selectbox("Seleção de produto vendido",["banana","laranja","Manga"])

    if st.button("Salvar"):
        data_hora = datetime.datetime.combine(data,hora)
        print(email,data)






if __name__ == "__main__":
    main()