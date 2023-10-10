<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
</head>

<body>

<h1>Pencil Angle and Length Measurement using OpenCV</h1>

<p>This Python project uses OpenCV to measure the angle between two pencils in an image and also calculates their length in centimeters. The project provides a graphical user interface to select points on the pencils and computes the angle and length based on the selected points.</p>

<h2>Prerequisites</h2>

<p>Make sure you have the following libraries installed:</p>
<ul>
    <li>OpenCV</li>
    <li>NumPy</li>
    <li>Math (usually included in Python)</li>
</ul>

<p>You can install OpenCV and NumPy using pip:</p>
<pre>
pip install opencv-python-headless numpy
</pre>

<h2>Usage</h2>

<ol>
    <li>Run the script using a Python interpreter.</li>
    <li>Load an image containing two pencils by modifying the <code>path</code> variable in the code.</li>
    <li>Follow the on-screen instructions to select points on the pencils.</li>
    <li>The program will display the calculated angle and length in centimeters for each pencil.</li>
    <li>Press 'q' to exit the application.</li>
</ol>

<h2>How it Works</h2>

<ul>
    <li>The code uses mouse clicks to select points on the pencils.</li>
    <li>It calculates the distance between points to determine the length of each pencil in centimeters.</li>
    <li>Using trigonometry, it computes the angle between the two pencils based on the selected points.</li>
</ul>

<h2>Contributing</h2>

<p>Feel free to contribute to this project by submitting issues or pull requests.</p>



<h2>Acknowledgments</h2>

<ul>
    <li>Special thanks to the OpenCV community for their excellent library.</li>
    <li>Inspired by computer vision and image processing techniques.</li>
</ul>

<p>Happy measuring!</p>

</body>

</html>
