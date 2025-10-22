# AI Image Classifier

AI-powered image classification tool using Google's Vision Transformer (ViT). Upload any image and get instant predictions with confidence scores.

## 🚀 [Try it Live!](https://huggingface.co/spaces/dakota-stpierre/github-image_classifier)


## 🛠️ Tech Stack
- **Model:** Google ViT (Vision Transformer)
- **Framework:** Transformers by Hugging Face
- **Interface:** Gradio
- **Deployment:** Hugging Face Spaces

## 📊 Features
- Classifies images into 1000+ categories
- Returns top 5 predictions with confidence scores
- Real-time processing in the cloud
- No installation required - runs in browser

## 🧠 How It Works
Uses a pre-trained Vision Transformer model trained on ImageNet (1.2 million images):
1. Splits uploaded images into patches
2. Processes through transformer attention layers
3. Predicts object categories with confidence scores

## 💻 Run Locally
```bash
pip install -r requirements.txt
python app.py
```

## 📝 What I Learned
- Loading and deploying pre-trained ML models
- Creating web interfaces for AI applications
- Understanding transformer architectures
- Full ML deployment pipeline from training to production

Built as part of my machine learning portfolio.
