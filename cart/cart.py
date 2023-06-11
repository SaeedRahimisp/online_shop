from products.models import Product

class Cart:
    def __init__(self, request):
        """"
        Initialize the cart
        """
        self.request = request

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity=1):
        """"
        Add the specified product to the cart
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        """"
        Remove the specified product from the cart
        """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """"
        Save the cart's changes
        """
        self.session.modified = True

    def __iter__(self):
        """"
        Get the products objects from product model and show
        """
        product_id = self.cart.keys()
        products = Product.objects.filter(id__in=product_id)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            yield item

    def __len__(self):
        """"
        Length of the cart
        """
        return len(self.cart.keys())

    def clear(self):
        """"
        Clear products in cart
        """
        del self.session['cart']
        self.save()

    def get_total_price(self):
        """"
        Show the total of price
        """
        product_id = self.cart.keys()
        products = Product.objects.get(id__in=product_id)

        return sum(products.price for product in products)
