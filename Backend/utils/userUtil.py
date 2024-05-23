# Define currentUser as a global variable
currentUser = None


# Function to update the currentUser variable
def update_current_user(user):
    global currentUser
    currentUser = user


# Function to get the currentUser
def get_current_user():
    return currentUser
