import json
import os

DATA_FILE = "data/todo-list.json"

# ✅ Load existing tasks or create empty list
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# ✅ Save tasks back to JSON
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# ✅ Add new task
def add_task(task_name):
    tasks = load_tasks()
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print(f"✅ Added: {task_name}")

# ✅ View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks yet.")
        return
    print("\nYour To-Do List:")
    for i, t in enumerate(tasks, start=1):
        status = "✔️" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")

# ✅ Mark task as done
def mark_done(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"🎉 Marked as done: {tasks[index - 1]['task']}")
    except IndexError:
        print("⚠️ Invalid task number.")

# ✅ Delete a task
def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed['task']}")
    except IndexError:
        print("⚠️ Invalid task number.")

# ✅ Main program menu
def main():
    while True:
        print("\n📋 TO-DO LIST MENU")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                add_task(task)
            else:
                print("⚠️ Task name cannot be empty.")
        elif choice == "3":
            view_tasks()
            try:
                num = int(input("Enter task number to mark done: "))
                mark_done(num)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "4":
            view_tasks()
            try:
                num = int(input("Enter task number to delete: "))
                delete_task(num)
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
