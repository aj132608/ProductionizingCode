class ProductFilter:
    """
    This class contains filters to retrieve products that fit a
    requirement.
    """
    def filter_by_color(self, products, color):
        """

        This function filters by a product's color

        :param products: list of Product objects
        :param color: desired color that will be used for filtering
        :returns: all products of the specified color
        """
        for p in products:
            # Selects products of the specified color
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        """

        This function filters by a product's size

        :param products: list of Product objects
        :param size: desired size that will be used for filtering
        :returns: all products of the specified color
        """
        for p in products:
            # Selects products of the specified size
            if p.size == size:
                yield p
