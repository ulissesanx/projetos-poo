import streamlit as st
import time
from datetime import date

st.set_page_config(page_title="Feliz Mesversário! ❤️", page_icon="❤️", layout="centered")


st.title("🎉 Feliz Mesversário, meu amor! ❤️")

data_inicio = date(2025, 1, 13)
hoje = date.today()

meses = 6

st.subheader(f"Estamos juntos há **{meses} meses** 🥰")

if st.button("💌 Abrir mensagem especial"):
    mensagem = st.empty()
    coracoes = st.empty()
    
    texto = "Como você me disse uma vez\n\n"
    texto += '"É fácil demais te amar!"\n\n'
    texto += "E eu escolho, escolho estar sempre do seu lado 💕\n\n"
    texto += "Porque? Porque é fácil demais te amar ❤️\n\n"
    texto += "É gostoso demais\n\n"
    texto += "É lindo demais!❤️\n\n"
    texto += "Você me faz perceber, que TALVEZ, tudo isso valha a pena.\n\n"

    for linha in texto.split("\n"):
        mensagem.title(linha)
        time.sleep(1.25)
    
    for _ in range(5):
        coracoes.markdown("<h1 style='text-align: center;'>❤️💖💝💘💕</h1>", unsafe_allow_html=True)
        time.sleep(0.5)
        coracoes.markdown("<h1 style='text-align: center;'>💘💝💖💕❤️</h1>", unsafe_allow_html=True)
        time.sleep(0.5)
    
    st.balloons()

    st.markdown("---")
    st.subheader("🖼️ Nosso Photodump Especial 🖼️")

    placeholder_foto = st.empty()

    for i in range(1, 14):  # De 1 a 13
        placeholder_foto.image(f"{i}.jpeg", use_container_width=True)
        time.sleep(1.5)  # Tempo que cada foto fica visível

    st.success("✨ Essas são só algumas das nossas melhores memórias... Que venham muitas outras! ✨")
    st.title('Que venham muitos outros meses!')
    st.title('Muitas outras histórias')
    st.title('Muitos outros conflitos..')

    st.title('PORQUE COM VOCÊ!!!...')

    st.button('❤️')

    time.sleep(2)    
    st.title('Tudo isso vale a pena! 💕')