# CAD Inspection Generator

Python tool for automatically generating **ballooned engineering drawings** and **inspection sheets** from CAD drawings.

This project focuses on automating quality-inspection documentation used in manufacturing workflows.

---

# Problem

In many manufacturing environments, quality engineers must manually:

• review engineering drawings
• identify inspection-relevant dimensions
• create ballooned drawings
• build inspection sheets for measurement recording

This manual workflow is slow and error-prone.

The goal of this project is to **automate the inspection documentation process directly from CAD drawings.**

---

# Solution Overview

The system processes engineering drawings exported from CAD systems and generates inspection documentation automatically.

### Input

• Engineering drawing (PDF)
• Matching CAD file (DXF)

### Output

• Ballooned inspection drawing
• Excel inspection sheet

---

# System Workflow

Engineering Drawing (PDF + DXF)

↓

DXF Dimension Parsing

↓

Inspection Feature Detection

↓

Balloon Number Assignment

↓

Inspection Sheet Generation

↓

Ballooned Drawing Output

---

# Features

• Parse DXF CAD drawings
• Detect inspection-relevant dimensions
• Assign balloon numbers automatically
• Generate structured inspection sheets
• Export inspection documentation to Excel
• Prepare ballooned engineering drawings

The system is designed to support **manufacturing quality workflows** where dimensional inspection is required.

---

# Inspection Sheet Format

Generated inspection sheets include the following fields:

| Field       | Description                 |
| ----------- | --------------------------- |
| Balloon #   | Inspection reference number |
| Dimension   | Nominal dimension           |
| Type        | Feature type                |
| Qty         | Quantity                    |
| Tolerance   | Allowed tolerance           |
| Lower Limit | Minimum value               |
| Upper Limit | Maximum value               |
| Measured    | Actual measured value       |
| Result      | Pass / Fail                 |
| Notes       | Inspector comments          |

Conditional formatting can highlight inspection results.

---

# Technology Stack

Python libraries used:

• **ezdxf** – DXF CAD file parsing
• **PyMuPDF** – PDF annotation and processing
• **openpyxl** – Excel inspection sheet generation
• **NumPy** – coordinate and geometry calculations

Desktop application layer:

• **PySide6** or **Tkinter**

Executable packaging:

• **PyInstaller**

---

# Project Structure

cad-inspection-generator/

main.py
dxf_parser.py
pdf_parser.py
inspection_generator.py
requirements.txt
README.md

---

# Planned Desktop Tool

The final version will run as a **Windows desktop application**.

User workflow:

1. Load drawing files (PDF + DXF)
2. Click **Generate Inspection**
3. Receive generated files automatically

Outputs:

• Ballooned drawing PDF
• Inspection sheet Excel file

No Python installation required for end users.

---

# Use Case

Manufacturing companies often need to convert engineering drawings into inspection documentation for quality control.

This tool automates that conversion process and helps standardize inspection preparation.

---

# Project Status

Early prototype.

Current development focuses on:

• DXF dimension parsing
• inspection sheet generation
• balloon placement logic

---

# Author

Zakaria B
Python Developer
Automation • Data Processing • Engineering Tools

