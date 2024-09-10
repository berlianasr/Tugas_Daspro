# Iuser input
desired_grade = input("Enter desired grade: ")
minimum_average_required = float(input("Enter minimum average required: "))
current_average = float(input("Enter current average in course: "))
final_weight_percentage = float(input("Enter how much the final counts as a percentage of the course grade: "))

# Convert percentage to a fraction
final_weight = final_weight_percentage / 100

# Calculate the score needed on the final exam
final_score_needed = (minimum_average_required - current_average * (1 - final_weight)) / final_weight

# Output the result
print(f"You need at least a score of {final_score_needed:.2f} on the final to get a {desired_grade}.")
