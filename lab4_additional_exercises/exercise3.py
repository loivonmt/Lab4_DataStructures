# ==========================================
# GLOBAL INPUTS
# ==========================================
SEED_NUM = 8
STUDENT_MAJOR = "BSME"
FAVORITE_ARTIST = "BINI"
LOCAL_HAZARD = "TYPHOON"  # Example local hazard in UPPERCASE

# Numeric computation control variable
CONTROL_NUM = max(3, SEED_NUM)

print(f"CONTROL_NUM initialized to: {CONTROL_NUM}")

# Exercise 3: Stateful Sliding Window Filter
from collections import deque, Counter

# Initialize tracking flags for the assessment table
weather_append_status = "N/A"
hazard_append_status = "N/A"

# Initialize deque with max length of 5
buffer = deque(maxlen=5)

# Base burst stream
burst = [
    (CONTROL_NUM, "WEATHER"), 
    (CONTROL_NUM + 1, "TRAFFIC"), 
    (CONTROL_NUM + 2, "WEATHER"), 
    (CONTROL_NUM + 3, "WEATHER"), 
    (CONTROL_NUM + 4, LOCAL_HAZARD), 
    (CONTROL_NUM + 5, "WEATHER"), 
    (CONTROL_NUM + 6, "TRAFFIC")
]

# 1. Data Expansion: Append exactly (CONTROL_NUM + 2) custom alerts with sequential timestamps
start_ts = CONTROL_NUM + 7
for i in range(CONTROL_NUM + 2):
    # Alternating custom alerts for demonstration
    category = "TRAFFIC" if i % 2 == 0 else "AMBULANCE"
    burst.append((start_ts + i, category))

# 2. Algorithm (The Sliding Window Filter)
for timestamp, category in burst:
    # Extract current categories in the deque buffer
    current_categories = [item[1] for item in buffer]
    counts = Counter(current_categories)
    
    # Check the Spam Rule constraint
    if counts[category] >= 2:
        # Check specific tracking milestones required by the assessment sheet
        if timestamp == CONTROL_NUM + 3 and category == "WEATHER":
            weather_append_status = "N"
        if category == LOCAL_HAZARD and hazard_append_status == "N/A":
            hazard_append_status = "N"
        continue  # Reject alert
    else:
        buffer.append((timestamp, category))
        # Check specific tracking milestones required by the assessment sheet
        if timestamp == CONTROL_NUM + 3 and category == "WEATHER":
            weather_append_status = "Y"
        if category == LOCAL_HAZARD and hazard_append_status == "N/A":
            hazard_append_status = "Y"

# Calculate final outputs
final_sum_timestamps = sum(item[0] for item in buffer)

# Output Assessment Data
print("="*40)
print("EXERCISE 3 ASSESSMENT DATA")
print("="*40)
print(f"LOCAL_HAZARD Used: {LOCAL_HAZARD}")
print(f"Total Burst Size (After adding custom alerts): {len(burst)}")
print(f"Did 'WEATHER' at Timestamp CONTROL_NUM + 3 append? (Y/N): {weather_append_status}")
print(f"Did LOCAL_HAZARD append? (Y/N): {hazard_append_status}")
print(f"Final Deque Length: {len(buffer)}")
print(f"Final Sum of Timestamps in Deque: {final_sum_timestamps}")
print(f"Exact Final Deque Output: {list(buffer)}")