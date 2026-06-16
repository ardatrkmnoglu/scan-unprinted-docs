# Unprinted Document Scanner

**In big 2026**, some authorities may still request printed and hand-filled documents just as a matter of formality.
Yes, you usually fill out your documents from your iPad. But some of the "old-fashioned" officials may want you to print and fill out requested forms (sometimes it may be required due to security concerns, I cannot say anything about that). If you think this kind of requirement is ridiculous, this tiny script may be useful for you.

##### "Make your digitally-annotated documents look as if they are printed, filled out by hand, and then scanned."

## Example Usage
- `python scan.py requestedimportant.pdf -o requestedimportant_scanned.pdf`
- `python scan.py anotherrequested.pdf` (the output file will be named as `output.pdf` if name was not specified)

### Dependencies
- `pdf2image`
- `Pillow`
