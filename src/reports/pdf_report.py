from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from config.settings import REPORT_DIR
from execution.execution_registry import ExecutionRegistry


def generate_pdf_report():
    registry = ExecutionRegistry()
    executions = registry.executions

    if not executions:
        return None

    today = date.today().isoformat()
    pdf_path = REPORT_DIR / f"execution_report_{today}.pdf"

    c = canvas.Canvas(str(pdf_path), pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica", 10)

    c.drawString(50, y, f"TaskFlow Execution Report - {today}")
    y -= 30

    for e in executions:
        line = f"{e['task_name']} | {e['status']} | {e['duration_seconds']}s"
        c.drawString(50, y, line)
        y -= 15

        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    return pdf_path
