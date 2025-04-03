import gradio as gr

def chatbot(input_text):
    return f"Chatbot response to: {input_text}"

interface = gr.Interface(fn=chatbot, inputs="text", outputs="text")

interface.launch()
