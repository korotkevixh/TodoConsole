tasks = {}

# глобальная блокировка интерпритатора
# многопоточка, многопроцессорность, ассинхронка
# async - полностью асинк программирование 

def main_loop():
    def parse_command(command):
        parts = command.split()
        if not parts:
            return
        cmd = parts[0].lower()
        args = parts[1:]
        if cmd == "add":
            handle_add(args)
        elif cmd == "update":
            handle_update(args)
        elif cmd == "remove":
            handle_remove(args)
        elif cmd == "stats":
            handle_stats()
        elif cmd == "done":
            handle_done(args)
        elif cmd == "exit":
            return True
        elif cmd == "help":
            print("All commands: ")
            print("< help")
            print("< add -> (id, value)")
            print("< stats")
            print("< exit")
        else: 
            print("Unknown command")


    def handle_add(args):
        if len(args) < 2:
            print("Error: not enough arguments")
            return
        try: 
            task_id = int(args[0])

        except ValueError:
            print("Error: the ID must be an integer value")
            return
        if task_id in tasks:
            print(f"Error: task with ID {task_id} already included")
            return
        text = " ".join(args[1:]).strip()
        if not text:
            print("Error: task text can't be empty")
            return
        tasks[task_id] = {"text": text, "done": False}
        print(f"Task [{task_id}] added: {text}")


    def handle_stats():
        if not tasks:
            print("Error: no tasks")
            return
        print("Current tasks")
        print("-" * 20)
        for task_id, task in tasks.items():
            status = "✓" if task["done"] else "✗"
            print(f"[{task_id}] {task['text']} {status}")

    def handle_done(args):
        if not args:
            print("Error: no task ID provided")
            return
        try:
            task_id=int(args[0])
        except ValueError:
            print("Error: task ID must be an integer value")
            return
        if task_id not in tasks:
            print(f"Error: no task with ID {task_id}")
            return
        if tasks[task_id]["done"]:
            print(f"Task [{task_id}] is already marked as done")
            return
        tasks[task_id]["done"] = True
        print(f"Task [{task_id}] marked as done: {tasks[task_id]['text']}")


    def handle_remove(args):
        if not args:
            print("Error: no task ID provided")
            return
        try:
            task_id=int(args[0])
        except ValueError:
            print("Error: task ID must be an integer value")
            return
        if task_id not in tasks:
            print(f"Error: no task with ID {task_id}")
            return
        del tasks[task_id]
        print(f"Task [{task_id}] successfuly removed! ✓")


    def handle_update(args):
        if not args:
            print("Error: no task ID provided")
            return
        try:
            task_id=int(args[0])
        except ValueError:
            print("Error: task ID must be an integer value")
            return
        if task_id not in tasks:
            print(f"Error: no task with ID {task_id}")
            return
        if len(args) < 2:
            print("Error: no new text provided")
            return
        new_text = " ".join(args[1:]).strip()
        if not new_text:
            print("Error: new text is empty")
            return
        tasks[task_id]["text"] = new_text
        print(f"Task [{task_id}] updated: {new_text}")


            
        
    

    while True: 
        print("help -> see all commands")
        print("Enter command: ")
        command = input("> ")
        if parse_command(command):
            break


main_loop()

