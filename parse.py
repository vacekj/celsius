import camelot

print("Parsing")
tables = camelot.read_pdf('celsius.pdf',
                          pages='47',
                          flavor='stream',
                          table_areas=['0,750,612,0'],
                          edge_tol=500)

print("Debugging")
# camelot.plot(tables[0], kind='contour').show()
# camelot.plot(tables[0], kind='grid').show()

print("Exporting")
tables.export('db.html', f='html')
