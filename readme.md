PowerPoint Generator Using Gemini AI

# Overview

This is a Python-based PowerPoint presentation generator that leverages AI (via Gemini AI- gemma-3-27b-it) to create dynamic, data-driven presentations. The tool allows users to input a topic, specify the number of slides, and receive a fully automated PowerPoint presentation. The generated slides include a mix of text-based content and relevant images. It’s designed to assist with content generation and save time for anyone who regularly creates presentations.

you can find a sample generated ppt here: /health_presentation.pptx

# Features

1. Automated Slide Generation: Generate presentations based on any topic with just a few inputs.
2. AI-Generated Content: Leverages the Gemini AI to automatically create slide outlines and content.
3. Image Integration: Automatically pulls relevant images based on the content and includes them in the slides.
4. Customizable Output parameters: Choose the number of slides and the file name for the generated PowerPoint.
5. Interactive User Input: Users specify the topic, number of slides, and output file name when running the program.

# Technologies Used

Python: The primary programming language used to build the project.
Gemini AI: Used to generate the content outline and image descriptions.
python-pptx: The library responsible for creating and modifying PowerPoint (.pptx) files.
Requests: For downloading images related to the content from the web.

# Installation

## 1. Requirements

Before running the project, ensure that Python is installed on your machine. You will also need to generate api keys for gemini api and pexel
Get your gemini API key from: https://makersuite.google.com/app/apikey
Get your gemini pexel key from: https://www.pexels.com/api/key

## 2. Steps to Set Up

### 2.a. Clone the repository to your local machine, Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate # For Windows
source .venv/bin/activate # For macOS/Linux

### 2.b. Install the required dependencies:

pip install -r requirements.txt

### 2.c. setup api keys as environment variables for gemini and pexel

Follow the setup instructions provided by the Gemini API to obtain an API key and pexel. Accordingly setup the 2 environment variables : 'GEMINI_API_KEY' and 'PEXEL_API_KEY'

# Usage

## To generate a presentation, run the following command:

python main.py

## The program will prompt you to enter the following:

Topic: The subject of the presentation (e.g., "Sunlight and Health - Recent Discoveries").

Number of Slides: How many slides you want in the presentation.

Output File Name: (Optional) Specify the output file name (default is generated_presentation.pptx).

After input, the program will generate the PowerPoint presentation and save it to the specified location.

Example
Enter the topic for the presentation: Sunlight and Health - Recent Discoveries
Enter the number of slides: 6
Enter the output file name (default is 'generated_presentation.pptx'): health_presentation.pptx
PPT Generator initialized successfully!
Generating presentation on: Sunlight and Health - Recent Discoveries
Creating slide 1: Sunlight & Health: Beyond Vitamin D - Recent Discoveries
Creating slide 2: Nitric Oxide & Cardiovascular Health
...
Presentation saved as: health_presentation.pptx

