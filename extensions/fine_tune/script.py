import modules.shared
import gradio as gr

def ui():
    activate = gr.Checkbox(value=True, label='Activate character bias')