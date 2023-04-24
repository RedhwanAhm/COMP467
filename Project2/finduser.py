
import os

# Get the current user
current_user = os.environ.get('USERNAME') or os.environ.get('USER')

# Print the current user
print("The current user is:", current_user)