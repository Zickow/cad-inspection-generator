# CAD Inspection Generator

This project demonstrates a Python-based desktop automation workflow for manufacturing inspection documentation.

## Vad demo:t ska gora
Det ska visa tre saker:

- lasa en DXF
- skapa en inspection sheet i Excel
- skapa en ballooned PDF mock output

Det behover inte vara perfekt. Det ska bara bevisa:

- Python desktop tool
- CAD/DXF workflow
- PDF + Excel output

## What it does
- Parses DXF engineering drawings
- Extracts dimension data
- Generates an Excel inspection sheet
- Creates a ballooned PDF output (or mock output when no input PDF exists)

## Tech stack
- Python
- ezdxf
- PyMuPDF
- openpyxl

## Output
- `inspection_sheet.xlsx`
- `ballooned_output.pdf`

## Use case
This proof of concept is designed for quality-control workflows where engineering drawings need to be converted into inspection-ready documentation.

## How to run
```bash
pip install -r requirements.txt
python main.py
```

## Filstruktur
```text
cad-inspection-generator/
|-- main.py
|-- dxf_parser.py
|-- excel_generator.py
|-- pdf_balloon.py
|-- requirements.txt
`-- README.md
```
