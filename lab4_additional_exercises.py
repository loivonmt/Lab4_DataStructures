from collections import defaultdict, Counter

# Initialize variables
SEED_NUM = 8
STUDENT_MAJOR = "BSME"
CONTROL_NUM = max(3, SEED_NUM) # 8

# Initial stream
stream = [
    ("TUP Manila", "BSECE"),
    ("TUP Taguig", f"BSME_v{CONTROL_NUM}"),
    ("TUP Manila", f"BSME_v{CONTROL_NUM}"),
    ("TUP Manila", "BSECE"),
    ("TUP Visayas", STUDENT_MAJOR),
    ("TUP Taguig", "BSECE"),
    ("TUP Manila", "BSECE")
]

# Data Expansion: Add exactly CONTROL_NUM + 3 (11) custom tuples
custom_data = [("TUP Manila", "BSME") for _ in range(11)]
stream.extend(custom_data)

# Algorithm Phase 1: Aggregation
campus_map = defaultdict(list)
for campus, program in stream:
    campus_map[campus].append(program)

# Algorithm Phase 2: Frequency Analysis
manila_counts = Counter(campus_map["TUP Manila"])
top_program, frequency = manila_counts.most_common(1)[0]

# Outputs for Assessment Table
print(f"CONTROL_NUM Used: {CONTROL_NUM}")
print(f"STUDENT_MAJOR Used: {STUDENT_MAJOR}")
print(f"Expanded Stream Length: {len(stream)}")
print(f"Total Applications for TUP Manila: {len(campus_map['TUP Manila'])}")
print(f"Top Requested Program at TUP Manila: {top_program}")
print(f"Exact Frequency of Top Program: {frequency}")

# Variables
FAVORITE_ARTIST = "BINI"
CONTROL_NUM = 8

# Initialize Sets
festival = {"Ben&Ben", "SB19", "Bini", "Eraserheads", FAVORITE_ARTIST, "Zild", f"Indie Artist {CONTROL_NUM}"}
user_a = {"Ben&Ben", "Bini", "Maki", "Dionela", FAVORITE_ARTIST}
user_b = {"SB19", "Eraserheads", "Zild", f"Indie Artist {CONTROL_NUM}", "Parokya ni Edgar"}

# Data Expansion: Add exactly CONTROL_NUM (8) new artists
new_artists = {f"Artist_{i}" for i in range(CONTROL_NUM)}
festival.update(new_artists)

# Algorithm: Jaccard Similarity J(A, B) = |A ∩ B| / |A ∪ B|
def calculate_jaccard(user_set, fest_set):
    intersection = user_set.intersection(fest_set)
    union = user_set.union(fest_set)
    return (len(intersection) / len(union)) * 100, len(intersection), len(union)

sim_a, inter_a, union_a = calculate_jaccard(user_a, festival)
sim_b, _, _ = calculate_jaccard(user_b, festival)

# Set Difference for Dealbreakers (In User A but NOT in Festival)
dealbreakers = user_a.difference(festival)

# Outputs for Assessment Table
print(f"Total Artists in Expanded Festival: {len(festival)}")
print(f"Length of Intersection (User A & Festival): {inter_a}")
print(f"Length of Union (User A & Festival): {union_a}")
print(f"User A Jaccard Similarity: {sim_a:.2f}%")
print(f"User B Jaccard Similarity: {sim_b:.2f}%")
print(f"User A Dealbreaker Artists: {dealbreakers}")

from collections import deque, Counter

CONTROL_NUM = 8
LOCAL_HAZARD = "FLOOD"

# Initialize deque with maxlen 5
buffer = deque(maxlen=5)

# Initial burst
burst = [
    (CONTROL_NUM, "WEATHER"),
    (CONTROL_NUM + 1, "TRAFFIC"),
    (CONTROL_NUM + 2, "WEATHER"),
    (CONTROL_NUM + 3, "WEATHER"),
    (CONTROL_NUM + 4, LOCAL_HAZARD),
    (CONTROL_NUM + 5, "WEATHER"),
    (CONTROL_NUM + 6, "TRAFFIC")
]

# Data Expansion: Add CONTROL_NUM + 2 (10) custom alerts
for i in range(7, 17):
    burst.append((CONTROL_NUM + i, "SYSTEM"))

# Algorithm: Sliding Window
for timestamp, category in burst:
    # Use list comprehension to get categories currently in deque
    current_categories = [item[1] for item in buffer]
    counts = Counter(current_categories)
    
    # Spam Rule: Reject if category already exists 2 or more times
    if counts[category] < 2:
        buffer.append((timestamp, category))

# Outputs for Assessment Table
final_timestamps = [item[0] for item in buffer]

print(f"LOCAL_HAZARD Used: {LOCAL_HAZARD}")
print(f"Total Burst Size: {len(burst)}")
print(f"Final Deque Length: {len(buffer)}")
print(f"Final Sum of Timestamps in Deque: {sum(final_timestamps)}")
print(f"Exact Final Deque Output: {list(buffer)}")