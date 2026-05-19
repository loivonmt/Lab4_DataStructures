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

# Exercise 2: Jaccard Similarity Engine

# Initialize base Sets
festival = {"Ben&Ben", "SB19", "Bini", "Eraserheads", FAVORITE_ARTIST, "Zild", f"Indie Artist {CONTROL_NUM}"}
user_a = {"Ben&Ben", "Bini", "Maki", "Dionela", FAVORITE_ARTIST} 
user_b = {"SB19", "Eraserheads", "Zild", f"Indie Artist {CONTROL_NUM}", "Parokya ni Edgar"}

# 1. Data Expansion: Add exactly CONTROL_NUM (8) new artists
custom_artists = {f"Custom Artist {i}" for i in range(1, CONTROL_NUM + 1)}
festival.update(custom_artists)

# 2. Algorithm: Jaccard Similarity calculations
# User A Calculation
intersection_a = user_a.intersection(festival)
union_a = user_a.union(festival)
jaccard_a = (len(intersection_a) / len(union_a)) * 100

# User B Calculation
intersection_b = user_b.intersection(festival)
union_b = user_b.union(festival)
jaccard_b = (len(intersection_b) / len(union_b)) * 100

# User A Dealbreakers (In user_a but NOT in festival)
dealbreakers_a = user_a.difference(festival)

# Output Assessment Data
print("="*40)
print("EXERCISE 2 ASSESSMENT DATA")
print("="*40)
print(f"Total Artists in Expanded Festival: {len(festival)}")
print(f"Length of Intersection (User A & Festival): {len(intersection_a)}")
print(f"Length of Union (User A & Festival): {len(union_a)}")
print(f"User A Jaccard Similarity: {jaccard_a:.2f}%")
print(f"User B Jaccard Similarity: {jaccard_b:.2f}%")
print(f"User A Dealbreaker Artists (Set Output): {dealbreakers_a}")