from python_design_patterns.design_patterns.creational.factory_method import TextDocument, Presentation, Spreadsheet, TextEditor, SpreadsheetEditor, PresentationEditor


def test_text_document():
    doc = TextDocument()
    assert doc.open() == "Opening text document"
    assert doc.save() == "Saving text document"

def test_spreadsheet_document():
    doc = Spreadsheet()
    assert doc.open() == "Opening spreadsheet"
    assert doc.save() == "Saving spreadsheet"

def test_presentation_document():
    doc = Presentation()
    assert doc.open() == "Opening presentation"
    assert doc.save() == "Saving presentation"

def test_text_editor():
    editor = TextEditor()
    doc = editor.new_document()
    assert isinstance(doc, TextDocument)

def test_spreadsheet_editor():
    editor = SpreadsheetEditor()
    doc = editor.new_document()
    assert isinstance(doc, Spreadsheet)

def test_presentation_editor():
    editor = PresentationEditor()
    doc = editor.new_document()
    assert isinstance(doc, Presentation)
