import gradio as gr

def predict(age, income):
    
    if income > 25000:
        return "Likely to Purchase"
    
    return "Not Likely to Purchase"

demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Age"),
        gr.Number(label="Monthly Income")
    ],
    outputs="text"
)

demo.launch()