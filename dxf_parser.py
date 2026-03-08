import ezdxf


def extract_dimensions(dxf_path: str) -> list[dict]:
    try:
        doc = ezdxf.readfile(dxf_path)
    except Exception:
        return []

    msp = doc.modelspace()

    dimensions = []
    counter = 1

    for entity in msp.query("DIMENSION"):
        try:
            measurement = getattr(entity.dxf, "actual_measurement", None)
            text = getattr(entity.dxf, "text", "") or ""
            defpoint = getattr(entity.dxf, "defpoint", None)

            x = getattr(defpoint, "x", 0.0) if defpoint else 0.0
            y = getattr(defpoint, "y", 0.0) if defpoint else 0.0

            dimensions.append(
                {
                    "balloon": counter,
                    "dimension": text if text not in ("<>", "") else str(measurement or ""),
                    "type": "Inspection",
                    "qty": 1,
                    "tolerance": "",
                    "lower_limit": "",
                    "upper_limit": "",
                    "measured": "",
                    "result": "",
                    "notes": "",
                    "x": x,
                    "y": y,
                }
            )
            counter += 1
        except Exception:
            continue

    return dimensions