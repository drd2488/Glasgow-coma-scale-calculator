# Define the GCS score calculation function
def calculate_gcs(eye_opening, verbal_response, motor_response):
    # Calculate the GCS score by adding the values
    gcs_score = eye_opening + verbal_response + motor_response
    return gcs_score


# Map the eye-opening scores to the corresponding GCS score values
eye_opening_scores = {
    "Spontaneous eye opening": 4,
    "Eye opening in response to speech": 3,
    "Eye opening in response to pain": 2,
    "No eye opening": 1
}

# Map the verbal response scores to the corresponding GCS score values
verbal_response_scores = {
    "Oriented": 5,
    "Confused conversation": 4,
    "Inappropriate speech": 3,
    "Incomprehensible speech": 2,
    "No verbal response": 1
}

# Map the motor response scores to the corresponding GCS score values
motor_response_scores = {
    "Carrying out request ('obeying command')": 6,
    "Localising response to pain": 5,
    "Withdrawal to pain": 4,
    "Flexor response to pain": 3,
    "Extensor posturing to pain": 2,
    "No response to pain": 1
}
# Intro
print("Welcome to the glasgow coma scale calculator. Make a selection")
# Print the available options for the eye-opening score
print("Choose the option for the eye opening score:")
print("1. Spontaneous eye opening")
print("2. Eye opening in response to speech")
print("3. Eye opening in response to pain")
print("4. No eye opening")

# Prompt the user for the eye-opening score
eye_opening = int(input("Enter the option number: "))

# Get the corresponding eye-opening score description
eye_opening_description = list(eye_opening_scores.keys())[eye_opening - 1]

# Get the GCS score value for the eye-opening score
eye_opening_value = eye_opening_scores[eye_opening_description]

# Print the available options for the verbal response score
print("\nChoose the option for the verbal response score:")
print("1. Oriented")
print("2. Confused conversation")
print("3. Inappropriate speech")
print("4. Incomprehensible speech")
print("5. No verbal response")

# Prompt the user for the verbal response score
verbal_response = int(input("Enter the option number: "))

# Get the corresponding verbal response score description
verbal_response_description = list(verbal_response_scores.keys())[verbal_response - 1]

# Get the GCS score value for the verbal response score
verbal_response_value = verbal_response_scores[verbal_response_description]

# Print the available options for the motor response score
print("\nChoose the option for the motor response score:")
print("1. Carrying out request ('obeying command')")
print("2. Localising response to pain")
print("3. Withdrawal to pain - pulls limb away from painful stimulus")
print("4. Flexor response to pain - pressure on nail bed causes abnormal flexion of limbs - decorticate posture")
print("5. Extensor posturing to pain - stimulus causes limb extension - decerebrate posture")
print("6. No response to pain")

# Prompt the user for the motor response score
motor_response = int(input("Enter the option number: "))

# Get the corresponding motor response score description
motor_response_description = list(motor_response_scores.keys())[motor_response - 1]

# Get the GCS score value for the motor response score
motor_response_value = motor_response_scores[motor_response_description]

# Calculate the GCS score
gcs_score = calculate_gcs(eye_opening_value, verbal_response_value, motor_response_value)

# Print the GCS score
print(f"GCS score: {gcs_score}")

if gcs_score <= 8:
    print("Patient has severe injury")
elif gcs_score <= 12:
    print("Patient has moderate injury")
else:
    print("Patient has minor injury")
