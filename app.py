# import
import os
import streamlit as st
import streamlit-chat

if "page" not in st.session_state:
    st.session_state.page = "home"

# ページ切り替え関数
def go_to(page_name):
    st.session_state.page = page_name

def home():
    st.title("ホームページ")
    if st.button("設定ページへ"):
        go_to("settings")
    return 

def setting_prompt():
    st.title("設定ページ")
    if st.button("ホームへ戻る"):
        go_to("home")

def main():
    st.title("ホームページ")
    if st.button("設定ページへ"):
        go_to("settings")
    return 








st.markdown('# 画像を保存するデモ')
    file = st.file_uploader('画像をアップロードしてください.', type=['jpg', 'jpeg', 'png'])
    if file:
        st.markdown(f'{file.name} をアップロードしました.')
        img_path = os.path.join(IMG_PATH, file.name)
        # 画像を保存する
        with open(img_path, 'wb') as f:
            f.write(file.read())
            
        # 保存した画像を表示
        img = Image.open(img_path)
        st.image(img)

if __name__ == '__main__':
    main()
