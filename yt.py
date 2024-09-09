import re
import pandas as pd
import random
import streamlit as st

# Load dataset from Excel file
def load_dataset(file_path):
    df = pd.read_excel(file_path)
    return df

# Load the dataset from the correct file
procurement_data = load_dataset(r'C:\Users\USER\Desktop\aiassignment\chatbot_dataset.xlsx')

# Function to find the best match from the dataset with priority handling
def find_best_match(user_message, dataset):
    user_message_set = set(user_message)  # Convert user_message to a set for faster lookups
    best_response = None
    highest_priority = -1

    for index, row in dataset.iterrows():
        keywords = set(row['Keywords'].split(','))  # Convert keywords to a set
        if keywords.issubset(user_message_set):  # Check if all keywords are present in user_message
            response = row['Response']  # Assuming 'Response' column
            priority = int(row['Priority']) if 'Priority' in row else 1
            if priority > highest_priority:
                best_response = response
                highest_priority = priority

    return best_response

# Function to handle message probability (can remain unchanged)
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

# Check all messages and determine the best response
def check_all_messages(message, dataset):
    best_match = find_best_match(message, dataset)
    return best_match if best_match else unknown()

# Function for unknown responses
def unknown():
    response = ["I'm not sure I understand. Can you ask about procurement?",
                "I couldn't catch that. Please try rephrasing.",
                "I'm not sure what you're asking. Do you need help with procurement?",
                "That doesn't seem related to procurement. Can you clarify?"][
        random.randrange(4)]
    return response

# Function to get chatbot response
def get_response(user_input, dataset):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message, dataset)

    # Handle specific cases manually if needed
    if any(word in split_message for word in ["thank", "thanks"]):
        response = "You're welcome! If you have any more questions, just let me know."

    return response

# Streamlit-based interaction
def main():
    st.title("Procurement Chatbot")

    # Instructions
    st.write("Ask me anything about the procurement process! Type your question below:")

    # Input field for user message
    user_input = st.text_input("You:", "")

    if st.button("Send") or user_input:
        # Get chatbot response
        bot_response = get_response(user_input, procurement_data)

        # Display the chatbot response
        st.write(f"Bot: {bot_response}")

if __name__ == '__main__':
    main()
