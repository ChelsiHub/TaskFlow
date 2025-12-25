import sys
from datetime import datetime
from rich.console import Console
from rich.table import Table

from execution.execution_store import save_execution
from tasks.task_registry import TaskRegistry
from tasks.automation_engine import AutomationEngine
from reports.report_generator import ReportGenerator
from notification.notifier import Notifier
from config.settings import EMAIL_CONFIG
from utils.logger import setup_logger

logger = setup_logger()
console = Console()
notifier = Notifier(EMAIL_CONFIG)
report_generator = ReportGenerator()
task_registry = TaskRegistry()
automation_engine = AutomationEngine()

# -------------------------------
# Core CLI functions
# -------------------------------

def run_tasks():
    tasks = task_registry.list_tasks()
    enabled_tasks = [t for t in tasks if t.enabled]

    if not enabled_tasks:
        console.print("[yellow]No enabled tasks found[/yellow]")
        return

    for task in enabled_tasks:
        start = datetime.now()
        try:
            console.print(f"[cyan]Running task:[/cyan] {task.name}")
            automation_engine.execute_task(task)
            status = "SUCCESS"
            error = None
        except Exception as e:
            status = "FAILED"
            error = str(e)
            console.print(f"[red]Task failed:[/red] {task.name} | {error}")
        end = datetime.now()
        save_execution(
            task_id=task.id,
            task_name=task.name,
            status=status,
            start_time=start,
            end_time=end,
            error=error
        )

    console.print("[green]All tasks executed[/green]")
    notifier.send_failure_alerts()
    report_generator.generate_daily_report()

def view_status():
    registry = report_generator.registry
    executions = registry.executions
    if not executions:
        console.print("[yellow]No executions found[/yellow]")
        return

    table = Table(title="Task Execution History")
    table.add_column("Task ID", style="cyan")
    table.add_column("Task Name", style="green")
    table.add_column("Status", style="magenta")
    table.add_column("Start Time", style="yellow")
    table.add_column("End Time", style="yellow")
    table.add_column("Duration(s)", style="blue")
    table.add_column("Error", style="red")

    for e in executions:
        table.add_row(
            e["task_id"],
            e["task_name"],
            e["status"],
            e["start_time"],
            e.get("end_time") or "",
            str(e.get("duration_seconds") or ""),
            e.get("error_message") or ""
        )

    console.print(table)

def generate_reports():
    summary = report_generator.generate_daily_report()
    console.print("[green]Reports generated[/green]")
    console.print(summary)

# -------------------------------
# CLI Menu
# -------------------------------
def main_menu():
    while True:
        console.print("\n[bold blue]TaskFlow CLI Menu[/bold blue]")
        console.print("1. Run Tasks Manually")
        console.print("2. View Task Status / History")
        console.print("3. Generate Reports")
        console.print("4. Exit")

        choice = console.input("\nEnter your choice: ")

        if choice == "1":
            run_tasks()
        elif choice == "2":
            view_status()
        elif choice == "3":
            generate_reports()
        elif choice == "4":
            console.print("[bold green]Exiting TaskFlow CLI[/bold green]")
            sys.exit(0)
        else:
            console.print("[red]Invalid choice. Try again.[/red]")

if __name__ == "__main__":
    main_menu()
