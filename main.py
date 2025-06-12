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
        # elif cmd == "update":
        #     handle_update(args)
        # elif cmd == "remove":
        #     handle_remove(args)
        # elif cmd == "list":
        #     handle_list(args)
        # elif cmd == "stats":
        #     handle_stats()
        # elif cmd == "get":
        #     handle_get(args)
        # elif cmd == "done":
        #     handle_done(args)
        elif cmd == "exit":
            return True
        elif cmd == "help":
            print("All commands: ")
            print("< help")
            print("< add")
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
            print("Error: the ID must be integer value")
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

    while True: 
        print("Enter command: ")
        command = input("> ")
        if parse_command(command):
            break
main_loop()

