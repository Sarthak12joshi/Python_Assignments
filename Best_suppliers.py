#Find Best Supplier
productData = {
    'prod1':['Supp1','Supp2','Supp3'],
    'prod2':['Supp3','Supp4','Supp5'],
    'prod3':['Supp1','Supp3','Supp5']
}

#Best Supplier for (prod1,prod3), (prod2,prod3), (prod1,prod2)


def best_supplier(a,b):
    set_a = set(productData[a])
    print('The suppliers for {} are : {}'.format(a,set_a)) 
    set_b = set(productData[b])
    print('The suppliers for {} are : {}'.format(b,set_b))
    print('The best supplier for {} and {} is {} '.format(a,b,set_a.intersection(set_b)))

best_supplier('prod2','prod3')
