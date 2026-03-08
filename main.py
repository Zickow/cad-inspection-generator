from dxf_parser import extract_dimensions
from excel_generator import create_inspection_sheet
from pdf_balloon import create_ballooned_pdf


def main() -> None:
    dxf_file = "sample.dxf"
    pdf_file = "sample.pdf"

    rows = extract_dimensions(dxf_file)

    if not rows:
        rows = [
            {
                "balloon": 1,
                "dimension": "2.170",
                "type": "Hole Location",
                "qty": 1,
                "tolerance": "",
                "lower_limit": "",
                "upper_limit": "",
                "measured": "",
                "result": "",
                "notes": "",
                "x": 0,
                "y": 0,
            },
            {
                "balloon": 2,
                "dimension": "0.590",
                "type": "Hole Diameter",
                "qty": 1,
                "tolerance": "",
                "lower_limit": "",
                "upper_limit": "",
                "measured": "",
                "result": "",
                "notes": "",
                "x": 0,
                "y": 0,
            },
        ]

    create_inspection_sheet(rows, "inspection_sheet.xlsx")
    create_ballooned_pdf(pdf_file, "ballooned_output.pdf", rows)

    print("Generated:")
    print("- inspection_sheet.xlsx")
    print("- ballooned_output.pdf")


if __name__ == "__main__":
    main()