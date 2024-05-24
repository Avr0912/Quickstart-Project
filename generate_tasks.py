import uuid
import random

# Define the number of tasks to generate
num_tasks = 1000000

# Define the output filename
output_filename = 'tasks.txt'

# Function to generate a random task name
def generate_task_name(task_number):
    return f"Task {task_number}"

# Function to generate a random priority
def generate_task_priority():
    return random.randint(1, 5)

# Function to generate a list of random tasks and write to a file
def generate_and_write_tasks(filename, num_tasks):
    with open(filename, mode='w') as file:
        for i in range(num_tasks):
            task_id = str(uuid.uuid4())
            task_name = generate_task_name(i + 1)
            task_priority = generate_task_priority()
            file.write(f"{task_id}, {task_name}, {task_priority}\n")

# Main function
def main():
    generate_and_write_tasks(output_filename, num_tasks)
    print(f"Generated {num_tasks} tasks and wrote to {output_filename}")

if __name__ == "__main__":
    main()
