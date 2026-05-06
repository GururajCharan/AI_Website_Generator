import streamlit as st
import dotenv
import langchain
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
import zipfile
from dotenv import load_dotenv
load_dotenv()
import os
os.environ["GOOGLE_API_KEY"]=os.getenv("gemini")



st.set_page_config(page_title="AI Website Creation", page_icon="🧠")

st.title("AI AUTOMATION WEBSITE CREATION")

prompt=st.text_area("write here about your website")


if st.button("generate"):
    message = [("system", """You are an expert web developer.

Create a complete, modern website in a SINGLE HTML file.

STRICT RULES:
- Use HTML, CSS, and JavaScript
- Embed CSS inside <style> tag
- Embed JS inside <script> tag
- DO NOT include explanations
- Output ONLY valid HTML code

The website should be clean, responsive, and professional.
""")]

    message.append(("user", prompt))

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

    try:
        response = model.invoke(message)
        html_content = response.content.strip()
    except Exception as e:
        st.error(f"Error: {e}")
        st.stop()

    html_content = html_content.replace("```html", "").replace("```", "")

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    import zipfile
    with zipfile.ZipFile("website.zip", "w") as zipf:
        zipf.write("index.html")

    with open("website.zip", "rb") as f:
        st.download_button("Download Website", f, "website.zip")

    st.subheader("Preview")
    st.components.v1.html(html_content, height=600, scrolling=True)

    st.success("Website generated successfully!")