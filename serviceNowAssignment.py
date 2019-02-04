import csv

class Node:

    def __init__(self, data):
        self.data = data;
        self.children = [];

    def addChild(self, obj):
        self.children.append(obj);

        
f = open('BusinessData.csv')
csv_f = csv.reader(f)

vendorList = [];
productList = [];
priceList = [];

for row in csv_f:
    vendorList.append(row[1])
    productList.append(row[2])
    priceList.append(row[3])
    
productList.remove('Product')
vendorList.remove('Vendor')
priceList.remove('Amount')

print(vendorList)
print(productList)
print(priceList)
print(len(vendorList))
i = 0;
vendorNodes = [];
while i < len(vendorList):
    vendorNodes[i] = Node(vendorList[i]);
    i += 1;
    
print(vendorNodes)    
