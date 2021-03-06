from flask import Flask
from lib.yolo_inference import yolo_infer2
from lib.emotic import Emotic
import numpy as np
from time import time
import cv2

app = Flask(__name__)

# setting up the categories
# our model outputs numbers as categories, so we much have a mapping from the numbers to the emotions
cat = ['Affection', 'Anger', 'Annoyance', 'Anticipation', 'Aversion', 'Confidence', 'Disapproval', 'Disconnection',
       'Disquietment', 'Doubt/Confusion', 'Embarrassment', 'Engagement', 'Esteem', 'Excitement', 'Fatigue', 'Fear',
       'Happiness', 'Pain', 'Peace', 'Pleasure', 'Sadness', 'Sensitivity', 'Suffering', 'Surprise', 'Sympathy',
       'Yearning']
cat2ind = {}
ind2cat = {}
for idx, emotion in enumerate(cat):
    cat2ind[emotion] = idx
    ind2cat[idx] = emotion

vad = ['Valence', 'Arousal', 'Dominance']
ind2vad = {}
for idx, continuous in enumerate(vad):
    ind2vad[idx] = continuous

# we need to normalise the demo image using the statistics of the training data the model was trained on
context_mean = [0.4690646, 0.4407227, 0.40508908]
context_std = [0.2514227, 0.24312855, 0.24266963]
body_mean = [0.43832874, 0.3964344, 0.3706214]
body_std = [0.24784276, 0.23621225, 0.2323653]
context_norm = [context_mean, context_std]
body_norm = [body_mean, body_std]

# start capture device
cap = cv2.VideoCapture(0)


@app.route('/api/v1/getEmotion', methods=['GET', 'POST'])
def get_emotion():

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip camera horizontally

    try:
        xs, _, _ = yolo_infer2(frame, 'experiment/results/',
                               'experiment/models/', context_norm, body_norm, ind2cat, ind2vad, write_op=False,
                               return_op=False)
        response = str(xs['bbox_0']['cat'][0]) + "~" + str(xs['bbox_0']['cont'][0])

    except:
        response = "Error"

    return response


if __name__ == '__main__':
    app.run()
