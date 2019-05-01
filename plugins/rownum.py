from visidata import Sheet, undoAddCols


Sheet.addCommand(None, 'addcol-rownum', 'addColumn(Column("rownum", type=int, getter=sheet.rowNumber), cursorColIndex)', undo=undoAddCols, helpstr='add column with original row ordering')


@Sheet.cached_property
def rowNumbers(sheet):
    'original row numbers for rows added with addRow'
    return {}     # [rowid(row)] -> rowidx


@Sheet.api
def rowNumber(sheet, col, row):
    return sheet.rowNumbers.get(sheet.rowid(row))


@Sheet.api
def addRow(sheet, row, index=None):
    if index is None:
        index = len(sheet.rows)

    sheet.rowNumbers[sheet.rowid(row)] = index
    return addRow.__wrapped__(sheet, row, index)
