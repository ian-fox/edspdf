import pandas as pd

from edspdf.visualization.merge import merge_lines

lines = [
    dict(page=0, x0=0, x1=1, y0=0, y1=0.1, label="body"),
    dict(page=0, x0=0, x1=1, y0=0.1, y1=0.2, label="body"),
    dict(page=0, x0=0, x1=0.4, y0=0.2, y1=0.3, label="body"),
    dict(page=0, x0=0.6, x1=1, y0=0.2, y1=0.3, label="other"),
    dict(page=1, x0=0.6, x1=1, y0=0.2, y1=0.3, label="body"),
]


def test_merge():

    df = pd.DataFrame.from_records(lines)
    out = merge_lines(df)

    assert len(out) == 4

    l0, l1, l2, l3 = out.to_dict(orient="records")

    assert l0 == dict(page=0, x0=0, x1=1, y0=0, y1=0.2, label="body")
    assert l1 == dict(page=0, x0=0, x1=0.4, y0=0.2, y1=0.3, label="body")
    assert l2 == dict(page=0, x0=0.6, x1=1, y0=0.2, y1=0.3, label="other")
    assert l3 == dict(page=1, x0=0.6, x1=1, y0=0.2, y1=0.3, label="body")
