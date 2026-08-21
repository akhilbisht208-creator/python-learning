#write a program to fill in a letter template given below with name and date(not cleared)

letter = ''' Dear < | Name | >,
        you are selected!
        <|Date|>'''
print(letter.replace("<|Name|>","akhil").replace("<|Date|","22 september 2008"))