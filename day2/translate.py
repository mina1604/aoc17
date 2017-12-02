import sys

cells = []

rowCount = 0
for row in sys.stdin:
    rowCount = rowCount + 1
    for cell in row.split('\t'):

        print 'cell(' + str(rowCount) + ',' + str(cell.strip()) + ').'

print 'row(1 .. ' + str(rowCount) + ').'
