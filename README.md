# UK Strowger symbols - kicad library

Attempt to produce a set of symbols for drawing schematics of GPO style strowger equipment.

## Installation
TODO: Write some instructions for how to imprt this library into Kicad

## ATW22001
The standard for GPO strowger diagrams is ATW2201: http://www.samhallas.co.uk/repository/po_docs/atw_22001.pdf

This document is extensive, and while this project aims to implement the symbols described in the standard, it is incomplete.

## Symbol labels
By default, kicad will try to auto-place the symbol labels, this messes up things like the coil values in the relay symbols.

You can fix this by turning off the auto placement, in `preferences -> Eeschema -> Editing Options -> Symbol Field Automatic Placement` and untick any boxes related to autoplacement.

## Grid settings
Most of the symbols in this library have pins placed on the default 50mil grid spacing.  However, that proved impractical for some symbols with high pin counts (eg uniselector banks with all pins broken out) 

So these symbols have pins on a 25mil grid spacing instead.  You may need to change your grid size in the schematic editor to successfully connect wires to these symbols.

## Contributing
I really don't know at this stage how well PRs are going to work on kicad files, but you're welcome to try and raise a PR and I'll see if it's mergable.
