import fitz


def create_ballooned_pdf(input_pdf: str, output_pdf: str, rows: list[dict]) -> None:
    try:
        doc = fitz.open(input_pdf)
        page = doc[0]
    except Exception:
        doc = fitz.open()
        page = doc.new_page(width=842, height=595)
        page.insert_text((40, 30), "Mock ballooned output", fontsize=12)

    start_x = 50
    start_y = 50
    step_y = 28

    for i, row in enumerate(rows[:10], start=0):
        x = start_x
        y = start_y + i * step_y

        page.draw_circle((x, y), 12, color=(1, 0, 0), width=1.5)
        page.insert_text((x - 4, y + 4), str(row["balloon"]), fontsize=10)

    doc.save(output_pdf)
    doc.close()