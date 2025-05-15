# 🖌️ Generative AI Sketch Service

A serverless Generative AI service that leverages **Amazon Bedrock**, **AWS Lambda**, **Amazon S3**, **IAM Policies**, and **Stability-AI** to generate images from text prompts via a simple RESTful API.

## ✨ Overview

This project enables users to generate AI-powered sketches based on their text input (prompt). The generated image is stored securely in S3 using a pre-signed URL and is accessible through a public API endpoint.
Visit the live API by replacing your prompt at the end of this URL:

* 🔗 Live Endpoint:
  [`https://dsb2zwz7pk.execute-api.us-east-1.amazonaws.com/dev/ai/sketch?prompt=WHAT_YOU_WANT_TO_SKETCH_TODAY`](https://dsb2zwz7pk.execute-api.us-east-1.amazonaws.com/dev/ai/sketch?prompt=WHAT_YOU_WANT_TO_SKETCH_TODAY)

✅ The image will be rendered in your browser.

## 🧪 Example Prompts

* *A robot sketching on paper*
* *An astronaut riding a horse in space*

### 🚀 How It Works

1. **User** sends a `prompt` to the REST API endpoint.
2. **API Gateway** triggers an **AWS Lambda** function.
3. Lambda:

   * Sends the prompt to **Amazon Bedrock (Stability-AI)** for image generation.
   * Stores the image using a **pre-signed S3 URL**.
   * Returns the image directly as part of the **HTTP response**, which the browser renders inline.
4. The user **sees the generated image immediately** in the browser.

## 🧰 Tech Stack

* **Amazon Bedrock** – for scalable foundation model orchestration
* **Stability-AI (via Bedrock)** – image generation from prompt
* **AWS Lambda** – serverless backend logic
* **Amazon S3** – image storage using pre-signed URLs
* **IAM Roles and Policies** – secure service-to-service access control
* **API Gateway** – exposes RESTful endpoint

## 🚀 Features

* ✅ Generate images via text prompts
* ✅ Secure image storage in S3
* ✅ Pre-signed URLs for direct and secure upload
* ✅ Stateless RESTful API with Lambda-backed logic
* ✅ Seamless integration with Bedrock & Stability-AI

## 🔐 IAM & Security

* **Lambda Execution Role:** Allows invoking Bedrock and uploading to S3.
* **S3 Bucket Policy:** Grants `PutObject` permission only via pre-signed URL.
* **Least Privilege:** IAM roles follow best practices for secure access.



