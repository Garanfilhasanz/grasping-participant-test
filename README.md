# Grasping Participant Test

This repository contains Python scripts and example data for analyzing tactile-guided grasping experiments. The main goal is to measure motor control performance differences between the dominant and non-dominant hand.

## Files

 `analyze_test_data.py`: Main script to compute reaction time, exploration time, grasping accuracy, and smoothness.
 `grasping_participant_test.csv`: Example raw data file.
 `processed_test.csv`: Output file with all computed features.

## How to Use

1. Run `analyze_test_data.py` in the same folder as your input data.
2. The script will output `processed_test.csv` with calculated metrics.

## Output Metrics

*Reaction Time*: Time from vibration onset to movement initiation.
*Exploration Time*: Same as reaction time (approximation due to setup limits).
*Grasping Accuracy*: Based on keypresses (`y` for correct, `n` for incorrect).
*Smoothness Score*: Based on changes in vibration motor patterns.

## Research Context

This project is part of a broader study on tactile guidance systems for blind individuals, focusing on sensorimotor control and the role of hand dominance.

## Author

Garanfil Hasanzade  
Email: garanfil.hasanzade@yandex.com  
GitHub: [Garanfilhasanz](https://github.com/Garanfilhasanz)
