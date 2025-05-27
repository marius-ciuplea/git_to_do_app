import json

TASK_FILE = "tasks.json"

def load_tasks():
	try:
		with open(TASK_FILE, "r") as file:
			return json.load(file)
	except FileNotFoundError:
		return []

def save_task(tasks):
	with open(TASK_FILE, "w") as file:
		json.dump(tasks, file, indent=4)

def add_task(task):
	tasks = load_tasks()
	tasks.append({"task": task, 'done': False})
	save_task(tasks)
	print(f'Added: {task}')

def view_tasks():
	tasks = load_tasks()
	if not tasks:
		print('No tasks yet!')
	else:
		for i, task in enumerate(tasks, 1):
			status ="✔" if task["done"] else "✘"
			print(f"{i}. {task['task']} [{status}]")


def mark_done(task_number):
	tasks = load_tasks()

	if 1 <= task_number <= len(tasks):  # Validate task number
		task = tasks[task_number - 1]

		if task["done"]:
			print(f"Task '{task['task']}' is already marked as done.")
		else:
			task["done"] = True  # Mark task as done
			save_task(tasks)  # Save updated tasks
			print(f"Marked '{task['task']}' as done!")
	else:
		print("Invalid task number.")


def delete_task(task_number):
	tasks = load_tasks()
	if 1 <= task_number <= len(tasks):
		removed_task = tasks.pop(task_number - 1)
		save_task(tasks)
		print(f"Deleted: {removed_task['task']}")
	else:
		print('Invalid task number.')

def main():
	while True:
		print("\nOptions: [1] Add [2] View [3] Done [4] Delete [5] Exit")
		choice = input('Choose an option: ')

		match choice:
			case '1':
				task = input('Enter task: ')
				add_task(task)
			case '2':
				view_tasks()
			case '3':
				view_tasks()
				try:
					num = int(input('Enter task number to mark as done: '))
					mark_done(num)
				except ValueError:
					print('Please enter a valid number.')
			case '4':
				view_tasks()
				try:
					num =int(input('Enter task number to delete:'))
					delete_task(num)
				except ValueError:
					print('Enter a valid number.')
			case '5':
				print('Goodbye!')
				break
			case _:
				print('Invalid choice, try again.')

if __name__ == '__main__':
	main()

