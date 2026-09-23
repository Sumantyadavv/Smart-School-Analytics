# V1 - Python Basics: Smart School Analytics Starter
# Author: Sumant Kumar Yadav

print("--- Welcome to Smart School Analytics ---")

# 1. Variables and Data Types
school_name = "Zenith Convent School"
total_students = 1200
passing_percentage = 85.5
is_grading_active = True

print(f"School Name: {school_name}")
print(f"Total Students: {total_students}")

# 2. Conditional Statement (if-elif-else)
if passing_percentage >= 80:
    print("Performance Status: Excellent Performance!")
elif passing_percentage >= 60:
    print("Performance Status: Good Performance.")
else:
    print("Performance Status: Needs Improvement.")

# 3. Simple Loop (for loop demo)
print("\nCounting active student batches:")
for batch in range(1, 4):
    print(f"Processing Batch {batch}...")

print("--- End of V1 Basics ---")