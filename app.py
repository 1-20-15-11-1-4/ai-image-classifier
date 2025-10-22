import gradio as gr
from transformers import pipeline

# Load pre-trained image classifier
classifier = pipeline("image-classification", model="google/vit-base-patch16-224")

# Create the function
def classify_image(image):
    predictions = classifier(image)
    return {pred["label"]: pred["score"] for pred in predictions}

# Create web interface
demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=5),
    title="AI Image Classifier",
    description="Upload an image and AI will identify what it is!"
)

# Launch it
demo.launch()
