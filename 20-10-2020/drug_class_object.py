#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:43:25 2020

@author: glenfish
"""

class Drug:
    def __init__(self, code=str, brand=str, name=str, desc=str, capsules=int):
        self.code = code
        self.brand = brand
        self.name = name
        self.desc = desc
        self.capsules = capsules
    def getDrugInfo(self):
        return print('Code: ',self.code,'\nBrand: ',self.brand,'\nName: ',self.name,'\nDescription: ',self.desc,'\nQTY: ',str(self.capsules),'\n')
        
drug1 = Drug('AE7yy','GNC','Mega Men','men\'s multi-vitamin',180)
drug2 = Drug('B09ty5','Thompson\'s','One-A-Day Milk Thistle','Traditional herb that supports liver and digestive health',60)
drug3= Drug('Dbh47f', 'CVS Health', 'Vitamin C', 'Vitamin C is good for your immune system', 200)
druglist = []
druglist.append(drug1.getDrugInfo())
druglist.append(drug2.getDrugInfo())
druglist.append(drug3.getDrugInfo())
print(druglist)

# drug2.getDrugInfo()

# print(drug1.brand)


class DrugCabinet:
    def __init__(self,code=str,drug=str,qty=int):
        self.code = code
        self.drug = drug
        self.qty = qty
    def getDrugCabinetInfo(self):
        return('Contents of drug cabinet ',self.code,': \n' + str(self.qty),self.drug)
cab1 = []        
cab1.append(DrugCabinet('A1',drug1.name,1000))
cab1.append(DrugCabinet('A1',drug2.name,5000))
print(cab1[0].getDrugCabinetInfo())
print(cab1[1].getDrugCabinetInfo())
