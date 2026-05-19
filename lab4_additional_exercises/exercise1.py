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

# Exercise 1: Unstructured Data Aggregator
from collections import defaultdict, Counter

# Initialize the base stream
stream = [
    ("TUP Manila", "BSECE"),
    ("TUP Taguig", f"BSME_v{CONTROL_NUM}"), 
    ("TUP Manila", f"BSME_v{CONTROL_NUM}"), 
    ("TUP Manila", "BSECE"),
    ("TUP Visayas", STUDENT_MAJOR), 
    ("TUP Taguig", "BSECE"),
    ("TUP Manila", "BSECE")
]

# 1. Data Expansion: Add exactly (CONTROL_NUM + 3) custom tuples
# For CONTROL_NUM = 8, we add 8 + 3 = 11 custom tuples
custom_tuples = [
    ("TUP Manila", "BSIT"),
    ("TUP Taguig", "BSIT"),
    ("TUP Visayas", "BSIT"),
    ("TUP Manila", "BSME"),
    ("TUP Manila", "BSECE"),
    ("TUP Taguig", "BSME"),
    ("TUP Manila", "BSIT"),
    ("TUP Manila", "BSECE"),
    ("TUP Visayas", "BSECE"),
    ("TUP Manila", "BSME"),
    ("TUP Taguig", "BSECE")
]

# Ensure we dynamically slice exactly the required amount
stream.extend(custom_tuples[:CONTROL_NUM + 3])

# Phase 1: Aggregation
campus_logs = defaultdict(list)
for campus, degree in stream:
    campus_logs[campus].append(degree)

# Phase 2: Frequency Analysis
counters = {}
for campus, degrees in campus_logs.items():
    counters[campus] = Counter(degrees)

# Extract top requested program at Manila
manila_top = counters["TUP Manila"].most_common(1)[0]

# Output Assessment Data
print("="*40)
print("EXERCISE 1 ASSESSMENT DATA")
print("="*40)
print(f"CONTROL_NUM Used: {CONTROL_NUM}")
print(f"STUDENT_MAJOR Used: {STUDENT_MAJOR}")
print(f"Expanded Stream Length: {len(stream)}")
print(f"Total Applications Processed for TUP Manila: {len(campus_logs['TUP Manila'])}")
print(f"Top Requested Program at TUP Manila: {manila_top[0]}")
print(f"Exact Frequency of Top Program: {manila_top[1]}")