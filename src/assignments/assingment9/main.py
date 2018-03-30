from src.assignments.assignment9.invoice import Invoice
from src.assignments.assignment9.invoice_item import InvoiceItem
#Write import statements for classes invoice and invoice_item
'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object
In the loop:
Create a new InvoiceItem
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''
invoice = Invoice('ABC Company', '03282018')

keep_going='y'

while keep_going == 'y':
    description = input('Enter Descripton: ')
    quantity = int(input('Enter Quantity: '))
    cost = float(input('Enter Cost: '))

    invoice_item = InvoiceItem(description, quantity, cost)
    invoice.add_invoice_item(invoice_item)

    keep_going = input('Type y to continue...')

    if keep_going != 'y':
        invoice.print_invoice()
