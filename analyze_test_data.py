import pandas as pd
import ast

# Load the data file
df = pd.read_csv("grasping_participant_test.csv")

# Calculate reaction time and exploration time
df['reaction_time'] = df['grasp_signal'] - df['nav_start']
df['exploration_time'] = df['reaction_time']

# Calculate accuracy
df['accuracy'] = df['key_pressed'].apply(lambda x: 1 if str(x).lower() == 'y' else 0)

# Define smoothness calculation function
def compute_smoothness(detection_str):
    detections = ast.literal_eval(detection_str)
    changes = sum(1 for i in range(1, len(detections)) if detections[i] != detections[i-1])
    return 1 / (1 + changes)

# Apply smoothness calculation
df['smoothness'] = df['target_detections'].apply(compute_smoothness)

# Save the analysis results
df[['target_label', 'reaction_time', 'exploration_time', 'accuracy', 'smoothness']].to_csv("processed_test.csv", index=False)

print("✅ Data successfully processed. Results saved to 'processed_test.csv'.")

