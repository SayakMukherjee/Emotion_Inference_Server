# Emotion Inference Server
This project is a part of the course CS4270: Conversational Agents at Delft University of Technology.

Detects users emotion based on captured frame. API calls are made to this server from the 
conversational agent MathTutor. The code for the MathTutor can be found <a href="https://github.com/paucanosa/MathTutor">here</a>.

# Dependencies

Make sure the following dependencies are installed. We recommened using a new conda environment.

- python=3.8
- pytorch <= 1.8.1
- scikit-learn
- numpy
- pandas
- matplotlib

## Links to EMOTIC dataset

This project uses the <a href="http://sunai.uoc.edu/emotic/download.html">EMOTIC dataset</a> and follows the methodology as introduced in the paper <a href="https://arxiv.org/pdf/2003.13401.pdf">'Context based emotion recognition using EMOTIC dataset'</a>.

To make it easier for you we have hosted the EMOTIC dataset as well, if you intend to make use of it.

**Link to data**: https://tud365.sharepoint.com/:f:/s/ConversationalAgents2021/EoSyoFarxCJFoZrfkgft3iQBnpRRPZNavJ6La5ZfRhrFXw?e=61LcKf

If you do not wish to train the model from scratch, section 12 will show you how you can use pretrained versions of the model along with a few examples

Pretrained model files located at <a href="https://tud365-my.sharepoint.com/:u:/g/personal/smukherjee1_tudelft_nl/Ee9KHDkV62JOhdG0kCQmV-0BJ1IEMlCa1FJGJAoPKZhekg?e=gMj2NE">OneDrive</a>.
# Implementation Details

## To run the inference server

1. Execute app.py
2. Server runs on localhost port 5000
3. API call http://127.0.0.1:5000/api/v1/getEmotion returns the emotion with the highest probabilty
4. In case the model fails it returns "Error"
