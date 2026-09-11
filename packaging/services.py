from itertools import permutations

from .models import Product, Box


def get_orientations(length, width, height):
    """
    Return all unique rotations of an item.
    """
    return list(set(
        permutations([length, width, height])
    ))


def fits_in_space(item, space):
    """
    Check whether an item can fit inside a free space.

    item = (length, width, height)
    space = (length, width, height)
    """

    return (
        item[0] <= space[0]
        and item[1] <= space[1]
        and item[2] <= space[2]
    )


def split_space(space, item):
    """
    After placing an item in a space, create
    the remaining usable spaces.

    We use a simple shelf-style 3D packing strategy.
    """

    space_length, space_width, space_height = space
    item_length, item_width, item_height = item

    remaining_spaces = []

    # Space to the right of the item
    if space_length > item_length:
        remaining_spaces.append(
            (
                space_length - item_length,
                space_width,
                space_height,
            )
        )

    # Space behind the item
    if space_width > item_width:
        remaining_spaces.append(
            (
                item_length,
                space_width - item_width,
                space_height,
            )
        )

    # Space above the item
    if space_height > item_height:
        remaining_spaces.append(
            (
                item_length,
                item_width,
                space_height - item_height,
            )
        )

    return remaining_spaces


def can_pack_products(products, box):
    """
    Try to pack all products into the box.

    Products may be rotated.

    This is a heuristic 3D packing algorithm, not
    an exact optimal bin-packing algorithm.
    """

    box_space = (
        box.length,
        box.width,
        box.height,
    )

    # Start with one free space representing the whole box.
    free_spaces = [box_space]

    # Larger products first generally produce better packing.
    products = sorted(
        products,
        key=lambda product: (
            product.length
            * product.width
            * product.height
        ),
        reverse=True,
    )

    for product in products:

        product_dimensions = (
            product.length,
            product.width,
            product.height,
        )

        placed = False

        for space_index, space in enumerate(free_spaces):

            orientations = get_orientations(
                *product_dimensions
            )

            for orientation in orientations:

                if not fits_in_space(
                    orientation,
                    space,
                ):
                    continue

                # Remove the space where the product
                # was placed.
                free_spaces.pop(space_index)

                # Add newly available spaces.
                new_spaces = split_space(
                    space,
                    orientation,
                )

                free_spaces.extend(new_spaces)

                placed = True
                break

            if placed:
                break

        if not placed:
            return False

    return True


def recommend_box(products):
    """
    Find the cheapest box that can contain all products.
    """

    product_objects = []

    total_weight = 0

    for product_data in products:

        try:
            product = Product.objects.get(
                id=product_data["product_id"]
            )
        except Product.DoesNotExist:
            raise ValueError(
                f"Product with id "
                f"{product_data['product_id']} "
                f"does not exist."
            )

        quantity = product_data.get(
            "quantity",
            1,
        )

        for _ in range(quantity):
            product_objects.append(product)

        total_weight += (
            product.weight * quantity
        )

    suitable_boxes = []

    for box in Box.objects.all():

        # Check total weight first.
        if total_weight > box.max_weight:
            continue

        # Check whether all products can be packed.
        if can_pack_products(
            product_objects,
            box,
        ):
            suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    # Cheapest suitable box.
    suitable_boxes.sort(
        key=lambda box: box.cost
    )

    return suitable_boxes[0]