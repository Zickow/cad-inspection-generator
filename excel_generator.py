from openpyxl import Workbook
from openpyxl.styles import Font


HEADERS = [
    "Balloon #",
    "Dimension",
    "Type",
    "Qty",
    "Tolerance",
    "Lower Limit",
    "Upper Limit",
    "Measured",
    "Result",
    "Notes",
]


def create_inspection_sheet(rows: list[dict], output_path: str) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Inspection Sheet"

    ws.append(HEADERS)

    for cell in ws[1]:
        cell.font = Font(bold=True)

    for row in rows:
        ws.append(
            [
                row["balloon"],
                row["dimension"],
                row["type"],
                row["qty"],
                row["tolerance"],
                row["lower_limit"],
                row["upper_limit"],
                row["measured"],
                row["result"],
                row["notes"],
            ]
        )

    for column in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
        ws.column_dimensions[column].width = 18

    wb.save(output_path)