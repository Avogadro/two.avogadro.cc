(menus-edit-menu)=

# Edit Menu

The Edit menu contains commands useful for typical manipulation of the file at hand.

Undo
: Undo the last made change to the document.

Redo
: Redo the last undo operation on the document.

Cut
: Cut any selected atoms/molecules, removing them from the document and placing them in the clipboard.

Copy
: Copy any selected atoms/molecules, keeping them in the document and placing them in the clipboard.

Copy As
: Copy the selected atoms/molecules as a text representation in either SMILES or InChI format.

Copy Graphics
: Copy the current viewing window as an image.

:::{note}
The Copy Graphics function copies the image in the `.png` format with the same resolution as the viewing window. This means a smaller viewing window will produce a lower resolution image.
:::

Paste
: Paste the last object in the clipboard.

:::{note}
The Paste function only works if the object on the clipboard is in CJSON format.
:::

Delete
: Delete any selected atoms/molecules from the document.
