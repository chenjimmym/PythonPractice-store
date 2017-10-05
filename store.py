class store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    def addProduct(self, item):
        self.products.append(item)
        return self
    def removeProduct(self, item):
        temp = []
        for data in self.products:
            if data == item:
                continue
            else:
                temp.append(data)
        self.products = temp
        return self
    def inventory(self):
        print 'List of Products in Store'
        for data in self.products:
            if data == 'iPhone':
                print 'iPhone: a smartphone'
            elif data == 'iPad':
                print 'iPad: a tablet'
            elif data == 'Macbook':
                print 'Macbook: a laptop'
            elif data == 'Apple TV':
                print 'Apple TV: a TV streamer'
        return self


store1 = store(['iPhone','iPad','Macbook'], 'Cupertino', 'Steve')
store1.addProduct('Apple TV').removeProduct('iPad')
print store1.products
store1.inventory()