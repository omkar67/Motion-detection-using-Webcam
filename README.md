# Motion Detection System Using OpenCV and Bokeh

## Overview
This project uses Python and the OpenCV library to detect motion through a webcam feed. It captures video, processes it to detect motion, and logs the times when motion is detected. The motion detection events are then visualized as a histogram using the Bokeh library.

## Features
1. **Initialize Webcam and Capture Video Feed**
    - Uses the OpenCV library to access and initialize the webcam.
    - Continuously captures the video feed from the webcam.

2. **Convert Video Feed to Black and White and Apply Foreground Subtraction**
    - Converts the captured video frames to grayscale to simplify processing.
    - Applies foreground subtraction to highlight moving objects by differentiating the foreground from the static background.

3. **Reduce Noise and Detect Contours**
    - Reduces noise in the video feed to avoid false positives in motion detection using techniques like Gaussian blur.
    - Checks the processed video frames for contours (outlines of detected objects).
    - Creates borders around these contours to visually mark detected motion areas.

4. **Record Timestamps of Motion Events**
    - Records a timestamp whenever motion is detected.
    - Stores these timestamps in a pandas DataFrame for structured logging of motion events.

5. **Plot Motion Detection Events Using Bokeh**
    - Uses the recorded timestamps to create a histogram.
    - Plots the histogram using the Bokeh library to visually represent the times when motion was detected, allowing for easy analysis of motion patterns.

## Requirements
- Python 3.x
- OpenCV
- Pandas
- Bokeh
