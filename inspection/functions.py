from .models import CCOS, Remark
import openpyxl as xl
from openpyxl.cell.text import InlineFont
from openpyxl.cell.rich_text import TextBlock, CellRichText



def generate_excel(obj:CCOS) -> bytes:
    wb = xl.load_workbook('template.xlsx')
    sheet = wb['Blank IR - Template']
    
    sheet['F1'] = obj.number
    sheet['I3'] = obj.creation_date.strftime('%d.%m.%y')
    sheet['F9'] = f'Yard: {obj.yard.employer}/{obj.yard}'
    # sheet['F9'] = CellRichText(
    #     'Yard: ', TextBlock(InlineFont(b=True,), f'{obj.yard.employer}/{obj.yard}')
    # )
    sheet['A10'] = f'Class: {obj.u_class.employer}/{obj.u_class}'
    sheet['A11'] = f'Client/Owner: {obj.owner.employer}/{obj.owner}'
    
    # ADDING THE REMARKS
    r = Remark.objects.filter(element__inspection=obj.id)
    class_remarks = []
    owner_remarks = []
    for remark in r:
        if remark.created_by.person.employer.type == 0:
            class_remarks.append((remark.body, remark.closed_on))
        
        else:
            owner_remarks.append((remark.body, remark.closed_on))
    
    row = 34
    for x, remark in enumerate(class_remarks):
        sheet[f'B{row}'] = x + 1
        sheet[f'c{row}'] = remark[0]
        
        if remark[1]:
            sheet[f'H{row}'] = remark[1].strftime('%d/%m/%y')
            
        row += 1
        
    wb.save('result.xlsx')
    return b''