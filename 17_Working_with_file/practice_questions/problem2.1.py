# Open tasks.txt in append mode and add a new line "Task Completed!".
with open("tasks.txt","a",encoding="utf-8") as f:
    content=f.write("Task Completed!")