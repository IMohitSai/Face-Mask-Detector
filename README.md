Face Mask Detection with Real-Time Air Quality and Access Control System
Description:

This project focuses on developing an AI-based system for face mask detection, leveraging the power of IBM Watson Visual Recognition and OpenCV. It aims to enhance safety in public and private spaces by detecting if individuals are wearing face masks, particularly in environments where mask usage is essential (e.g., hospitals, offices, schools).

In addition to mask detection, the system integrates real-time air quality monitoring and provides recommendations based on air pollution levels, ensuring that individuals are wearing appropriate protection in hazardous conditions. The system also features an access control mechanism, allowing entry only if the user is detected wearing a mask.

Key Features:

Real-time Face Mask Detection:
The system uses a camera to capture live video and detects whether a face mask is worn using a pre-trained IBM Watson model.
It provides visual feedback on the status of the detection (e.g., green for mask detected, red for no mask).
Air Quality Monitoring and Mask Recommendation:
Real-time data from an MQ-135 sensor is used to assess the pollution levels in the surrounding environment.
If the air quality is poor, the system recommends N95 masks instead of regular cloth masks.
Access Control (Only Masked Entry):
The system integrates with a door lock mechanism (via Raspberry Pi/Arduino) to allow or deny access based on mask detection.
Access is granted only if the person is properly wearing a mask.
Alert System:
If no mask is detected, a visual alert is shown, and the system will deny access until a mask is worn correctly.
User-Friendly Interface:
A simple interface that displays the mask detection status and air quality levels in real time.
Additional logging and notifications can be added to monitor system activity and mask-wearing trends.
Some Features mentioned are still work in progress.
